# معماری فنی، امنیت، یکپارچه‌سازی API و عملیات

منبع اصلی: **PGX_Document.xlsx** (سند ارزیابی فنی و معماری؛ شیت‌های ۰۱ تا ۰۹، با فهرست کشویی وضعیت «دارد، ندارد، قابل توسعه، Third Party، Roadmap، نامشخص»). منابع دیگر: RFI (شیت فنی، ردیف ۱۴۰ تا ۱۷۹)، دک‌ها (اسلاید معماری)، FAQ فنی، سند پیش‌نیاز نصب (۱۴۰۴/۰۳/۱۵).
اولویت در موضوعات فنی: **خودارزیابی (`self-assessment.md`) برای معماری و امکانات فنی**، سند نصب برای سخت‌افزار و سیستم‌عامل ← PGX ← RFI ← دک‌ها ← FAQ (تأیید ویزارد ۱۴۰۵/۰۸/۰۵). تناقض‌ها در `conflicts.md`.

> ⚠ **هر جا این فایل از PGX «میکروسرویس (۵۳ سرویس)»، «‎.NET 8»، «React»، «IdentityServer» یا «Message Broker» نقل کرده، منسوخ است.** معماری معتبر طبق خودارزیابی: ASP.NET WebForm در لایه‌های Presentation، Application و Business؛ SQL Server 2022؛ REST (Swagger)، SOAP و Webhook؛ دو Windows Service نیتیو، یک سرویس IIS و کش Redis به‌علاوه In-Memory؛ بدون کانتینر، Docker، Kubernetes، Message Broker، API Gateway و ESB؛ IAM با Active Directory؛ جست‌وجوی Full-Text SQL Server (C35).

> ستون Gap/Evidence خود PGX صادقانه نوشته که کدام ادعاها شاهد مستند ندارند. در RFP رسمی، برای هر ادعای فنی، شاهد را هم ذکر کن یا «قابل ارائه پس از جلسه فنی» بنویس.

## پشته فناوری
| لایه | مقدار (PGX) | منابع دیگر |
|---|---|---|
| معماری | **Microservice — ۵۳ میکروسرویس**؛ در On-Premise برای سادگی نگهداری در قالب **۵ Windows Service** مستقر می‌شوند | RFI: «ماژولار چندلایه (Multi-Tier) روی هسته مرکزی»؛ FAQ و دک: SOA و Service Oriented |
| Presentation | React JS، React Native، ASP.NET Core MVC | دک: ASP.NET، Ajax، MVC، TypeScript |
| Application و Business | **.NET 8** | دک: .NET Framework 4.8.1، SeptaNSF 6، .NET 5؛ RFI: .NET Framework 4.8 و C#؛ FAQ: .NET Core و C# |
| Data | **SQL Server 2022** | سند نصب: SQL Server 2022 (Enterprise یا Enterprise-Core)؛ دک: 2022 or higher؛ RFI: 2016/2019/2022 Standard یا Enterprise |
| سیستم‌عامل | — | سند نصب: Windows Server **2022 یا 2025** (Standard یا Datacenter)؛ نصب روی ویندوز کلاینت ممکن نیست. دک: WS 2022+؛ RFI: WS 2019/2022 |
| وب‌سرور | IIS 10 | |
| Integration | REST API، SOAP API (WCF)، Webhook | |
| Message Broker | RabbitMQ (بخشی از ارتباطات Async؛ معماری کاملاً Event-Driven **نیست**) | |
| API Gateway | مرکزی مبتنی بر ASP.NET Core 8 (Routing، احراز هویت، کنترل دسترسی، لاگ، سیاست‌های مشترک) | |
| Cache | Redis و In-Memory | |
| Search | SQL Server Full-Text Search | |
| Workflow/Rules/BPM Engine | داخلی پیام‌گستر | BPMN 2.0 |
| IAM | IdentityServer (دک: IdentityServer4)؛ OAuth 2.0 و OpenID Connect؛ JWT | الگوها: Service Result Pattern، Multi Task، Caching، **CQRS** |
| IDE | Visual Studio .NET 2025 (دک) | |
| کانتینر | Cloud: همه میکروسرویس‌ها Containerized روی **Docker** با ارکستراسیون **Docker Swarm**. On-Prem: Windows Service | |
| Kubernetes | «امکان دارد»؛ مهاجرت از Swarm آماده‌سازی و اعتبارسنجی Manifest می‌خواهد ⇒ در RFP «قابل توسعه»، نه «دارد» | |
| Service Mesh، ESB، GraphQL | **ندارد** | |

## استقرار، مقیاس و دسترس‌پذیری
- On-Premise ✔، Private Cloud ✔، Public Cloud ✔، **Hybrid ✖** (PGX). ⚠ RFI ۱۴۲ گفته «Cloud یا Hybrid موجود». در RFP، Hybrid را «نیاز به بررسی» یا «با طراحی زیرساخت» بنویس.
- **Multi-Tenant ✖**، Multi-Instance ✔، Stateless ✔، مقیاس افقی و عمودی ✔.
- Load Balancing: چند نمونه Application پشت **HAProxy** یا Load Balancer زیرساخت.
- HA: با HAProxy. Active/Active در لایه Application قابل پیاده‌سازی است؛ در لایه‌های دیگر به زیرساخت و DB بستگی دارد. Active/Passive تابع معماری HA/DR زیرساخت.
- DR: با Replication پایگاه داده، Backup و سایت جایگزین؛ طراحی بر اساس RTO/RPO توافقی. **RTO از ۶۰ دقیقه تا ۲۴ ساعت، RPO از ۱۵ دقیقه تا ۶ ساعت** بسته به سناریو.
- Uptime: PGX «0.999» را در ستونی با واحد درصد نوشته؛ منظور ۹۹٫۹٪ است. فقط با SLA قراردادی و زیرساخت مشخص تعهد بده.
- ظرفیت (PGX، On-Prem): حداقل **۵۰۰ کاربر همزمان** در بهره‌برداری عملیاتی؛ **۱۲۰۰ کاربر ثبت‌شده**؛ داده تا **۲TB**؛ تا **۱۲۰ میلیون رکورد** تست‌شده. TPS و زمان پاسخ: «وابسته به سناریو؛ نیازمند Benchmark».
- چندسروری: تفکیک وب/اپ و DB روی دو سرور (برای بیش از ۵۰ کاربر توصیه شده). محیط Test/Staging جدا ممکن است.
- چند شعبه، حتی خارج از ایران: با IP Static و اینترنت امن به یک نسخه وصل می‌شوند؛ دسترسی بین شعبه‌ها قابل تنظیم است.

## امنیت (شیت ۰۳ PGX + RFI)
| کنترل | وضعیت | توضیح |
|---|---|---|
| گواهی افتا محصول | دارد | ISO 15408/EAL1، آزمایشگاه شریف، cbp-c1470-0301، اعتبار تا ۱۴۰۵/۱۱/۰۸ |
| OWASP Top 10 | دارد (ادعا) | در طراحی و ارزیابی لحاظ شده؛ شاهد مستقل در سند مبنا نیست |
| Secure SDLC | دارد (ادعا) | بازبینی امنیتی پیش از انتشار |
| SAST | **ندارد** | ابزار خودکار مستقل استفاده نمی‌شود |
| DAST | دارد | Acunetix |
| SCA | دارد | بررسی آسیب‌پذیری Packageها |
| Secret Scanning | **ندارد** | |
| Vulnerability Management | دارد | ثبت و پیگیری در Azure DevOps |
| تست نفوذ دوره‌ای مستقل | **ندارد** | گزارش معتبر آخرین تست نفوذ هم موجود نیست |
| Patch Management | دارد | جست‌وجو و نصب خودکار به‌روزرسانی؛ کنترل اصالت با هش منتشرشده |
| CVE Management | **ندارد** | فرایند یا ابزار متمرکز ندارد |
| Audit Log | دارد | احراز هویت، نشست، عملیات مدیریتی، تغییرات امنیتی، ورود و خروج داده؛ شامل زمان، نوع، هویت، نتیجه و IP. KB: «سوابق ورود کاربر» (2.8.1) و «فعالیت‌های کاربر» (ایجاد، ویرایش، حذف، ارجاع؛ 2.8.4) در کنسول مدیریت کاربر. ⚠ مدیر می‌تواند با «ورود به سایت» به‌جای کاربر وارد شود (اقدامات به نام همان کاربر ثبت می‌شود) و لاگ آخرین ورود را حذف کند |
| Immutable Log | جزئی | لاگ در محصول فقط‌خواندنی است؛ کنترل Hash برای تشخیص تغییر ندارد |
| SIEM | قابل اتصال | با مکانیزم‌های استاندارد جمع‌آوری لاگ (شاهد صریح ندارد) |
| RBAC | دارد | Permission، نقش، سمت در چارت؛ شامل مشاهده، ایجاد، ویرایش، حذف و خروجی اکسل |
| ABAC | دارد | مالکیت رکورد، جایگاه در چارت، ویژگی‌های داده و کاربر |
| MFA / 2FA | دارد (OTP) | **KB 2.8.7: «الزام به ورود با کد تأیید یک‌بار مصرف»** برای کاربران، نمایندگان و مشتریان باشگاه (وب، اپ، تایم‌نگر، باشگاه)، سراسری یا برای هر کاربر؛ رسانه: پیامک، فکس یا پیام شبکه اجتماعی. OTP فراموشی رمز و ثبت‌نام با پیامک یا ایمیل (2.8.6). **TOTP شاهد ندارد** (ادعای PGX) |
| SSO | دارد | IdentityServer، OAuth2/OIDC؛ RFI: با AD/LDAP و توکن وب‌سرویس (با پیکربندی) |
| LDAP/AD | دارد | Microsoft Active Directory |
| OAuth2 / OIDC / JWT | دارد | |
| Certificate Management | دارد | X509v3/RFC 5280، CA/basicConstraints، OCSP/CRL |
| mTLS | ⚠ نیازمند تأیید | سند امنیتی هم «احراز دوطرفه TLS» را تیک زده هم نوشته «محصول کلاینت‌ها را احراز نمی‌کند» |
| Encryption in Transit | دارد | HTTPS/TLS الزامی؛ SSL Valid روی IIS |
| Encryption at Rest (لایه اپلیکیشن) | **ندارد** | رمز عبور Hash می‌شود. Column-level encryption ندارد (RFI ۱۵۷: «قابل ارائه نیست») |
| Database Encryption | با زیرساخت | SQL Server TDE توسط DBA مشتری |
| Key Management | جزئی | RSA 2048، ECDH(E)، DH 2048 و نابودی کلید مستند است؛ چرخه کامل مدیریت کلید مستند نیست |
| Password Policy | دارد | حروف کوچک و بزرگ، عدد، کاراکتر خاص، تاریخچه، حداقل ۸ کاراکتر، تغییر اجباری در ورود اول |
| Session Management | دارد | KB: مدت نشست پیش‌فرض ۳۰ دقیقه، قابل تنظیم ۵ تا ۱۰۰۸۰ دقیقه؛ تمدید بر اساس آخرین فعالیت؛ نگهداری نشست در مرورگر؛ سقف نشست همزمان (مرورگر و اپ)؛ Refresh Token با مدت قابل تنظیم (2.8.1 تا 2.8.7) |
| محدودیت IP و زمان | **دارد (برای هر کاربر)** | KB 2.8.1: «آدرس‌های IP مجاز کاربر» و «روز و ساعت‌های مجاز هفته» در کنسول مدیریت کاربر. Allow-list سراسری و محدودیت جغرافیایی ⇒ IIS و فایروال |
| PAM | **ندارد** | دسترسی مدیریتی با Role/Permission و Audit؛ قابل اتصال به PAM سازمان |
| الگوریتم‌ها | AES / SHA (سند امنیتی) | |

## کنترل‌های داده در محصول (KB)
- «محدودکردن مشاهده اطلاعات مخاطبان به کاربران مرتبط» (مسئول فروش، پشتیبانی یا متفرقه)؛ مدیر بانک اطلاعاتی مستثناست.
- «زمان مجاز حذف مخاطب از تاریخ ایجاد»؛ حذف نظر فقط تا ۱ ساعت بدون مجوز (2.8.7.1).
- مجوز جدا برای «دریافت خروجی اکسل» (ستون‌های لیست) و «دریافت خروجی کامل آیتم» (2.8.8).
- محدودیت تعداد و حجم فایل آپلودی (2.8.8).
- نمایش هویت در جست‌وجو منوط به مجوز «مشاهده لیست» زیرنوع (2.8.4).
- «ممانعت از ارتباط با وب‌سرویس‌های فاقد گواهی SSL معتبر».
- رمز: پیچیدگی (حرف بزرگ، کوچک و عدد)، حداقل طول، تغییر در اولین ورود، انقضای دوره‌ای (روز)، و استثنای «رمز هرگز منقضی نشود» برای هر کاربر.
- کنسول کاربر: فعال‌سازی، Unlock، تعلیق و رفع تعلیق، تغییر رمز توسط مدیر، منقضی‌کردن نشست.

## یکپارچه‌سازی و API (شیت ۰۴ PGX)
- REST API ✔ (Swagger/OpenAPI ✔؛ در پاسخ‌های قبلی تیم: «Swagger فقط با یوزر و پسورد اختصاصی»)، SOAP/WCF ✔، Webhook ✔ (و Service Task در BPMS)، Message Queue داخلی (RabbitMQ) ✔.
- ⚠ دامنه مستند در KB: **مستندات رسمی وب‌سرویس (developer.payamgostar.com) SOAP/WCF است** (۲۲ سند: Authentication، Person، Organization، Identity/Lead، Opportunity، Invoice، Receipt/Payment، MoneyAccount، Contract، Form، Task، Ticket، Appointment، PhoneLog، BusinessNote، Product، PriceList، Inventory، EPay، ProcessEngine، CrmObjectType، Users). **REST** در Release Notes فقط برای **فرصت** (Find، و از 2.8.7.1 Create/Update/Delete) و فیلدهای لیستی (2.8.5) مستند است. **Webhook** مستند فقط برای **محصولات** (Insert/Update/Delete). جزئیات در `kb-evidence/api-guide.md`.
- **ندارد یا تأییدنشده**: GraphQL ✖، Event API، Batch/File Interface، API Versioning، Sandbox، Rate Limiting، API Monitoring، ESB ✖. PGX: «آماده‌بودن API برای همه حوزه‌ها باید به تفکیک سرویس تأیید شود».
- مستندات: پورتال توسعه‌دهندگان در help.payamgostar.com؛ دسترسی به API رایگان.
- احراز هویت API: توکن وب‌سرویس (OAuth2/JWT طبق شیت ۰۳؛ شیت ۰۴ می‌گوید «در سند امنیتی تأیید نشده»).
- اتصال به DB خارجی: ماژول «تخصیص داده پیشرفته» (SQL و Expression).
- حوزه‌های بانکی (Core Banking، Mobile/Internet Banking، ATM، POS، AML، اعتبارسنجی): اتصال آماده ندارد؛ فقط از راه API یا پروژه.
- BI: Power BI (ماژول). DMS: اتصال آماده ذکر نشده. DWH/Data Lake: ذکر نشده.

## پشتیبان‌گیری، پایش و عملیات (RFI)
- Backup: SQL Server Maintenance Plan (Full روزانه، Differential/Log ساعتی) به‌علاوه پوشه فایل‌های پیوست، روی NAS/Backup Server، و تست دوره‌ای Restore در محیط تست. دیتابیس و بکاپ روی دو درایو جدا (سند نصب).
- پایش: CPU، RAM، Disk، سرویس IIS و Application Pool، SQL Server، سرویس ویندوزی مرکز تماس، لاگ خطا؛ با ابزارهای پایش مشتری.
- مقاوم‌سازی: SSL روی IIS، بستن پورت‌های غیرضروری، محدودیت دسترسی مستقیم به SQL، سیاست رمز، محدودیت نشست، 2FA.
- پورت‌ها: TCP 80/443 (وب، باشگاه، وب‌سرویس)، 1433 (اپ به SQL)، 5038 (AMI به Issabel/Asterisk)، 801 (ارتباطات داخلی سرویس‌ها).
- سرویس‌ها و مسیرهایی که باید از آنتی‌ویروس Exclude شوند: `C:\Program Files (x86)\1st\…` (PayamGostar2Host.exe، PayamGostarActivation.exe، PgAgentConfManager.exe) و `C:\Program Files (x86)\Septa\UpdateCenter v1.0\…` (SeptaUpdateCenter.exe، SeptaUpdateCenterConfigurationManager.exe، SeptaUpdateService.exe).
- Release Notes در help.payamgostar.com/docs/releasenotes.

## کیفیت و تست در RFP
- Load Test: جدول پیش‌نیاز سخت‌افزار به‌علاوه همکاری در تست بار در زیرساخت مشتری. TPS تضمینی اعلام نشده.
- UAT: سناریوهای مورد تأیید کارفرما، در محیط تست، با صورت‌جلسه.
