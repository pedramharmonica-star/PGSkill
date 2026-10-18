# payamgostar-knowledge

**دانش محصول CRM پیام‌گستر به‌شکل اسکیل، برای هر مدل و ایجنت هوش مصنوعی**
*PayamGostar CRM product knowledge as portable AI skills (Agent Skills format + model-agnostic bundle).*

> ⚠️ **محرمانه، فقط برای استفاده داخلی.** این مخزن شامل اسناد داخلی است (RFI تأییدشده، سند فنی PGX، یادداشت‌های تناقض و محدودیت). آن را خصوصی نگه دارید.

نسخه: **0.3.0** · دانش مرکز دانش تا نسخه نرم‌افزار **2.8.8.2** (برداشت ۱۴۰۵/۰۶/۱۴) · نگهدارنده: Pedram Berenji

---

## این مخزن چه کاری انجام می‌دهد؟

| کاربرد | توضیح |
|---|---|
| **پرسش و پاسخ** | آیا پیام‌گستر X را دارد؟ کدام منو؟ کدام ماژول، ویرایش یا نسخه؟ نیازمندی‌های فنی، امنیتی و نصب؟ |
| **تطبیق RFP/RFI/مناقصه** | هر ردیف نیازمندی را به زیرالزام می‌شکند و وضعیت را تعیین می‌کند: دارد، با پیکربندی، ماژول جانبی، API، پوشش جزئی، توسعه، Roadmap، ندارد یا مستند نشده. ماژول، ویرایش، حداقل نسخه، شاهد و متن پاسخ مشتری را هم می‌دهد. |
| **پایه ایجنت** | CSVهای ماشین‌خوان، ابزار جست‌وجوی BM25 فارسی با خروجی JSON، و تعریف ابزار برای Function Calling. |

## ساختار

```
payamgostar-knowledge/
├── .claude-plugin/plugin.json      ← مانیفست پلاگین Claude
├── AGENTS.md                       ← راهنمای Codex، Cursor، Copilot، Gemini CLI و …
├── skills/                         ← دو اسکیل با استاندارد باز Agent Skills (SKILL.md)
│   ├── payamgostar-knowledge/
│   │   ├── SKILL.md                ← قواعد، اولویت منابع، وضعیت‌ها، روش پاسخ
│   │   ├── references/             ← دانش: ۲۰ فایل موضوعی + kb/ (۱۰۱۲ مقاله) + kb-evidence/ + نمایه‌ها
│   │   └── scripts/                ← find.py (جست‌وجو)، search_kb.py، read_source.py، convert_kb.py
│   └── payamgostar-rfp-matcher/
│       ├── SKILL.md                ← گردش کار ۵ گامی تطبیق RFP و کنترل کیفیت
│       └── scripts/candidates.py   ← کاندیدای شاهد برای هر ردیف RFP
├── portable/                       ← نسخه مستقل از مدل (ChatGPT، Gemini، Copilot، RAG)
│   ├── SYSTEM_PROMPT.md            ← دستورالعمل کوتاه (کمتر از ۸۰۰۰ کاراکتر)
│   ├── PayamGostar-Skill-Complete.md ← اسکیل کامل در یک فایل
│   ├── knowledge/                  ← مرکز دانش در ۵ بخش + CSVها + درخت منو
│   └── agent/search_tool.json      ← تعریف ابزار جست‌وجو برای Function Calling
├── dist/                           ← فایل‌های آماده نصب: .plugin برای Claude و zip نسخه portable
└── tools/build_portable.py         ← ساخت دوباره portable/ از skills/
```

## نصب و استفاده

### ۱) Claude (اپ Claude، Claude Code، Cowork)
فایل `dist/payamgostar-knowledge-v0.3.0.plugin` را دانلود و در Claude نصب کنید، یا پوشه را به‌عنوان پلاگین اضافه کنید. اسکیل‌ها خودکار فعال می‌شوند؛ کافی است بپرسید یا فایل RFP را بدهید.

### ۲) ایجنت‌های سازگار با Agent Skills (OpenAI Codex، Gemini CLI، Cursor، GitHub Copilot، VS Code و …)
SKILL.md یک استاندارد باز است. پوشه‌های `skills/payamgostar-knowledge` و `skills/payamgostar-rfp-matcher` را در پوشه اسکیل‌های ابزار کپی کنید (مثلاً `.agents/skills/`، `.codex/skills/` یا `.github/skills/`، طبق مستندات همان ابزار). اگر ابزار فقط `AGENTS.md` را می‌خواند، کل مخزن را باز کنید.

### ۳) چت‌بات‌های بدون فایل‌سیستم (ChatGPT، Gemini Gem، Copilot Studio، DeepSeek، مدل لوکال)
از پوشه `portable/` (یا فایل فشرده `dist/payamgostar-portable-v0.3.0.zip`) استفاده کنید. راهنمای قدم‌به‌قدم هر پلتفرم در [`portable/README.md`](portable/README.md) است.

### ۴) ایجنت اختصاصی (هر LLM از طریق API)
```bash
python3 skills/payamgostar-knowledge/scripts/find.py "اتصال دوطرفه فاکتور با سپیدار" --top 5 --json
python3 skills/payamgostar-rfp-matcher/scripts/candidates.py requirements.csv candidates.json --top 6
```
System Prompt را از `portable/SYSTEM_PROMPT.md` بردارید و ابزار `portable/agent/search_tool.json` را تعریف کنید. فقط Python 3 استاندارد لازم است.

## منابع دانش و اولویت آن‌ها

| حوزه | اولویت (بالاترین ← پایین‌ترین) |
|---|---|
| سخت‌افزار و زیرساخت | سند پیش‌نیاز نصب ۱۴۰۴/۰۳/۱۵ ← PGX ← RFI |
| رفتار محصول، منو و «از کدام نسخه» | **مرکز دانش رسمی و Release Notes** ← کاتالوگ ریزقابلیت ← RFI ← FAQ ← دک‌ها |
| معماری و امنیت فرایندی | PGX (ستون Gap) ← RFI ← FAQ |
| سناریوهای ترکیبی | پاسخ تأییدشده RFI، مگر مرکز دانش نسخه جدیدتری نشان دهد |

منابع واردشده: سند پیش‌نیاز نصب، PGX_Document، RFI تکمیل‌شده خدمات پس از فروش (۲۱۱ ردیف)، کاتالوگ ۵۴۱ ریزقابلیت، ۵ سند همگام‌ساز مالی، FAQ، ۴ پروپوزال صنعتی (بیمه، شهرداری، برق، گاز)، **متن کامل مرکز دانش رسمی** ([1stco/PayamGostarDocs](https://github.com/1stco/PayamGostarDocs)، commit `e6143c66`)، و بسته technical-kb (نمایه ۴۱۴۶ منبع شامل ۲۲ وب‌سرویس).

جزئیات بیشتر در `skills/payamgostar-knowledge/references/source-map.md` است. تناقض‌های شناخته‌شده و قاعده هرکدام در `conflicts.md` آمده است.

## در انتظار
- صفحه‌های قیمت (ابری، استاندارد، پیشرفته). با این‌ها مشخص می‌شود BPMS و پیامک جزو بسته پایه‌اند یا ماژول جدا.
- ماتریس مادر حدود ۶۵۸ ریزقابلیت.
- RFPهای تأییدشده بیشتر.

## نگهداری
1. منبع تازه را طبق `references/pending-sources.md` وارد کنید.
2. به‌روزرسانی مرکز دانش: مخزن رسمی را `git pull` کنید و `scripts/convert_kb.py` را اجرا کنید. سپس `version-history.md`، `conflicts.md` و `gaps-and-limits.md` را بازبینی کنید.
3. پس از هر تغییر: `python3 tools/build_portable.py`، ساخت دوباره فایل‌های `dist/` و به‌روزرسانی [`CHANGELOG.md`](CHANGELOG.md).

## محدودیت‌ها
- تصاویر و ویدیوهای مرکز دانش متن ندارند و جزئیاتی که فقط در تصویر است تأییدشده نیست.
- متن PDFهای وب‌سرویس داخل مخزن نیست. فقط نمایه آن‌ها هست و خواندن متن کامل نیاز به شبکه دارد (`read_source.py`).
- مدل‌های دیگر ممکن است قواعد شواهد را سخت‌گیرانه رعایت نکنند. خروجی RFP را پیش از ارسال بازبینی انسانی کنید.
