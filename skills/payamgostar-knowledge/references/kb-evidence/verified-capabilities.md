# گزیده قابلیت‌ها و حدود تأیید

## فهرست
- هویت و سوابق
- فرم و شخصی‌سازی
- فرآیند
- فروش و دریافت
- انبار
- پشتیبانی
- باشگاه
- گزارش
- امنیت
- اتصال‌ها و ATS

این گزیده برای شروع پاسخ است. برای جزئیات و تعهد RFP، منبع همان بند را بخوان. ذکر یک قابلیت در این فایل به معنای فعال بودن آن در همه بسته‌ها و نسخه‌های مشتری نیست. منابع با شناسه commit به snapshot رسمی متصل‌اند.

## هویت و سوابق

- داده اولیه فروش در قالب سرنخ حقیقی/حقوقی قابل ثبت است. در راهنمای ثبت سرنخ حقیقی، اطلاعات اولیه، مسئولان پروفایل، مشخصات اضافه و راه‌های ارتباطی از هم تفکیک شده‌اند. تعیین مسئول فروش، پشتیبانی و مسئول متفرقه در پرونده هویت دیده می‌شود. [ایجاد سرنخ حقیقی جدید](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Integrated-bank/Database/General-specifications/Lead-management/2.6.1/NewLead-person.md) (`repo-720f5fbf77099643`)
- برای هویت، امکان نگهداری چند راه ارتباطی و تعیین مورد پیش‌فرض تشریح شده است؛ این را با تعداد نامحدود هر نوع داده برابر ندان. همان راهنما توصیه می‌کند سرنخ در چند دسته هم‌زمان ذخیره نشود، هرچند امکانش را بیان کرده است. [ایجاد سرنخ حقیقی جدید](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Integrated-bank/Database/General-specifications/Lead-management/2.6.1/NewLead-person.md) (`repo-720f5fbf77099643`)
- تبدیل سرنخ به مخاطب، موضوع مستقلی در راهنماست؛ آن را با ثبت فرصت یا ثبت فاکتور یکی ندان. [تبدیل سرنخ به مخاطب](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Integrated-bank/Database/mafahim/tabdil-sarnakh.md) (`repo-3fd97eac4fde7ce3`)
- در ۲.۸.۷، سوابق هویت نمایش جدولی و زمانی دارند؛ برای آیتم مرحله‌دار، پس از فیلتر مناسب، نمای کانبان نیز توضیح داده شده است. [شرح تغییرات نسخه 2.8.7](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.7.md) (`repo-fdb40f24a63a1895`)
- در ۲.۸.۸، لیست‌های «سرنخ‌های من» و «مخاطبان من» برای رکوردهای ایجادشده توسط کاربر یا مرتبط با مسئولیت او آمده است. مشاهده ردیف در لیست، مجوز بازکردن پروفایل نیست. [شرح تغییرات نسخه 2.8.8](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.md) (`repo-5206215a52f84266`)

## فرم و شخصی‌سازی

- طراح فرم، افزودن و چیدمان دیداری گروه‌فیلد و فیلدها را با جابه‌جایی کشیدنی فراهم می‌کند. تنظیمات تخصصی بعضی فیلدها باید در بخش افزودن مشخصه تکمیل شود؛ طراح دیداری به‌تنهایی همه تنظیمات را انجام نمی‌دهد. [افزودن فیلد از طریق طراح فرم](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/Personalization-crm/CustomizationCommonSettings/FormDesignerTool.md) (`repo-d42f84c929d73706`)
- فرم عمومی یک URL برای دریافت اطلاعات خارج از محیط ورود کارکنان دارد. فرم می‌تواند با هویت مرتبط یا بدون آن ذخیره شود. در حالت مرتبط، قواعد جست‌وجوی هویت موجود و ایجاد سرنخ جدید باید تنظیم شوند. [تنظیمات فرم عمومی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Form/GeneralFormSetting_2.8.4.md) (`repo-5670244d36be702a`)
- برای ایجاد هویت جدید از فرم عمومی، زیرنوع سرنخ حقیقی یا حقوقی از قبل لازم است. این سازوکار را «ایجاد هر نوع هویت با هر سیاست تطبیق» توصیف نکن. [تنظیمات فرم عمومی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Form/GeneralFormSetting_2.8.4.md) (`repo-5670244d36be702a`)
- در ۲.۸.۸، برای عنوان فرم، گزینه‌های مقداردهی پیش‌فرض، خالی گذاشتن جهت تکمیل و پنهان‌کردن توضیح داده شده است. [شرح تغییرات نسخه 2.8.8](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.md) (`repo-5206215a52f84266`)
- تنظیم تعداد اعشار مبالغ در زیرنوع‌های مالی و فیلدهای پول/لیست مبلغ در ۲.۸.۸ مطرح است؛ امکان تبعیت از تنظیم ارز یا تنظیم جداگانه توضیح داده شده است. [شرح تغییرات نسخه 2.8.8](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.md) (`repo-5206215a52f84266`)

## فرآیند

- طراحی چرخه‌کاری، کارتابل، اقدام، فعالیت، انتظار و حالت نهایی منابع مستقل دارند. صرف وجود ابزار گردشکار، انطباق با همه اجزای استاندارد BPMN یا همه سناریوهای BPMS را اثبات نمی‌کند. [آشنایی با چرخه‌کاری در پیام‌گستر](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/Personalization-crm/Overview/Process-design/Concept-Process.md) (`repo-1ba69b33b8600cbf`)
- برای فعالیت‌های ثبت وظیفه/فرصت/قرارملاقات، ارسال پیام، تخصیص مقدار، شرط، تصمیم، عضویت، تأیید آیتم مالی و فراخوانی سرویس منابع جداگانه وجود دارد؛ تنظیم و محدودیت فعالیت موردنیاز را در همان منبع بررسی کن. [نحوه ایجاد فعالیت](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/Personalization-crm/Overview/Process-design/Create-a-work-cycle/Activity/Activity.md) (`repo-8b6bd685feacf28f`)
- فعالیت فراخوانی سرویس، آدرس، نوع درخواست، نگاشت ورودی و خروجی و مسیر موفقیت/خطا دارد. تعداد تلاش مجدد و فاصله تلاش‌ها نیز در راهنما آمده است. سرویس اختصاصی و کلیدهای فیلد/آیتم از پیش‌نیازهای سناریوی توسعه هستند. [فعالیت فراخوانی سرویس](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/Personalization-crm/Overview/Process-design/Create-a-work-cycle/Activity/Call-service/Call-service.md) (`repo-5d7c1fdfe8d88171`)
- این فعالیت، ابزار اتصال و اجرای سرویس است؛ وجود آن به‌تنهایی connector آماده یک محصول ثالث یا سازگاری تضمین‌شده با هر API را اثبات نمی‌کند. [فعالیت فراخوانی سرویس](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/Personalization-crm/Overview/Process-design/Create-a-work-cycle/Activity/Call-service/Call-service.md) (`repo-5d7c1fdfe8d88171`)
- نسخه ۲.۸.۷ به خروجی و بارگذاری تنظیمات فرآیند اشاره دارد. آن را بدون بررسی سند تخصصی «مهاجرت کامل همه داده‌های جاری و همه وابستگی‌ها» ننام. [شرح تغییرات نسخه 2.8.7](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.7.md) (`repo-fdb40f24a63a1895`)
- در ۲.۸.۷ دامنه expression برای دریافت، پرداخت، قرارملاقات و تماس گسترش یافته و رسید/حواله در همان متن استثنا شده‌اند. [شرح تغییرات نسخه 2.8.7](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.7.md) (`repo-fdb40f24a63a1895`)
- در ۲.۸.۸، تخصیص کار براساس بارِ کارتابل مشخص افزوده شده است؛ راهنما آن را از محاسبه کل کارهای فرآیند جدا می‌کند. [شرح تغییرات نسخه 2.8.8](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.md) (`repo-5206215a52f84266`)

## فروش و دریافت

- فرصت، پیش‌فاکتور، انواع فاکتور، قرارداد و دریافت/پرداخت را موجودیت‌های متفاوت در نظر بگیر. متد API یکی، پشتیبانی از دیگری را ثابت نمی‌کند. برای هر کدام در نمایه همان نام را جست‌وجو کن.
- ثبت ردیف تکراری محصول بدون تغییر نام و اقلام با مبلغ صفر در یادداشت ۲.۸.۷ فاکتور آمده است. امکان محصول تکراری در فرصت در یادداشت ۲.۸.۸ جداگانه مطرح شده است. [شرح تغییرات نسخه 2.8.7](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.7.md) (`repo-fdb40f24a63a1895`) [شرح تغییرات نسخه 2.8.8](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.md) (`repo-5206215a52f84266`)
- بررسی تکراری بودن کد محصول در ۲.۸.۸ قابلیت تنظیم دارد. رفتار ورود دستی/وب‌سرویس با ورود اکسل در همان سند یکسان نیست؛ امکان کد تکراری را به اکسل تعمیم نده. [شرح تغییرات نسخه 2.8.8](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.md) (`repo-5206215a52f84266`)
- در ۲.۸.۸.۲، اتصال POS برای ارسال مبلغ و ثبت دریافت پس از پرداخت توصیف شده و فعال‌سازی آن به هماهنگی با پیام‌گستر وابسته است. سازگاری همه مدل‌های کارتخوان از این متن نتیجه نمی‌شود. [شرح تغییرات نسخه 2.8.8.2](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.2.md) (`repo-634dbfe6bb17d622`)
- امکان انتخاب طرف پرداخت‌کننده کمیسیون در حساب مالی مرتبط با پول‌خرد، در یادداشت ۲.۸.۸.۱ آمده است؛ آن را به همه درگاه‌ها تعمیم نده. [شرح تغییرات نسخه 2.8.8.1](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.1.md) (`repo-0c957dd8dc13e90b`)
- در گزارش آیتم‌های مالی دارای تأیید دستی، تاریخ ایجاد و تاریخ تأیید دو مفهوم‌اند؛ تفکیک فیلتر آن‌ها در یادداشت ۲.۸.۸.۲ آمده است. [شرح تغییرات نسخه 2.8.8.2](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.2.md) (`repo-634dbfe6bb17d622`)

## انبار

- استفاده از انبارداری به ماژول مربوط، تعریف محصول و تعیین محصول مجاز انبار وابسته است. رسید، ورود کالا و حواله، خروج کالا را ثبت می‌کند. [مبانی انبارداری](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/InventoryManagement/PrinciplesOfWarehousing_2.8.3.md) (`repo-391dab4e982a4de4`)
- رسید موجودی اولیه در هر انبار محدودیت دارد؛ اگر پیش‌تر رسید/حواله ثبت شده باشد، راهنما اجازه ثبت موجودی اولیه را نمی‌دهد. وجود عملیات انبار را با «امکان ثبت موجودی اولیه در هر زمان» برابر ندان. [مبانی انبارداری](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/InventoryManagement/PrinciplesOfWarehousing_2.8.3.md) (`repo-391dab4e982a4de4`)
- رسید، حواله، مرجوعی و انتقال بین انبارها در مدل عملیاتی مستندند. عنوان یکی از مرجوعی‌ها در راهنمای مبانی نیازمند دقت است؛ جهت ورود/خروج و راهنمای تراکنش تخصصی را مبنا قرار بده. [مبانی انبارداری](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/InventoryManagement/PrinciplesOfWarehousing_2.8.3.md) (`repo-391dab4e982a4de4`)
- تنظیمات سریالی و گزارش/وب‌سرویس موجودی را با یک سیستم کامل برنامه‌ریزی تولید، MRP یا حسابداری صنعتی برابر ندان؛ برای چنین RFPهایی شاهد مستقل لازم است.

## پشتیبانی

- تیکت می‌تواند از پرونده مشتری یا منوی خدمات ثبت شود و به هویت مرتبط گردد. راهنمای مورد بررسی می‌گوید زیرنوع درخواست باید از شخصی‌سازی CRM ایجاد شده باشد. [درخواست پشتیبانی جدید](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Ticket/NewTicketing_2.8.3.md) (`repo-fe892fb2dfc01bd3`)
- جریان پاسخ تیکت مبتنی بر ایمیل تشریح شده است؛ اطلاعات مرتبط، مسئول، وضعیت، شدت و تأثیرگذاری وجود دارند و اولویت از ماتریس شدت/تأثیر تعیین می‌شود. صرف این مدل، تضمین SLA یا پوشش همه کانال‌های omnichannel را اثبات نمی‌کند. [درخواست پشتیبانی جدید](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Ticket/NewTicketing_2.8.3.md) (`repo-fe892fb2dfc01bd3`)

## باشگاه

- در راهنمای ۲.۸.۸، پنج مبنای قانون امتیاز وجود دارد: سریال، خرید محصول، ایجاد آیتم، ثبت‌نام و مبلغ خرید. این‌ها سناریوهای مختلف‌اند و پیش‌نیاز یکسان ندارند. [قوانین امتیازدهی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/Manage-all-kinds-of-profiles/ScoringRules_2.8.8.md) (`repo-c22ab2f95a223713`)
- امتیاز سریال به انبارداری سریالی و تنظیم اصالت وابسته است. در این روش و روش امتیاز خرید محصول، قانون امتیاز برای تک‌محصول بیان شده و تعیین امتیاز گروه محصول در همان متن رد شده است. [قوانین امتیازدهی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/Manage-all-kinds-of-profiles/ScoringRules_2.8.8.md) (`repo-c22ab2f95a223713`)
- امتیاز خرید محصول براساس تعداد در فاکتور تأییدشده محاسبه می‌شود. رد فاکتور و برگشت کالا بر امتیاز اثر دارند؛ بازگرداندن فاکتور به انتظار تأیید در این سند رفتار متمایزی دارد. برای محاسبه دقیق وضعیت‌های مالی را جدا کن. [قوانین امتیازدهی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/Manage-all-kinds-of-profiles/ScoringRules_2.8.8.md) (`repo-c22ab2f95a223713`)
- حذف آیتم غیرمالیِ امتیازآور و رد آیتم مالی می‌توانند باعث کسر امتیاز شوند؛ «اعطای امتیاز همیشگی پس از ایجاد» عبارت دقیقی نیست. [قوانین امتیازدهی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/Manage-all-kinds-of-profiles/ScoringRules_2.8.8.md) (`repo-c22ab2f95a223713`)

## گزارش

- گزارش‌ساز، محیط گزارش و داشبورد با RDL است. راهنمای آن شناخت روابط داده و آشنایی با RDL را پیش‌نیاز مهارتی می‌داند؛ همه گزارش‌های اختصاصی را بدون نیاز به تخصص معرفی نکن. [معرفی گزارش‌ساز پیام‌گستر](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Management-and-reports/Report-Builder/ReportBuilderIntroduction.md) (`repo-ece48efc5e4de827`)
- افزودن چند منبع اطلاعاتی به گزارش در منبع «گزارش‌ساز پیشرفته» آمده است. منابع داخلی شامل داده CRM، فرآیند، انبار، بازاریابی و ساختار سازمانی‌اند. تعریف کلید کاربر برای دیده‌شدن بعضی موجودیت‌ها و فیلدها شرط است. [افزودن منبع اطلاعاتی جدید](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Management-and-reports/Report-Builder/AddNewDataSet_2.7.0.md) (`repo-3dfb3b3beda2235a`)
- منبع داده خارجی با تنظیم اتصال دیتابیس تشریح شده است؛ این را به پشتیبانی همه موتورهای دیتابیس یا اتصال آماده هر ERP تعمیم نده. [افزودن منبع اطلاعاتی جدید](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Management-and-reports/Report-Builder/AddNewDataSet_2.7.0.md) (`repo-3dfb3b3beda2235a`)
- دستیار مدیر رایان، گزارش‌گیری از درخواست متنی، مشاهده SQL و در سناریوی مناسب نمودار دارد. ماژول، مجوز مربوط و حساب دارای اعتبار رایان در راهنما شرط شده‌اند. [دستیار هوش مصنوعی مدیران](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Management-and-reports/ManagerAssist-2.8.8.md) (`repo-6dd52f7eba4efbb8`)
- خروجی هوش مصنوعی را از نظر تعریف شاخص، فیلتر زمانی و روابط داده کنترل کن؛ وجود دستیار به معنای تضمین صحت همه خروجی‌ها یا قابلیت اجرای هر عملیات CRM نیست. [دستیار هوش مصنوعی مدیران](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Management-and-reports/ManagerAssist-2.8.8.md) (`repo-6dd52f7eba4efbb8`)
- آمار گزارش‌های آماده در نسخه‌ها متفاوت است؛ برای RFP به نسخه مشخص استناد کن و تعدادهای قدیمی/جدید را با هم جمع نکن. [شرح تغییرات نسخه 2.7.0](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.7.0.md) (`repo-65799cf5709bde48`) [شرح تغییرات نسخه 2.8.7](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.7.md) (`repo-fdb40f24a63a1895`)

## امنیت

- سند امنیت ۲.۸.۷ مدت نشست، تمدید از آخرین فعالیت، باقی‌ماندن نشست در مرورگر و سقف نشست هم‌زمان را تنظیمات جدا می‌داند. بازه مدت نشست در همین منبع ۵ تا ۱۰۰۸۰ دقیقه بیان شده است؛ برای نصب مشتری دوباره تأیید کن. [تنظیمات امنیتی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/General-settings/security/SecuritySetting-2.8.7.md) (`repo-3094cc7f5def2b3d`)
- الزام OTP برای کاربران، مشتریان و نمایندگان باشگاه در همین منبع آمده است. رسانه ارسال و خط پیش‌فرض، تنظیم پیام سیستمی دارند. برای ادعای MFA با روش خاص مانند TOTP، FIDO2 یا authenticator به شاهد اختصاصی نیاز است. [تنظیمات امنیتی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/General-settings/security/SecuritySetting-2.8.7.md) (`repo-3094cc7f5def2b3d`)
- پشتیبانی refresh token با مدت اعتبار توکن و refresh token، الزام پیچیدگی/حداقل طول رمز، تغییر رمز در اولین ورود و انقضای دوره‌ای رمز در سند دیده می‌شود. برای استثناهای کاربری، کنسول همان کاربر را بررسی کن. [تنظیمات امنیتی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/General-settings/security/SecuritySetting-2.8.7.md) (`repo-3094cc7f5def2b3d`)
- تنظیم جلوگیری از ارتباط با سرویس دارای گواهی نامعتبر، شاهد همان کنترل ارتباطی است؛ اثبات رمزنگاری پایگاه‌داده یا اعتبار همه گواهی‌های استقرار مشتری نیست. [تنظیمات امنیتی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/General-settings/security/SecuritySetting-2.8.7.md) (`repo-3094cc7f5def2b3d`)
- محدودکردن مشاهده هویت به مسئولان پروفایل، استثنای مدیر بانک اطلاعاتی دارد. بنابراین «هیچ کاربر دیگری تحت هیچ شرایطی نمی‌بیند» پاسخ نادرستی است. [تنظیمات امنیتی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/General-settings/security/SecuritySetting-2.8.7.md) (`repo-3094cc7f5def2b3d`)
- ثبت بازدید همه صفحات در سند امنیت حالت آزمایشی دارد؛ از آن برای تأیید قطعی audit trail کامل و تغییرناپذیر استفاده نکن. [تنظیمات امنیتی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Settings/General-settings/security/SecuritySetting-2.8.7.md) (`repo-3094cc7f5def2b3d`)
- در ۲.۸.۸، مجوز خروجی اکسل لیست از خروجی کامل آیتم تفکیک شده و محدودیت حجم/تعداد فایل توضیح داده شده است. محدودیت فایل در همان یادداشت برای فایل امضا استثنا دارد. [شرح تغییرات نسخه 2.8.8](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.8.md) (`repo-5206215a52f84266`)

- یادداشت قدیمی ۲.۵.۳ از واردکردن نام کاربران ActiveDirectory در نسخه پیشرفته نام می‌برد؛ import نام کاربری، شاهد SSO یا احراز هویت LDAP نیست. [مرجع قدیمی ActiveDirectory](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/2.5.3/2.5.3.md) (`repo-80c9982b102dc001`)

## اتصال‌ها و ATS

- SOAP و REST هر دو در منابع رسمی دیده می‌شوند؛ REST فرصت و فیلدهای لیستی دامنه مستند دارند. نوع پروتکل، endpoint و احراز هویت هر سرویس باید جدا تأیید شود. [REST فرصت](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.7.1.md) (`repo-e008ded2ea8a6443`) [فیلدهای لیستی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.5.md) (`repo-6df871bd1dd7f281`)
- اتصال تلگرام، ثبت پیام‌های ورودی/خروجی مرتبط با مخاطب و کاربرد در ارسال/برنامه تبلیغاتی در ۲.۸.۷.۱ بیان شده است؛ اتصال فعال، تنظیم رسانه و نسخه مشتری باید بررسی شوند. [مرجع ارتباط تلگرام](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.7.1.md) (`repo-e008ded2ea8a6443`)

- [ماتریس یکپارچه‌سازی](integration-matrix.md) را برای جهت انتقال هر موجودیت بخوان؛ گزارش «اتصال به سپیدار» جایگزین بررسی محصول، هویت، پیش‌فاکتور، فاکتور و دریافت به‌تفکیک نیست.
- در اتصال WooCommerce، مستندات ایجاد هویت/کاربر باشگاه، ثبت سفارش در آیتم مالی و دریافت و تأثیر بر موجودی را توضیح می‌دهند. لایسنس لازم است و همان منبع درباره مرحله آزمایشی و آماده نبودن انتشار عمومی افزونه هشدار دارد؛ وضعیت عرضه جاری را استعلام کن. [اتصال به ووکامرس](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/sync/WooCommerce/WooCommerceIntegrationPlugin.md) (`repo-2e3e55bc59b88c9e`)
- ATS، گردآوری و ارزیابی رزومه از پلتفرم‌های نام‌برده، ثبت هویت متقاضی، فرم آگهی و درخواست مصاحبه و ارجاع فرآیندی را تشریح می‌کند. این شاهد نرم‌افزار جامع حقوق‌ودستمزد، حضوروغیاب یا همه ماژول‌های HR نیست. [راهکار مدیریت منابع انسانی پیام‌گستر(ATS)](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/PayamgostarATS/WhatIsPayamgostarATS.md) (`repo-6fea9edc9bc1e0bd`)
- راهنمای تلفنی برای سانترال‌های پاناسونیک مدل‌های مشخص و پیش‌نیاز Caller ID و نیز برخی سیستم‌های مبتنی بر استریسک مثال دارد. سازگاری همه مدل‌ها/نسخه‌های نام تجاری یا یکسان‌بودن ضبط، شنود و نجوا در همه خطوط از آن نتیجه نمی‌شود. [سیستم تلفنی‌های قابل پشتیبانی](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Integrated-bank/Database/calls-h/poshtibani-khat.md) (`repo-30d2e808bacd7e12`)
