#!/usr/bin/env python3
"""Build the model-agnostic (portable) edition of the PayamGostar skill.

Usage (from repo root):  python3 tools/build_portable.py
Outputs into portable/:
  PayamGostar-Skill-Complete.md   one self-contained skill file: instructions of both
                                  skills + every curated reference file (no full KB text)
  knowledge/kb-part-NN.md         full official help center, split into upload-sized parts
  knowledge/*.csv, kb-map.md      machine-readable tables + menu tree
SYSTEM_PROMPT.md is hand-written (short, <8000 chars) and is not generated.
Re-run after any change under skills/.
"""
import glob, os, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(ROOT, "skills")
REF = os.path.join(SK, "payamgostar-knowledge", "references")
OUT = os.path.join(ROOT, "portable")
KN = os.path.join(OUT, "knowledge")
PART_LIMIT = 1_200_000  # bytes per KB part (fits ChatGPT/Gemini/Copilot knowledge uploads)

ORDER = [
    "version-history.md", "company-facts.md", "modules.md", "editions-licensing-services.md",
    "technical-architecture-security.md", "installation-requirements.md", "integrations.md",
    "gaps-and-limits.md", "conflicts.md", "glossary.md", "industry-solutions.md",
    "kb-evidence/verified-capabilities.md", "kb-evidence/version-notes.md",
    "kb-evidence/api-guide.md", "kb-evidence/integration-matrix.md", "kb-evidence/rfp-policy.md",
    "kb-evidence/terminology.md", "kb-evidence/capability-map.md", "kb-evidence/coverage.md",
    "faq.md", "verified-answers-aftersales.md", "capabilities-catalog.md",
    "source-map.md", "pending-sources.md",
]

def body(path):
    s = open(path, encoding="utf-8").read()
    if s.startswith("---"):
        s = s.split("---", 2)[2]
    return s.strip()

def demote(text, by=1):
    out, fence = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and re.match(r"^#{1,5} ", line):
            line = "#" * by + line
        out.append(line)
    return "\n".join(out)

def fm(path, key):
    s = open(path, encoding="utf-8").read().split("---", 2)[1]
    m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', s, re.M)
    return m.group(1)

def complete():
    ks = os.path.join(SK, "payamgostar-knowledge", "SKILL.md")
    rs = os.path.join(SK, "payamgostar-rfp-matcher", "SKILL.md")
    ps = os.path.join(SK, "payamgostar-proposal", "SKILL.md")
    desc = fm(ks, "description") + " Also matches RFP/RFI/tender requirements row by row against PayamGostar capabilities and builds the branded customer proposal / RFP response."
    parts = [
        "---", "name: payamgostar-knowledge", f'description: "{desc}"', "---", "",
        "# اسکیل کامل دانش پیام‌گستر (نسخه مستقل از مدل)", "",
        "این فایل یک اسکیل کامل و خودبسنده است و در هر مدل یا ایجنتی (Claude، ChatGPT و GPTهای سفارشی، Gemini، Copilot، Cursor، Codex، ایجنت‌های LangChain و n8n و …) قابل استفاده است.",
        "",
        "**راهنمای خواندن این فایل:**",
        "- بخش «الف» دستورالعمل است و باید رعایت شود. بخش «ب» دانش مرجع است.",
        "- هر جا در دستورالعمل به `references/<نام فایل>` اشاره شده، همان فایل در بخش «ب» با عنوان «فایل مرجع: <نام فایل>» آمده است.",
        "- متن کامل مرکز دانش رسمی (`references/kb/`) به‌خاطر حجم، جدا در `knowledge/kb-part-*.md` است. اگر در دسترس است برای منو، تنظیمات و «از کدام نسخه» به آن رجوع کن؛ اگر نیست، بگو جزئیات منو از مرکز دانش تأیید شود.",
        "- دستورهای `python3 scripts/...` فقط وقتی کاربرد دارند که محیط اجرای کد و پوشه کامل اسکیل در دسترس باشد؛ در غیر این صورت در همین فایل جست‌وجو کن.",
        "",
        "# الف) دستورالعمل", "",
        "## الف-۱) دانش و پرسش و پاسخ", "", demote(body(ks), 2), "",
        "## الف-۲) تطبیق RFP با قابلیت‌ها", "", demote(body(rs), 2), "",
        "## الف-۳) ساخت پروپوزال و پاسخ RFP طراحی‌شده", "",
        "> بخش‌های فنی این قسمت (HTML، Playwright، فونت و لوگو) فقط در محیطی با اجرای کد کاربرد دارند. در چت‌بات بدون اجرای کد، از قواعد محتوا، استوری‌بورد و نگاشت وضعیت‌ها برای نوشتن متن پروپوزال استفاده کن.", "",
        demote(body(ps), 2), "",
        "# ب) دانش مرجع", "",
    ]
    for name in ORDER:
        p = os.path.join(REF, name)
        if not os.path.exists(p):
            continue
        parts += [f"## فایل مرجع: references/{name}", "", demote(body(p), 2), ""]
    open(os.path.join(OUT, "PayamGostar-Skill-Complete.md"), "w", encoding="utf-8").write("\n".join(parts) + "\n")

def kb_parts():
    for old in glob.glob(os.path.join(KN, "kb-part-*.md")):
        os.remove(old)
    files = sorted(glob.glob(os.path.join(REF, "kb", "*.md")),
                   key=lambda p: (os.path.basename(p).startswith("releasenote"), os.path.basename(p)))
    parts, cur, size = [], [], 0
    for f in files:
        b = os.path.getsize(f)
        if cur and size + b > PART_LIMIT:
            parts.append(cur); cur, size = [], 0
        cur.append(f); size += b
    if cur:
        parts.append(cur)
    for i, group in enumerate(parts, 1):
        names = ", ".join(os.path.basename(g)[:-3] for g in group)
        txt = [f"# مرکز دانش رسمی پیام‌گستر — بخش {i} از {len(parts)}", "",
               f"بخش‌های این فایل: {names}", ""]
        for g in group:
            txt += [demote(open(g, encoding="utf-8").read().strip(), 1), ""]
        open(os.path.join(KN, f"kb-part-{i:02d}.md"), "w", encoding="utf-8").write("\n".join(txt) + "\n")
    return len(parts)

def main():
    os.makedirs(KN, exist_ok=True)
    complete()
    n = kb_parts()
    for f in ("capabilities.csv", "verified-answers-aftersales.csv", "kb-map.md"):
        shutil.copy(os.path.join(REF, f), KN)
    print(f"portable built: complete file + {n} KB parts")

if __name__ == "__main__":
    main()
