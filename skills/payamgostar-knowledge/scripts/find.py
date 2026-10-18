#!/usr/bin/env python3
"""Search PayamGostar knowledge references for a requirement or question.

Usage: python3 find.py "متن نیازمندی یا سؤال" [--top 8] [--only kb|ref] [--json]
Searches every references/**/*.md paragraph (including the full official help
center in references/kb/) and the CSVs (capabilities, verified RFI answers).
Ranking: BM25 over light-stemmed Persian tokens + synonym expansion + article
title boost. Prints hits with source file and article title so answers can cite.
"""
import csv, glob, math, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "..", "references")
STOP = set("""و در به از که با را این برای یا تا می شود است های ها هر بر آن امکان قابلیت سامانه سیستم نرم افزار
پیام گستر پیامگستر crm شما خود نیز روی بودن استفاده یک دو کنید نمایید باید آیا چه کدام چگونه the and or of""".split())
SYN = {
    "پورتال": ["باشگاه", "پرتال"], "پرتال": ["باشگاه", "پورتال"], "portal": ["باشگاه"],
    "کارتخوان": ["pos"], "pos": ["کارتخوان"],
    "ios": ["pwa", "وب", "اپلیکیشن"], "آیفون": ["ios", "pwa"],
    "فرایند": ["فرآیند", "چرخه"], "فرآیند": ["فرایند", "چرخه"], "workflow": ["فرایند", "چرخه", "bpms"],
    "تیکت": ["درخواست"], "ticket": ["درخواست", "تیکت"],
    "لید": ["سرنخ"], "lead": ["سرنخ"], "opportunity": ["فرصت"],
    "ووکامرس": ["woocommerce"], "woocommerce": ["ووکامرس"],
    "دومرحله": ["otp", "یکبار"], "otp": ["یکبار", "کد"], "mfa": ["otp"], "2fa": ["otp"],
    "انتقال": ["خروجی", "بارگذاری"], "export": ["خروجی"], "import": ["بارگذاری", "ورود"],
    "گزارش": ["گزارشات"], "داشبورد": ["dashboard"],
    "sla": ["زمان", "مهلت"], "api": ["وب", "سرویس", "rest"], "webhook": ["وب", "هوک"],
    "ریزش": ["churn"], "یادگیری": ["ml", "ai"], "هوش": ["ai"], "مصنوعی": ["ai"],
    "چندزبانه": ["زبان"], "زبانه": ["زبان"], "kubernetes": ["k8s"], "امضا": ["امضای"],
}
PHRASES = [("دو مرحله", " otp "), ("دومرحله", " otp "), ("دو عاملی", " otp "), ("یک بار مصرف", " otp "),
           ("یکبار مصرف", " otp "), ("چند زبانه", " چندزبانه "), ("پاپ آپ", " پاپآپ ")]

def norm(s):
    s = s.replace("ي", "ی").replace("ك", "ک").replace("ۀ", "ه").replace("أ", "ا").replace("إ", "ا")
    s = s.replace("‌", "").replace("ـ", "")
    s = re.sub(r"[ً-ْ]", "", s)
    s = s.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
    s = re.sub(r"[^\w\s]", " ", s.lower())
    return s

def stem(t):
    if re.match(r"^[a-z0-9]+$", t):
        return t
    for suf, rep in (("هایی", ""), ("های", ""), ("ها", ""), ("گان", "ه"), ("ات", ""), ("ی", "")):
        if t.endswith(suf) and len(t) - len(suf) >= 3:
            return t[: -len(suf)] + rep
    return t

def toks(s):
    s = s.replace("\u200c", "")
    for a, b in PHRASES:
        s = s.replace(a, b)
    return [stem(t) for t in norm(s).split() if len(t) > 1 and t not in STOP]

def docs(only=None):
    if only != "kb":
        for path in glob.glob(os.path.join(REF, "*.csv")):
            name = os.path.basename(path)
            with open(path, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    yield name, "", " | ".join(v for v in row.values() if v)
    for path in sorted(glob.glob(os.path.join(REF, "**", "*.md"), recursive=True)):
        name = os.path.relpath(path, REF)
        if name.startswith(("capabilities-catalog", "verified-answers", "kb-map")):
            continue  # covered by CSVs / navigation only
        is_kb = name.startswith("kb" + os.sep)
        if (only == "kb" and not is_kb) or (only == "ref" and is_kb):
            continue
        article, block = "", []
        for line in open(path, encoding="utf-8"):
            if line.startswith("## "):
                if block:
                    yield name, article, " ".join(block)
                block = []
                article = line.strip("# \n")
                continue
            if line.lstrip().startswith("|") and not re.match(r"^\s*\|[\s:|-]+\|\s*$", line):
                if block:
                    yield name, article, " ".join(block)
                    block = []
                yield name, article, line.strip()   # each table row is its own unit
                continue
            if line.strip():
                block.append(line.strip())
            elif block:
                yield name, article, " ".join(block)
                block = []
        if block:
            yield name, article, " ".join(block)

_CACHE = {}

def corpus_for(only=None):
    if only in _CACHE:
        return _CACHE[only]
    corpus, df = [], collections.Counter()
    for src, art, text in docs(only):
        if len(text) < 25:
            continue
        tt = collections.Counter(toks(text))
        corpus.append((src, art, text, tt, set(toks(art))))
        df.update(tt.keys())
    n = max(len(corpus), 1)
    avg = sum(sum(c[3].values()) for c in corpus) / n
    _CACHE[only] = (corpus, df, n, avg)
    return _CACHE[only]

def search(query, top=8, only=None):
    q = toks(query)
    qx = collections.Counter(q)
    for t in list(q):
        for s in SYN.get(t, []):
            for st in toks(s):
                qx[st] += 0.5
    corpus, df, n, avg = corpus_for(only)
    out = []
    for src, art, text, tt, at in corpus:
        length = sum(tt.values())
        score = matched = total = 0.0
        for term, w in qx.items():
            f = tt.get(term, 0)
            idf = math.log(1 + (n - df.get(term, 0) + 0.5) / (df.get(term, 0) + 0.5))
            total += w * idf
            if f:
                matched += w * idf
                score += w * idf * f * 2.2 / (f + 1.2 * (0.25 + 0.75 * length / avg))
            elif term in at:
                matched += 0.5 * w * idf
            if term in at:
                score += w * 0.8 * idf
        if score <= 0:
            continue
        cover = matched / max(total, 1e-9)
        score *= min(cover, 1.0) ** 2
        if src.startswith(("kb" + os.sep + "Other-Mds", "kb" + os.sep + "Positions-Roadmap")):
            score *= 0.6
        out.append((score, src, art, text))
    out.sort(key=lambda x: -x[0])
    return out[:top]

def score(q, t):
    """Backward-compatible simple overlap score (used by older scripts)."""
    hit = set(q) & set(t)
    if not hit:
        return 0.0
    w = sum(3.0 if re.match(r"^[a-z0-9]+$", h) else 1.0 for h in hit)
    return w / (max(len(set(q)), 1) ** 0.5 * (len(set(t)) ** 0.25))

def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 8
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    hits = search(sys.argv[1], top, only)
    if "--json" in sys.argv:  # for agents / function calling
        import json
        print(json.dumps([{"score": round(s, 2), "source": src, "article": art, "text": text[:1500]}
                          for s, src, art, text in hits], ensure_ascii=False, indent=1))
        return
    for s, src, art, text in hits:
        head = f"{src} › {art}" if art else src
        print(f"[{s:.2f}] {head}\n    {text[:420]}\n")

if __name__ == "__main__":
    main()
