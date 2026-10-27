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
