# نسخه مستقل از مدل (Portable)

این پوشه برای استفاده از دانش پیام‌گستر **خارج از Claude** ساخته شده است: ChatGPT و GPTهای سفارشی، Gemini و Gem، Microsoft Copilot، DeepSeek، مدل‌های لوکال، و ایجنت‌سازهایی مثل LangChain، n8n، Dify یا Flowise.

| فایل | کاربرد |
|---|---|
| `SYSTEM_PROMPT.md` | دستورالعمل کوتاه (حدود ۵۰۰۰ کاراکتر). در کادر Instructions یا System Prompt بگذارید. |
| `PayamGostar-Skill-Complete.md` | **اسکیل کامل در یک فایل**: دستورالعمل هر پنج اسکیل (دانش، تطبیق RFP، پروپوزال سه‌مدلی، قرارداد و پیش‌فاکتور، ساخت فرم و فرایند) و همه فایل‌های مرجع (حدود ۹۰۰ کیلوبایت). به‌عنوان Knowledge آپلود کنید یا در ایجنت‌های فایل‌محور به‌جای SKILL.md بگذارید. |
| `knowledge/kb-part-01..05.md` | متن کامل مرکز دانش رسمی (۱۰۱۲ مقاله، تا نسخه 2.8.8.2)، در ۵ بخش حدود ۱ مگابایتی |
| `knowledge/capabilities.csv` | ۵۴۱ ریزقابلیت کددار |
| `knowledge/verified-answers-aftersales.csv` | ۲۱۱ پاسخ تأییدشده RFI |
| `knowledge/kb-map.md` | درخت منوها و مقاله‌ها |
| `agent/search_tool.json` | تعریف ابزار جست‌وجو برای Function Calling |

## راه‌اندازی در هر پلتفرم

**ChatGPT (GPT سفارشی یا Project)**
1. Instructions: متن `SYSTEM_PROMPT.md`.
2. Knowledge: `PayamGostar-Skill-Complete.md` و هر ۵ فایل `kb-part`، به‌علاوه دو CSV و `kb-map.md`. مجموعاً ۹ فایل است و زیر سقف ۲۰ فایل.
3. اگر Code Interpreter روشن باشد، CSVها برای شمارش و فیلتر هم قابل استفاده‌اند.

**Gemini (Gem) یا NotebookLM**
- Instructions: `SYSTEM_PROMPT.md`. فایل‌ها: `PayamGostar-Skill-Complete.md`، ۵ فایل `kb-part`، دو CSV و `kb-map.md` (۹ فایل، زیر سقف ۱۰ فایل Gem). بسته آماده: `dist/payamgostar-gemini-v*.zip` با راهنمای قدم‌به‌قدم.
- Gemini CLI: پوشه مخزن را باز کنید؛ `GEMINI.md` در ریشه، `AGENTS.md` و اسکیل‌ها را بارگذاری می‌کند.

**Microsoft Copilot Studio، Dify، Flowise، n8n و هر RAG دیگر**
- System Prompt: `SYSTEM_PROMPT.md`. منبع دانش: همه فایل‌های `knowledge/` به‌همراه `PayamGostar-Skill-Complete.md`.
- پیشنهاد chunking: بر اساس سرتیترهای `##`. هر مقاله مرکز دانش با `##` شروع می‌شود و مسیر و نسخه سند در خط بعدش آمده است.

**ایجنت‌های کدنویسی (Codex، Gemini CLI، Cursor، GitHub Copilot و …)**
- لازم نیست از این پوشه استفاده کنید. پوشه `skills/` در ریشه مخزن با استاندارد باز **Agent Skills** سازگار است و `AGENTS.md` راهنمای این ابزارهاست.

**ایجنت اختصاصی خودتان (API هر مدلی)**
- `SYSTEM_PROMPT.md` را system message بگذارید و ابزار `agent/search_tool.json` را تعریف کنید.
- پیاده‌سازی ابزار: `python3 skills/payamgostar-knowledge/scripts/find.py "<query>" --json`، یا در پایتون `find.search(query, top, only)`. فقط کتابخانه استاندارد پایتون لازم است.

## نکته‌ها
- محتوا محرمانه و داخلی است. فایل‌ها را فقط در فضای سازمانی یا خصوصی آپلود کنید، نه در GPT عمومی.
- کیفیت نهایی به مدل بستگی دارد. قواعد «بدون شاهد ادعا نکن» در همه فایل‌ها تکرار شده، ولی خروجی RFP را پیش از ارسال بازبینی کنید.
- پس از هر تغییر در `skills/` این دستور را اجرا کنید: `python3 tools/build_portable.py`. فایل `SYSTEM_PROMPT.md` دستی است و جداگانه به‌روز می‌شود.
