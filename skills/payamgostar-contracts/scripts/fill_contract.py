#!/usr/bin/env python3
"""Fill a PayamGostar contract template (.docx) with deal data.

Usage:
  python3 fill_contract.py <template> <deal.json> <out.docx>
  python3 fill_contract.py --calc <deal.json>          # only print the money lines

<template> is one of: sales, install, sla, nda  (or a path to a .docx under templates/)

deal.json (all money in RIAL, integers):
{
  "buyer_company": "...", "buyer_reps": "خانم ... به‌عنوان مدیرعامل و ...",
  "buyer_rep_name": "...", "buyer_rep_title": "آقای ...", "buyer_rep_role": "مدیرعامل",
  "buyer_reg_no": "...", "buyer_national_id": "...", "buyer_economic_code": "...",
  "buyer_address": "...", "buyer_email": "...",
  "proforma_no": "1405/DS/....", "start_date": "1405/../..", "date": "1405/../..",
  "main_contract_no": "...", "main_contract_date": "...",
  "seller_rep_national_code": "...",              # only for NDA; ask the user, never stored in the repo
  "software_amount": 0,                           # final software amount without VAT (after any APPROVED discount)
  "install_amount": null,                         # default = 10% of software_amount
  "project_amount": 0,                            # optional personalisation project (install contract)
  "prepay_percent": 50, "vat_percent": 10   # prepay is REQUIRED: negotiated per deal, usually >= 50
}
Only deal data is replaced. The contract wording is never changed.
"""
import json, os, re, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(os.path.dirname(HERE), "templates")
NAMES = {"sales": "sales-contract.docx", "install": "install-training-support-contract.docx",
         "sla": "sla-annex.docx", "nda": "nda.docx"}
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

# ---------- Persian number to words ----------
ONES = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
TEENS = ["ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]
TENS = ["", "", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
HUNDREDS = ["", "صد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]
SCALES = ["", "هزار", "میلیون", "میلیارد", "هزار میلیارد"]

def _three(n):
    parts = []
    h, r = divmod(n, 100)
    if h: parts.append(HUNDREDS[h])
    if 10 <= r < 20: parts.append(TEENS[r - 10])
    else:
        t, o = divmod(r, 10)
        if t: parts.append(TENS[t])
        if o: parts.append(ONES[o])
    return " و ".join(parts)

def words(n):
    n = int(n)
    if n == 0: return "صفر"
    groups, i = [], 0
    while n:
        n, g = divmod(n, 1000)
        if g: groups.append(_three(g) + ((" " + SCALES[i]) if SCALES[i] else ""))
        i += 1
    return " و ".join(reversed(groups))

def money(n):
    return f"{int(n):,}"

# ---------- calculations ----------
def calc(d):
    vat = d.get("vat_percent", 10) / 100
    if d.get("prepay_percent") is None:
        sys.exit("prepay_percent is required (negotiated per deal; usually not below 50). Ask the user.")
    pp = d["prepay_percent"] / 100
    if d["prepay_percent"] < 50:
        print("WARNING: prepayment below 50% is unusual; confirm with the sales manager.", file=sys.stderr)
    S = int(d.get("software_amount") or 0)
    out = {}
    out["{{درصد پیش‌پرداخت}}"] = str(d["prepay_percent"])
    out["{{درصد باقی‌مانده}}"] = str(100 - d["prepay_percent"])
    if S:
        pre = round(S * pp)
        rest_vat = S - pre + round(S * vat)
        out.update({
            "{{مبلغ نرم‌افزار بدون ارزش افزوده (ریال)}}": money(S),
            "{{مبلغ نرم‌افزار به حروف}}": words(S),
            "{{پیش‌پرداخت (ریال)}}": money(pre),
            "{{باقی‌مانده به‌علاوه ارزش افزوده کل (ریال)}}": money(rest_vat),
            "{{باقی‌مانده به‌علاوه ارزش افزوده به حروف}}": words(rest_vat),
        })
        out["_sales_prepay_words"] = words(pre)
    I = d.get("install_amount")
    I = int(I) if I is not None else round(S * 0.10)
    P = int(d.get("project_amount") or 0)
    T = I + P
    if T:
        pre2 = round(T * pp); rest2 = T - pre2; vat2 = round(T * vat)
        out.update({
            "{{مبلغ خدمات نصب و آموزش = ۱۰٪ مبلغ نرم‌افزار (ریال)}}": money(I),
            "{{مبلغ خدمات نصب و آموزش به حروف}}": words(I),
            "{{مبلغ پروژه شخصی‌سازی (ریال)}}": money(P),
            "{{مبلغ پروژه شخصی‌سازی به حروف}}": words(P),
            "{{پیش‌پرداخت کل قرارداد (ریال)}}": money(pre2),
            "{{باقی‌مانده (ریال)}}": money(rest2),
            "{{باقی‌مانده به حروف}}": words(rest2),
            "{{مالیات بر ارزش افزوده کل قرارداد (ریال)}}": money(vat2),
            "{{ارزش افزوده به حروف}}": words(vat2),
        })
        out["_install_prepay_words"] = words(pre2)
    return out

TEXT = {
    "buyer_company": ["{{نام شرکت خریدار}}", "{{نام شرکت کارفرما}}"],
    "buyer_reps": ["{{عنوان، نام و سمت نماینده یا نمایندگان خریدار}}"],
    "buyer_rep_name": ["{{نام نماینده خریدار}}", "{{نام نماینده کارفرما}}"],
    "buyer_rep_title": ["{{عنوان و نام نماینده خریدار}}", "{{عنوان و نام نماینده کارفرما}}"],
    "buyer_rep_role": ["{{سمت نماینده خریدار}}", "{{سمت نماینده کارفرما}}"],
    "buyer_reg_no": ["{{شماره ثبت خریدار}}", "{{شماره ثبت کارفرما}}"],
    "buyer_national_id": ["{{شناسه ملی خریدار}}", "{{شناسه ملی کارفرما}}"],
    "buyer_economic_code": ["{{کد اقتصادی خریدار}}", "{{کد اقتصادی کارفرما}}"],
    "buyer_address": ["{{نشانی خریدار}}", "{{نشانی کارفرما}}"],
    "buyer_email": ["{{ایمیل رسمی خریدار}}"],
    "proforma_no": ["{{شماره پیش‌فاکتور}}"],
    "start_date": ["{{تاریخ شروع قرارداد}}"],
    "date": ["{{تاریخ}}"],
    "main_contract_no": ["{{شماره قرارداد اصلی}}"],
    "main_contract_date": ["{{تاریخ قرارداد اصلی}}"],
    "seller_rep_national_code": ["{{کد ملی نماینده مجری}}"],
}
SELLER = {"{{شناسه ملی فروشنده}}": "14009714841"}

def mapping(d, which):
    m = dict(SELLER)
    for k, phs in TEXT.items():
        if d.get(k):
            for ph in phs: m[ph] = str(d[k])
    c = calc(d)
    pw = c.pop("_sales_prepay_words", None); iw = c.pop("_install_prepay_words", None)
    m.update(c)
    # the same placeholder name is used for the prepayment words in both contracts
    m["{{پیش‌پرداخت به حروف}}"] = (iw if which == "install" else pw) or "{{پیش‌پرداخت به حروف}}"
    if m["{{پیش‌پرداخت به حروف}}"].startswith("{{"): del m["{{پیش‌پرداخت به حروف}}"]
    return m

def fill(tpl, d, out):
    from lxml import etree
    which = next((k for k, v in NAMES.items() if os.path.basename(tpl) == v), "")
    m = mapping(d, which)
    zin = zipfile.ZipFile(tpl); zout = zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED)
    left = set()
    for it in zin.infolist():
        data = zin.read(it.filename)
        if it.filename.startswith("word/") and it.filename.endswith(".xml") and b"<w:" in data:
            root = etree.fromstring(data)
            for p in root.iter("{%s}p" % W):
                ts = [t for t in p.iter("{%s}t" % W) if _owner(t) is p]
                if not ts: continue
                txt = "".join(t.text or "" for t in ts)
                if "{{" not in txt: continue
                new = txt
                for k, v in m.items(): new = new.replace(k, v)
                left.update(re.findall(r"{{[^}]*}}", new))
                if new != txt:
                    ts[0].text = new
                    ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
                    for t in ts[1:]: t.text = ""
            data = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
        zout.writestr(it, data)
    zout.close()
    return sorted(left)

def _owner(t):
    a = t.getparent()
    while a is not None and a.tag != "{%s}p" % W: a = a.getparent()
    return a

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    if a[0] == "--calc":
        d = json.load(open(a[1], encoding="utf-8"))
        for k, v in calc(d).items():
            if not k.startswith("_"): print(k, "=", v)
        sys.exit(0)
    tpl = a[0] if a[0].endswith(".docx") else os.path.join(TPL, NAMES[a[0]])
    d = json.load(open(a[1], encoding="utf-8"))
    left = fill(tpl, d, a[2])
    print("written:", a[2])
    if left:
        print("UNFILLED placeholders (ask the user, or delete the clause if not applicable):")
        for x in left: print("  ", x)
