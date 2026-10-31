# -*- coding: utf-8 -*-
"""Pre-invoice (پیش‌فاکتور) PDF builder, standard notes of references/pre-invoice.md.

Usage: python3 build_preinvoice.py deal.json out_dir   (then render with templates/proposal/render_a4.js)
deal.json (prices in TOMAN, from pricing.md; the script writes RIAL = toman x 10):
{ "buyer": "...", "scenario_note": "ویرایش استاندارد، نصب درون‌سازمانی",
  "scenarios": [["الف", 10], ["ب", 25]],                     # label, named users (one pre-invoice each)
  "modules": [["کنسول مدیریت ارتباط با مشتری تحت وب – ۵ کاربر", 61200000], ["کاربر اضافه (ویرایش تحت وب)", 7900000], ...],
  "pending": [["کاربر باشگاه نمایندگان (هر نفر)", 4100000, "تعداد"]],   # unknown quantity: shown, kept out of the total
  "services": [["بسته استقرار اولیه ۳۰ ساعته", 64000000, 3]],           # no 10% column
  "hours_total": 105, "hours_extra": 90, "support": "نقره‌ای" }
Unknown deal data (number, dates, prepayment, buyer details) stays as a dashed placeholder: ask the user.
No discount unless the sales manager approved an amount. Never commit a filled deal file.
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..')) + '/'
DEAL = json.load(open(sys.argv[1], encoding='utf-8'))
sys.path.insert(0, HERE)
from fill_contract import words
ASSET = REPO + 'payamgostar-proposal/assets/'
FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
def fa(x): return str(x).translate(FA)
def m(n): return fa(f'{int(n):,}'.replace(',', '٬'))
TBD = lambda t: f'<span class="tbd">{t}</span>'

MODS = [tuple(x) for x in DEAL['modules']]
PENDING = [tuple(x) for x in DEAL.get('pending', [])]
SERVICES = [tuple(x) for x in DEAL.get('services', [])]
SCEN = [tuple(x) for x in DEAL['scenarios']]
HOURS, HX = DEAL.get('hours_total', 15), DEAL.get('hours_extra', 0)

def build(letter, users):
    rows, n = [], 0
    soft = dep = 0
    for name, toman in MODS:
        q = 1
        if name.startswith('کاربر اضافه'):
            q = users - 5
            if q <= 0: continue
        unit = toman * 10
        price = unit * q; d = price // 10
        soft += price; dep += d; n += 1
        rows.append(f'<tr><td>{fa(n)}</td><td class="nm">{name}</td><td>{fa(q)}</td><td>{m(unit)}</td><td>{m(d)}</td><td>{m(price + d)}</td></tr>')
    for name, toman, what in PENDING:
        n += 1
        rows.append(f'<tr class="pend"><td>{fa(n)}</td><td class="nm">{name}</td><td>{TBD(what)}</td><td>{m(toman * 10)}</td><td colspan="2">پس از اعلام تعداد به جمع اضافه می‌شود</td></tr>')
    extra = 0
    for name, toman, q in SERVICES:
        n += 1; extra += toman * 10 * q
        rows.append(f'<tr class="svc"><td>{fa(n)}</td><td class="nm">{name}</td><td>{fa(q)}</td><td>{m(toman * 10)}</td><td>—</td><td>{m(toman * 10 * q)}</td></tr>')
    total = soft + dep + extra
    notes = [
        f'نرخ مندرج در پیش فاکتور شماره {TBD("شماره")} تا تاریخ {TBD("تاریخ اعتبار")} معتبر می باشد.',
        f'مبلغ نهایی پیش فاکتور بدون احتساب مالیات بر ارزش افزوده به صورت زیر میباشد: الف – هزینه حق بهره برداری لایسنس نرم افزار معادل {m(soft)} ریال؛ ب- هزینه خدمات استقرار نرم افزار ۱۰٪ قیمت نرم افزار معادل {m(dep)} ریال' + (f'، و {fa(HX)} نفرساعت استقرار تکمیلی معادل {m(extra)} ریال.' if extra else '.'),
        'به مبلغ فوق ۱۰٪ مالیات بر ارزش افزوده اضافه خواهد گردید که بر عهده خریدار می‌باشد.',
        f'جهت تأیید سفارش: پرداخت {TBD("درصد")}٪ مبلغ نهایی پیش‌فاکتور الزامی است؛ الباقی طی چک (با ثبت صیادی) به تاریخ‌های {TBD("تاریخ چک‌ها")} تسویه می‌گردد. ارائه اصل چک با ثبت صیادی در زمان تحویل بسته نرم‌افزاری الزامی است.',
        'هزینه‌های بند الف مربوط به فروش حق بهره‌برداری نرم‌افزار (فروش کالا) است و هیچ‌گونه کسور قانونی به آن تعلق نمی‌گیرد.',
        'طبق بند ۴ بخشنامه ۱۴/۳ درآمد تأمین اجتماعی (قراردادهای ICT) هیچ‌گونه حق بیمه به صورت‌حساب تعلق نمی‌گیرد؛ فروشنده در صورت درخواست مفاصاحساب بیمه ارائه می‌کند.',
        f'آموزش کاربران به‌صورت وبینار عمومی رایگان و نامحدود تا یک سال از تحویل بسته است. استقرار در مجموع {fa(HOURS)} نفرساعت' + (f' (۱۵ نفرساعت پایه و {fa(HX)} نفرساعت تکمیلی)' if HX else '') + ' تعهد می‌شود با مهلت استفاده تا ۳ ماه و ۱۵ روز از تحویل بسته؛ نفرساعت اضافه هزینه جدا دارد.',
        f'پشتیبانی سال اول در قالب بسته {DEAL.get("support", "نقره‌ای")} ۱۲ ماهه است.',
        'لینک پرداخت را از کارشناس فروش دریافت کنید.',
        'تأمین سخت‌افزار ماژول‌ها بر عهده مشتری است.',
        'تهیه سرور مطابق پیش‌نیاز نصب بر عهده خریدار است.',
        'خریدار دسترسی Remote به سرور را برای کارشناسان پشتیبانی فراهم می‌کند.',
        'هزینه اعزام کارشناس به خارج از تهران بر عهده مشتری است.',
        'واریز پیش‌پرداخت به منزله قبول موارد فوق و قوانین و مقررات پیام‌گستر (termsofuse) است.',
        'خریدار مدیر پروژه و نماینده تام‌الاختیار خود را معرفی می‌کند؛ مکاتبات ایمیل‌های رسمی دامنه payamgostar.com و ایمیل اعلامی خریدار حکم مکاتبه کتبی دارد.']
    nh = ''.join(f'<li>{x}</li>' for x in notes)
    head = f'''<div class="hd"><img src="file://{ASSET}logo/payamgostar-light-horizontal-631.png"><div class="tt"><h1>پیش فاکتور فروش کالا و ارائه خدمات</h1>
<div class="meta"><span>تاریخ: {TBD("تاریخ")}</span><span>شماره: {TBD("شماره پیش‌فاکتور")}</span><span>پیوست: ندارد</span></div></div></div>
<div class="parties"><div><h3>فروشنده</h3><p>شرکت راهکار هوشمند پیام‌گستر</p><p>تهران، شهرک غرب، بلوار دادمان، خیابان بهارستان، پلاک ۷</p><p>تلفن <bdi dir="ltr">۰۲۱-۴۹۷۱۴</bdi>، نمابر <bdi dir="ltr">۰۲۱-۴۴۴۲۰۰۷۵</bdi></p><p>کارشناس فروش: {TBD("نام کارشناس")}</p></div>
<div><h3>خریدار</h3><p>{DEAL['buyer']}</p><p>نشانی: {TBD("نشانی خریدار")}</p><p>تلفن و نمابر: {TBD("تلفن")}</p><p>نماینده خریدار: {TBD("نام و سمت")}</p></div></div>
<div class="scen">سناریوی {letter}: {fa(users)} کاربر نام‌دار، {DEAL.get('scenario_note', '')}</div>'''
    table = f'''<table class="it"><thead><tr><th>ردیف</th><th>محصول</th><th>تعداد</th><th>قیمت واحد (ریال)</th><th>استقرار (ریال)</th><th>قیمت کل (ریال)</th></tr></thead><tbody>{"".join(rows)}</tbody>
<tfoot><tr><td colspan="3">مجموع</td><td>{m(soft + extra)}</td><td>{m(dep)}</td><td>{m(total)}</td></tr>
<tr><td colspan="5">تخفیف</td><td>—</td></tr>
<tr class="fin"><td colspan="5">مبلغ نهایی (بدون احتساب مالیات بر ارزش افزوده)</td><td>{m(total)}</td></tr></tfoot></table>
<div class="words">مبلغ نهایی به حروف: {words(total)} ریال</div>'''
    sign = '<div class="sign"><div>مدیر فروش<br><small>امضا و مهر</small></div><div>تأیید خریدار یا نماینده<br><small>مهر و امضا</small></div></div>'
    foot = '<div class="pf">تهران، شهرک غرب، بلوار دادمان، خیابان بهارستان، پلاک ۷، ساختمان تجارت الکترونیک اول. تلفن <bdi dir="ltr">(+9821) 49714</bdi>، <bdi dir="ltr">info@payamgostar.com</bdi></div>'
    p1 = f'<section class="a4">{head}{table}{sign}{foot}</section>'
    p2 = f'<section class="a4"><h2>توضیحات</h2><ol class="nt">{nh}</ol>{sign}{foot}</section>'
    return p1 + p2, total, soft, dep, extra

CSS = f'''@font-face{{font-family:YB;src:url(file://{ASSET}fonts/YekanBakhFaNum-0400-Regular.ttf);font-weight:400}}
@font-face{{font-family:YB;src:url(file://{ASSET}fonts/YekanBakhFaNum-0700-Bold.ttf);font-weight:700}}
@font-face{{font-family:YB;src:url(file://{ASSET}fonts/YekanBakhFaNum-0900-Heavy.ttf);font-weight:900}}
@page{{size:A4;margin:0}}*{{box-sizing:border-box;margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:YB;color:#2B2F36;background:#fff}}
.a4{{width:210mm;height:297mm;padding:12mm 12mm 18mm;position:relative;break-after:page;overflow:hidden}}
.hd{{display:flex;justify-content:space-between;align-items:center;border-bottom:3px solid #F26122;padding-bottom:8px}}
.hd img{{height:44px}}
.tt h1{{font-size:19px;font-weight:900;color:#F26122;text-align:left}}
.meta{{display:flex;gap:14px;font-size:11.5px;color:#4A505A;margin-top:4px;justify-content:flex-end}}
.parties{{display:flex;gap:12px;margin:10px 0}}
.parties div{{flex:1;border:1px solid #E8E9EC;border-radius:8px;padding:8px 10px}}
.parties h3{{font-size:12.5px;color:#B8460F;margin-bottom:3px}}
.parties p{{font-size:11px;line-height:1.7}}
.scen{{background:#FFF3EC;border-radius:6px;padding:6px 10px;font-size:12px;font-weight:700;color:#B8460F;margin-bottom:8px}}
table.it{{width:100%;border-collapse:collapse;font-size:10.5px}}
.it th{{background:#F26122;color:#fff;padding:6px 5px;font-weight:700}}
.it td{{border-bottom:1px solid #E8E9EC;padding:5px 5px;text-align:center;white-space:nowrap}}
.it td.nm{{text-align:right;white-space:normal}}
.it tr.pend td{{background:#FAFAFB;color:#6E747F}}
.it tr.svc td{{background:#FFF8F3}}
.it tfoot td{{font-weight:700;background:#F4F5F7;border-bottom:1px solid #fff}}
.it tfoot tr.fin td{{background:#2B2F36;color:#fff;font-size:11.5px}}
.it tfoot td:first-child{{text-align:right}}
.words{{font-size:11px;margin-top:6px;color:#4A505A}}
h2{{font-size:16px;color:#F26122;margin:4px 0 8px}}
.nt{{padding-right:18px;font-size:11.2px;line-height:1.85}}
.nt li{{margin-bottom:3px}}
.tbd{{color:#B8460F;background:#FFF3EC;border:1px dashed #F26122;border-radius:4px;padding:0 4px;font-weight:700;white-space:nowrap}}
.sign{{position:absolute;bottom:28mm;right:12mm;left:12mm;display:flex;justify-content:space-between;font-size:11.5px;font-weight:700;text-align:center}}
.sign div{{width:45%;border-top:1px solid #C9CCD2;padding-top:6px}}
.sign small{{font-weight:400;color:#6E747F}}
.pf{{position:absolute;bottom:8mm;right:12mm;left:12mm;font-size:9.5px;color:#6E747F;border-top:1px solid #E8E9EC;padding-top:5px;text-align:center}}
'''
body, summary = '', []
for L, u in SCEN:
    h, tot, soft, dep, extra = build(L, u)
    body += h; summary.append((L, u, soft, dep, extra, tot))
doc = f'<!DOCTYPE html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
os.makedirs(sys.argv[2], exist_ok=True)
out = os.path.join(sys.argv[2], 'preinvoice.html')
open(out, 'w', encoding='utf-8').write(doc)
for s in summary: print(s)
