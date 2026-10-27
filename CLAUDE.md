# CLAUDE.md: PGSkill

مخزن اسکیل‌های پیام‌گستر (دانش محصول، تطبیق RFP، ساخت پروپوزال). صاحب: پدرام برنجی، عملیات فروش پیام‌گستر.

**پیش از هر کاری `handoff/HANDOFF.md` را کامل بخوان.** هدف، تصمیم‌ها، اولویت منابع، یافته‌ها و کارهای باز آنجاست.

## قواعد کار در این مخزن
- با پدرام **فارسی** صحبت کن. نسخه قابل‌تست را مرحله‌به‌مرحله تحویل بده.
- قواعد غیرقابل‌مذاکره دانش (ساختن ممنوع، «مستند نشده» ≠ «ندارد»، قید ماژول، نسخه و ویرایش، اولویت منابع، محرمانگی) در `skills/payamgostar-knowledge/SKILL.md` است. همیشه رعایتشان کن.
- مخزن خصوصی و محرمانه است. رمز، Credential یا اطلاعات شخصی مشتری را commit نکن.
- فایل خام تازه ← `incoming/`. مقصد هر نوع فایل در `incoming/README.md` آمده است.
- پس از هر تغییر در `skills/`:
  1. `python3 tools/build_portable.py`
  2. بسته‌های `dist/` را دوباره بساز (zip پلاگین: `.claude-plugin`، `skills`، `README.md`، `AGENTS.md`، `CHANGELOG.md`؛ zip پوشه `portable`).
  3. نسخه را در `.claude-plugin/plugin.json` و `CHANGELOG.md` بالا ببر.
- جست‌وجوی دانش: `python3 skills/payamgostar-knowledge/scripts/find.py "<سؤال>" --top 8`
- سایت payamgostar.com برای WebFetch مسدود است (robots). برای خواندنش از مرورگر (Claude in Chrome) استفاده کن و فقط بخوان. فرم پر نکن و چیزی ارسال نکن.

## منبع مرکز دانش: فقط‌خواندنی
- مخزن `https://github.com/1stco/PayamGostarDocs` را مدیر آموزش شرکت ساخته است. **به هیچ عنوان در آن چیزی ننویس:** نه commit، نه push، نه issue یا PR. فقط clone (با push غیرفعال: `git remote set-url --push origin DISABLED`) و استخراج.
- استخراج: `python3 tools/import_kb_images.py <clone> <commit>` (تصاویر ← `kb-assets/`) و `python3 skills/payamgostar-knowledge/scripts/convert_kb.py <clone> skills/payamgostar-knowledge/references/kb <commit>` (متن ← `references/kb/`).

## نسخه دمو
- نشانی، نام کاربری و رمز دمو را **هرگز** در مخزن یا حافظه ذخیره نکن. ورود را خود پدرام انجام می‌دهد؛ Claude فقط بعد از ورود او، فقط‌خواندنی می‌گردد (نه ذخیره، نه حذف، نه تغییر تنظیمات).
- مشاهده‌ها در `skills/payamgostar-knowledge/references/demo-walkthrough.md`، بدون داده‌های نمونه (نام اشخاص و شرکت‌ها، مبلغ‌ها).
