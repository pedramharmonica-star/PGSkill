# قالب تأییدشده پروپوزال پیام‌گستر (۱۴۰۵/۰۸/۰۹)

این پوشه همان خروجی‌ای را می‌سازد که پدرام در دور سوم بازخورد تأیید کرد: قاب افقی ۱۹۲۰×۱۰۸۰، جلد کندوی شش‌ضلعی، صفحه راهکار، نمودار به‌جای جدول گزارش، صفحه نصب از سند رسمی، نقشه راه گرافیکی، SLA با نگاشت سطح شدت. قواعد محتوا در `../../references/proposal-structure.md` است.

## فایل‌ها
| فایل | کار |
|---|---|
| `build_proposal.py` | موتور: داده مشتری را می‌خواند و `proposal.html` را می‌سازد. فقط ظاهر و محتوای سندشده خود پیام‌گستر در آن است. |
| `example_data.py` | همه فیلدهای داده با یک مشتری خیالی («شرکت نمونه»). برای مشتری واقعی کپی کن، **بیرون از مخزن** پر کن. |
| `charts.py` | نمودارهای SVG راست‌به‌چپ: `hbars`، `funnel`، `columns`، `line`، `seg100`، `stacked`، `meter`، `legend`. پالت با `validate_palette.js` اسکیل dataviz آزموده شده است. |
| `style.css` | همه سبک‌ها (فونت یکان بخ از `../../assets/fonts`). |
| `render.js` | HTML ← PNG هر صفحه در `png/` و PDF افقی. |
| `render_a4.js` | HTML پیش‌فاکتور ← PNG و PDF A4. |
| `reference/` | تصویر صفحه‌های مرجع (از داده نمونه) و صفحه اول پیش‌فاکتور. |

## ساخت
```bash
python3 build_proposal.py /path/to/customer_data.py /path/to/out
cd /path/to/out && NODE_PATH=$(npm root -g) node <این پوشه>/render.js proposal.html PayamGostar-Proposal-<Client>.pdf
```
- مسیر دارایی‌ها خودکار `../../assets/` است؛ اگر موتور جای دیگری اجرا می‌شود، `PG_ASSETS` را بده.
- اسکرین‌شات صفحه راهکار: مسیر نسبت به فایل داده یا نسبت به `assets/` (برش‌های تارشده آماده: `assets/screenshots/crops/`). اگر مقدار `img` با `<` شروع شود، HTML (مثلاً داشبورد نمودار) داخل قاب مرورگر می‌نشیند.
- صفحه‌های اختیاری با مقدار `None` حذف می‌شوند: `KPI`، `DEMO`، `SLA`. فهرست مطالب و شماره صفحه‌ها خودکار است.
- `[[نیازمند تأیید تیم فنی]]` در متن، کادر نقطه‌چین نارنجی می‌شود.

## پیش‌فاکتور
`../../../payamgostar-contracts/scripts/build_preinvoice.py deal.json out` (نمونه: `../../../payamgostar-contracts/templates/preinvoice-example.json`)، بعد `render_a4.js preinvoice.html PreInvoice.pdf`.

## کنترل پیش از تحویل
1. همه صفحه‌ها را ببین (برگه تصاویر `png/`): بیرون‌زدگی متن، برچسب نمودار بریده، هم‌پوشانی شماره‌ها روی تصویر.
2. grep: `tbd`، `—`، `·`، «ي» و «ك» عربی.
3. داده واقعی مشتری را commit نکن.
