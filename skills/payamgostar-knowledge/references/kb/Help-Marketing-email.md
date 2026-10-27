# مستندات رسمی پیام‌گستر — Help-Marketing-email

منبع: مخزن رسمی 1stco/PayamGostarDocs (commit e6143c66b174، ۱۴۰۵/۰۶/۱۴) — متن مقاله‌های help.payamgostar.com/docs. تصاویر به‌صورت پیوند `![IMG-…](</kb-assets/kb-images/…>)` (مسیر از ریشه مخزن PGSkill) آمده‌اند؛ متن داخل تصویر جست‌وجو نمی‌شود. فهرست تصاویر: `references/kb-images-index.csv`.

## پروتکل‌های قابل پشتیبانی ایمیل
`مسیر سند: Help/Marketing/email/email-support.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/email-support.md)

-  POP3

-  IMAP

-  SMTP

**1.POP3:**  با استفاده از POP3 کامپیوتر شما به سراغ سرور می رود و پیام های جدید را دانلود می کند. شما این امکان را خواهید داشت که یک کپی از پیام را روی سرور برای مدت زمان مشخصی نگه دارید و سپس پیام پاک شود و یا اینکه کلاً با انجام تنظیمات مرتبط پیام های دانلود شده بلافاصله از روی سرور پاک شوند. این تنظیمات در بخش Account Settings و تب Advanced اعمال می شود. این پروتکل، قدیمی‌ترین طراحی است و در دوره‌ای بیشتر مورد استفاده قرار می‌گرفت که اتصالات از طریق مودم‌های (Dial-up) معمول بود. POP به کاربران امکان می‌دهد هنگام برقراری ارتباط، ایمیل‌های خود را بازیابی کرده و بدون نیاز به آنلاین ماندن روی پیغام‌های بازیابی شده فعالیت کنند.

> از آنجایی‌که ایمیل باید قبل از به نمایش در آمدن ابتدا دانلود شود، ممکن است در استفاده از پروتکل POP3 با مشکلات زیر روبه رو شوید:
اگر پای کامپیوتر دیگری بنشینید و بخواهید ایمیل خود را دریافت کنید باید تمام ایمیل‌ها را یکبار دیگر دریافت کنید.اگر قصد چک کردن ایمیل‌های خود را هم در منزل و هم در محل کار داشته باشید ممکن است دچار سردرگمی شوید. تمامی پیام‌ها و فایل‌های ضمیمه شده به ایمیل‌ها در فرآیند “Check new email” به طور کامل باید دانلود شوند.

**2.IMAP:**  پروتکل جدیدتری است که براساس حالت **«متصل»** عمل می‌کند. رویه حالت استاندارد این پروتکل، قرار دادن پیغام‌ها در سرور به‌جای بازیابی نسخه‌های آن است بنابراین ایمیل‌ها تنها زمانی قابل دسترسی است که آنلاین باشید.

این پروتکل به شما امکان می‌دهد به ایمیل‌های خود در بیش از یک مکان دسترسی داشته باشید. به‌عنوان مثال از رایانه رومیزی خود در محل کار، از لپ‌تاپ خود در منزل و همچنین از گوشی تلفن همراه خود در مکان‌های مختلف و از آنجا که پیغام‌ها در سرور باقی می‌مانند، تا زمانی که توسط کاربر حذف نشده باشند، از طریق رایانه‌های مختلف قابل دسترس خواهد بود.

نیاز به همواره آنلاین بودن برای خواندن ایمیل‌ها، زمانی که این‌گونه اتصال‌ها همیشه در دسترس هستند مساله بزرگی به‌حساب نمی‌آید (مانند این است که نامه‌های خود را در اداره پست بگذارید و هر زمان که خواستید به آنجا رفته و آنها را بخوانید. ممکن است در دنیای واقعی مشکل باشد ولی در جهان مجازی بسیار ساده خواهد بود).

IMAP اجازه می‌دهد ایمیل‌هایی را که در سرور میزبان قرار دارد مشاهده کنید؛ بنابراین هر تغییری که روی آنها بدهید (حذف، پاسخ، ارسال مجدد و جابه‌جایی) توسط هر شخص دیگری که در حساب ایمیل یا IMAP وارد شود، دیده خواهد شد.

**3.SMTP** از پروتکل استاندارد SMTP  برای ارسال پیام‌های امن در اینترنت می‌توان استفاده کرد، البته SMTP برای دریافت ایمیل هم استفاده می‌شود اما به دلیل این که مدیریتی بر روی ایمیل‌های دریافتی مانند دو پروتکل IMAP و POP3  نداریم(برای مثال ساخت پوشه، دسته بندی ایمیل‌ها) از این پروتکل برای دریافت استفاده نمی‎‌کنیم.
پروتکل SMTP برای کار خود از دو پورت زیر استفاده می‌کند:

**1.**	پورت 25 به صورت پیش‌فرض و رمزنگاری نشده می‌باشد.

**2.**	پورت 465 به صورت رمزنگاری شده(SSL) و برای ارسال **پیام‌های امن SMTP** مورد استفاده قرار می‌گیرد.

## ایمیل
`مسیر سند: Help/Marketing/email/email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/email.md)

در این بخش امکان مشاهده گزارش از ارسال ایمیل ها، بصورت نموداری می باشد که شامل دو نمودار می باشد:

**نمودار پیام کوتاه های ارسالی در ماه های گذشته:**  بصورت خودکار سه ماه گذشته نمایش داده می شود ، که در هر کدام از این ماه ها چه تعداد ایمیل ارسال شده، چه تعداد رسیده ، چه تعداد از ایمیل ها توسط مخاطب باز شده و چه تعداد از ایمیل ها را که شامل لینک بوده روی لینک کلیک شده است  .

**نمودار پیام کوتاه های ارسالی در 90 روز گذشته:**  در این قسمت گزارش نموداری ارسال پیام ها در 90 روز گذشته نمایش داده می شود ، چه تعداد رسیده ، چه تعداد از ایمیل ها توسط مخاطب باز شده و چه تعداد از ایمیل ها را که شامل لینک بوده روی لینک کلیک شده است

> نکته: کاربر برای استفاده از برنامه های تبلیغاتی مربوط به ایمیل نیاز به مجوز ارسال ایمیل دارد .

![IMG-0771](</kb-assets/kb-images/Help/Marketing/email/advertising-mail.webp>)

[اپراتور ارسال](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Send-operators/Send-operators.md)

[فرستنده ایمیل](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Email-sender/Email-sender.md)

[ایمیل ویژه - هوشمند](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Smart-email/smart-email.md)

[طریقه ایجاد یک ایمیل عکس دار](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Photo-email/Photo-email.md)

[مدیریت ارسال گروهی ایمیل](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/send-group-email/send-group-email.md)

[رویداد تبلیغاتی](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Advertising-event-email/advertising-event-email.md)

[خبرنامه](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Newsletters-email/Newsletters-email.md)

[لیست ایمیل‌های ارسالی](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Send-List-email/send-list.-email.md)

[لیست ایمیل‌های دریافتی](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/resive-list-email/resive-list-email.md)

## ارسال ایمیل از صفحه هویت
`مسیر سند: Help/Marketing/email/ersal-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/ersal-email.md)

در صفحه‌ی اصلی هویت‌ها امکان ارسال ایمیل وجود دارد.

![IMG-0772](</kb-assets/kb-images/Help/Marketing/email/ersal-email.jpg.webp>)

با استفاده از این بخش، صفحه‌ی ارسال ایمیل در دسترس قرار می‌گیرد و همچنین امکان پیوست فایل برای ارسال در این بخش وجود دارد.

![IMG-0773](</kb-assets/kb-images/Help/Marketing/email/ersal-email2.jpg.webp>)

## خبرنامه
`مسیر سند: Help/Marketing/email/Newsletters-email/Newsletters-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Newsletters-email/Newsletters-email.md)

با استفاده از این قابلیت این امکان فراهم می شود تا در تاریخ های مورد نظر پیام های  هوشمند مختلفی را برای مخاطبان خود ارسال کنید .

در صفحه اول، می توان با تعیین تاریخ اجرا، کاربر ایجاد کننده برنامه،نام برنامه تعریف شده و براساس قابلیت عضویت و لغو عضویت و زدن دکمه فیلتر، لیست برنامه های اجرا شده در گذشته را مشاهده کرد. اما برای اجرای یک برنامه جدید باید بر روی دکمه "خبرنامه جدید" در سمت راست و بالای صفحه کلیک کرده و بالای صفحه کلیک کرده و با گذراندن چند گام ساده، برنامه را به راحتی اجرا نمایید.

لطفا ابتدا  [اطلاعات مشترک بین ابزارها](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/moshtarak-abzar/moshtarak-abzar.md) را مطالعه فرمایید و طبق گام های زیر برای ارسال گروهی جدید اقدام فرمایید

 گام 1- [اطلاعات خبرنامه](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Newsletters-email/1-avalie-khabarname-email/1-avalie-khabarname-email.md)

گام 2-  تنظیم متن

گام 3-  انتخاب مخاطبان

![IMG-0784](</kb-assets/kb-images/Help/Marketing/email/Newsletters-email/advertising-sendingnewsmail-home.webp>)

## گام 3 -  مدیریت مخاطبان خبرنامه ایمیل
`مسیر سند: Help/Marketing/email/Newsletters-email/3-mokhatab-khabarname-email/3-mokhatab-khabarname-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Newsletters-email/3-mokhatab-khabarname-email/3-mokhatab-khabarname-email.md)

برای اطلاعات بیشتر به انتخاب مخاطبان مراجعه نمایید.

این مخاطبان باید شامل پروفایل هایی باشند که آدرس ایمیل در آن ها وجود داشته باشد .

![IMG-0787](</kb-assets/kb-images/Help/Marketing/email/Newsletters-email/3-mokhatab-khabarname-email/advertising-sendingnewsmail-thirdstep.webp>)

## گام 1 -  اطلاعات پیام خبرنامه ایمیل
`مسیر سند: Help/Marketing/email/Newsletters-email/1-avalie-khabarname-email/1-avalie-khabarname-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Newsletters-email/1-avalie-khabarname-email/1-avalie-khabarname-email.md)

لطفا ابتدا[ اطلاعات مشترک ابزارها ](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/moshtarak-abzar/gam-se/select-Audience.md)را مطالعه فرمایید و طبق گام های زیر برای ارسال گروهی جدید اقدام فرمایید

> نکته: تنها تفاوت موجود با پیام کوتاه در این است که در ایمیل امکان عضویت خودکار موجود نیست.

![IMG-0785](</kb-assets/kb-images/Help/Marketing/email/Newsletters-email/1-avalie-khabarname-email/advertising-sendingnewsmail-firststep.webp>)

## گام 2 -  محتوای پیام خبرنامه ایمیل
`مسیر سند: Help/Marketing/email/Newsletters-email/2-tanzimmatn-khabarname-email/2-tanzimmatn-khabarname-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Newsletters-email/2-tanzimmatn-khabarname-email/2-tanzimmatn-khabarname-email.md)

برای اطلاعات بیشتر به [گام تنظیم متن](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/send-group-email/2-tanzim-matn-email/2-tanzim-matn-email.md) ارسال گروهی ایمیل مراجعه نمایید.

![IMG-0786](</kb-assets/kb-images/Help/Marketing/email/Newsletters-email/2-tanzimmatn-khabarname-email/advertising-sendingnewsmail-secondstep.webp>)

## ارسال ایمیل از طریق ویجت دسترسی سریع
`مسیر سند: Help/Marketing/email/Quick-access/2.6.0/Send-Mail.md` · `نسخه سند: 2.6.0` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Quick-access/2.6.0/Send-Mail.md)

از طریق ویجت دسترسی سریع در صورت داشتن دسترسی به خطوط ایمیل می‌توانید از صفحه ارسال ایمیل، یک ایمیل جدید ارسال کنید.

![IMG-0794](</kb-assets/kb-images/Help/Marketing/email/Quick-access/2.6.0/Send-Mail.webp>)

**از:** در این قسمت می‌توانید از بین ایمیل‌های به اشتراک گذاشته شده برای شما، یک ایمیل را به عنوان فرستنده انتخاب نمایید.

**اصل:** در این قسمت آدرس ایمیل گیرنده یا گیرندگان مورد نظر خود را وارد کنید.

**رونوشت:** در صورتی که برای چند گیرنده ایمیلی به حالت رونوشت ارسال شود، تمامی گیرندگان می‌توانند لیست باقی گیرندگان و ایمیل‌هایی که در پاسخ ایمیل فرستاده شده است را مشاهده کنند.

**رونوشت مخفی:** در صورتی که ایمیل به حالت رونوشت مخفی ارسال شود، لیست گیرندگان و ایمیل‌هایی که در پاسخ ایمیل فرستاده شده است قابل مشاهده نخواهد بود ( در واقع نمی‌توان فهمید ایمیل به چه کسانی ارسال شده و چه ایمیل‌هایی در جواب ایمیل فرستاده شده است.) .

> **نکته:** ارسال ایمیل به صورت رونوشت و رو نوشت مخفی تنها از طریق پروتکل SMTP امکان پذیر است.

در صورت نیاز به الصاق فایل (Attach) می‌توانید از گزینه انتخاب فایل استفاده کنید. سپس موضوع و محتوای ایمیل خود را مشخص کرده و روی دکمه "ارسال کردن" کلیک کنید.

## ایمیل ویژه هوشمند
`مسیر سند: Help/Marketing/email/Smart-email/smart-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Smart-email/smart-email.md)

ایمیل ویژه برای دنبال کردن عکس العمل مخاطب شماست. آگاهی از تاثیر پیام شما بر مخاطب می تواند در بهبود تبلیغات شما تاثیر بسزایی داشته باشد. با انتخاب این  اپراتور ،  ارسال ها دارای تضمین Inbox  هستند و پس از ارسال موفق یا ناموفق بودن ارسال و همچنین باز شدن و یا نشدن ایمیل توسط مخاطب را به کاربر نمایش می دهد.

نکته جالب توجه در ارسال ایمیل ویژه، قراردادن لینک ویژه است. می توان در قسمت تنظیم متن لینکی قرارداد و با کلیک راست بر روی آن و انتخاب لینک ویژه، این لینک را قابل ردگیری کرد. به این شکل که اگر دریافت کننده ایمیل بر روی لینک کلیک نمایید در نمودار در ستون مخاطبان بازخورده نمایش داده می شود.

![IMG-0798](</kb-assets/kb-images/Help/Marketing/email/Smart-email/11.webp>)

**1**. با استفاده از این گزینه می توانید یک لینک به ایمیل خود اضافه کنید(مانند HTTP://PAYAMGOSTAR.COM)

![IMG-0799](</kb-assets/kb-images/Help/Marketing/email/Smart-email/12.webp>)

**2**. با راست کلیک بر روی یک لینک می توانید آن را به صورت ویژه تعیین کنید. در گزارشات مربوط به این ارسال تعداد مخاطبانی که بر روی این لینک کلیک کرده اند را نیز می توان مشاهده کرد.

**3**. با استفاده از این گزینه هم می شود لینک ویژه ایجاد کرد و یا لینک ایجاد شده را به لینک ویژه تبدیل کرد.

> نکته: در صورتی که می خواهید از SMTP   برای ارسال ایمیل استفاده نمایید ایمیل شما قابلیت ردگیری نخواهد داشت.

## رویداد تبلیغاتی
`مسیر سند: Help/Marketing/email/Advertising-event-email/advertising-event-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Advertising-event-email/advertising-event-email.md)

برای ارسال پیام هوشمند در زمانبندهای دقیق و پیشرفته، می توانید از رویداد تبلیغاتی استفاده کنید.

با استفاده از رویداد می توان زمانبندی های مشخصی برای ارسال پیام های متفاوت در نظر گرفت ، برای مثال می توان برای تاریخ هایی که در مدیریت اعیاد و مناسبت ها تعریف شده است پیام های متفاوتی تنظیم کرد تا در همان تاریخ ها برای مخاطبان انتخاب شده ،  ارسال شود .

 در صفحه اول، می توان با تعیین تاریخ اجرا ، ایجاد کننده رویداد و یا عنوان تعریف شده برای رویداد و زدن دکمه فیلتر، لیست برنامه های اجرا شده در گذشته را مشاهده کرد. اما برای اجرای یک برنامه جدید باید بر روی دکمه " رویداد جدید " در سمت راست و بالای صفحه کلیک کرده و با گذراندن چند گام ساده، برنامه را به راحتی اجرا کرد

 لطفا ابتدا [اطلاعات مشترک بین ابزارها](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/moshtarak-abzar/moshtarak-abzar.md) را مطالعه فرمایید و طبق گام های زیر برای ارسال گروهی جدید اقدام فرمایید

 گام 1- اطلاعات رویداد

گام 2-  [زمان اجرا](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Advertising-event-email/2-zamanbandi-roydad-email/2-zamanbandi-roydad-email.md)

گام 3-  تنظیم متن

گام 4-  انتخاب مخاطبان

![IMG-0774](</kb-assets/kb-images/Help/Marketing/email/Advertising-event-email/advertising-sendingeventmail-home.webp>)

## گام 4 -  مدیریت مخاطبان رویداد تبلیغاتی ایمیل
`مسیر سند: Help/Marketing/email/Advertising-event-email/4-mokhatab-roydad-email/4-mokhatab-roydad-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Advertising-event-email/4-mokhatab-roydad-email/4-mokhatab-roydad-email.md)

برای اطلاعات بیشتر به لینک [انتخاب مخاطبان ](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/moshtarak-abzar/gam%20se/select-Audience.md)در برنامه پیام کوتاه مراجعه نمایید.

این مخاطبان باید شامل پروفایل هایی باشند که آدرس ایمیل در آن ها وجود داشته باشد .

![IMG-0778](</kb-assets/kb-images/Help/Marketing/email/Advertising-event-email/4-mokhatab-roydad-email/advertising-sendingeventmail-fourthtstep.webp>)

## گام 1 - اطلاعات پیام رویداد تبلیغاتی ایمیل
`مسیر سند: Help/Marketing/email/Advertising-event-email/1-avalie-roydad-email/1-avalie-roydad-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Advertising-event-email/1-avalie-roydad-email/1-avalie-roydad-email.md)

به بخش گام اول - اطلاعات پیام در [اطلاعات مشترک بین ابزارها](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/moshtarak-abzar/moshtarak-abzar.md) مراجعه کنید.

![IMG-0775](</kb-assets/kb-images/Help/Marketing/email/Advertising-event-email/1-avalie-roydad-email/advertising-sendingeventmail-firststep.webp>)

## گام 3 -  محتوای پیام رویداد تبلیغاتی ایمیل
`مسیر سند: Help/Marketing/email/Advertising-event-email/3-matn-roydad-email/3-matn-roydad-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Advertising-event-email/3-matn-roydad-email/3-matn-roydad-email.md)

برای اطلاعات بیشتر به   گام تنظیم متن ارسال گروهی ایمیل مراجعه نمایید.

![IMG-0777](</kb-assets/kb-images/Help/Marketing/email/Advertising-event-email/3-matn-roydad-email/advertising-sendingeventmail-thirdstep.webp>)

## گام 2 -  زمان اجرای رویداد تبلیغاتی ایمیل
`مسیر سند: Help/Marketing/email/Advertising-event-email/2-zamanbandi-roydad-email/2-zamanbandi-roydad-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Advertising-event-email/2-zamanbandi-roydad-email/2-zamanbandi-roydad-email.md)

به [گام زمان اجرا](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/sms/Advertising-event/2-zaman-bandi/zaman-bandi.md) در رویداد تبلیغاتی پیام کوتاه مراجعه کنید.

![IMG-0776](</kb-assets/kb-images/Help/Marketing/email/Advertising-event-email/2-zamanbandi-roydad-email/advertising-sendingeventmail-secondstep.webp>)

## اپراتور ایمیل پرتال اول
`مسیر سند: Help/Marketing/email/Send-operators/Send-operators.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Send-operators/Send-operators.md)

 اپراتور ارسال ایمیل می تواند پرتال اول و یا SMTP  باشد. برای ارسال ایمیل از طریق پرتال اول باید در پرتال اول دارای حساب کاربری باشید و در منوی 1st، مشخصات کاربری، نام کاربری و رمز عبور خود را وارد کرده باشید.

## طریق ایجاد یک ایمیل عکس دار
`مسیر سند: Help/Marketing/email/Photo-email/Photo-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Photo-email/Photo-email.md)

برای ارسال ایمیل عکس دارد باید تصویر مورد نظر در یک سایت آپلود شود

و  آدرس آن فایل را در داخل گام تنظیم متن مطابق تصویر وارد نمود. تنها از این طریق، تصویر موجود در متن، در ایمیل های مخاطبان مشاهده خواهد شد.

سایت www.1st.ir  این فرصت را برای شما فراهم آورده است که تصاویر و فایل های موردنیاز را در داخل خود سایت آپلود نمایید .

ابتدا می بایست به سایت پرتال اول مراجعه کرده و با نام کاربری خود وارد نمایید. همانطور که در تصویر مشاهده می نمایید به مسیر داشبورد من ---> پنل ایمیل ---> بانک فایل های من مراجعه نمایید .

**1**. ابتدا در سایت پرتال اول به قسمت داشبورد من مراجعه کنید. و برروی دکمه "می خواهم فروشنده شوم" کلیک نمایید.

![IMG-0788](</kb-assets/kb-images/Help/Marketing/email/Photo-email/13.webp>)

**2**. بر روی تب سه خط کلیک کنید تا وارد منوی پرتال شوید.

**3**. بر روی تبلیغات و ارتباط با مشتری و سپس بر روی پنل ارسال ایمیل کنید.

![IMG-0789](</kb-assets/kb-images/Help/Marketing/email/Photo-email/14.webp>)

**4,5** . آپلود فایل را انتخاب و سپس تصویر مورد نظر خود را انتخاب کنبد .

![IMG-0790](</kb-assets/kb-images/Help/Marketing/email/Photo-email/advertising-mail-1st-7.webp>)

![IMG-0791](</kb-assets/kb-images/Help/Marketing/email/Photo-email/advertising-mailimage-1st-6.webp>)

**6**. لینک مورد نظر را کپی کنید.

![IMG-0792](</kb-assets/kb-images/Help/Marketing/email/Photo-email/advertising-mail-1st-8.webp>)

هنگام اجرای برنامه ایمیل گروهی، در گام محتوای پیام بر روی آیکون " InsertImage" کلیک می نماییم و در پنجره جدید آدرس موردنظر را در کادر "ImageSrc"  وارد می نماییم.

![IMG-0793](</kb-assets/kb-images/Help/Marketing/email/Photo-email/advertising-mailsending-1st-5.webp>)

## لیست پیام‌های دریافتی
`مسیر سند: Help/Marketing/email/resive-list-email/resive-list-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/resive-list-email/resive-list-email.md)

در این پنجره تمام ایمیل هایی که پس از اجرای برنامه های مختلف به شماره شما ارسال شده است، نمایش داده می شود. شماره خط و ارسال کننده و همچنین تاریخ دریافت نمایش داده می شود. همچنین می توان لیست ایمیل ها را با فاکتورهایی مانند تاریخ دریافت و یا بازه ای بین دو تاریخ محدود نمود.

برای دیدن متن ارسال شده بر روی لینک محتوای پیام  در روبروی هر سطر کلیک نمایید.

![IMG-0800](</kb-assets/kb-images/Help/Marketing/email/resive-list-email/15.webp>)

## اپراتور ارسال ایمیل پرتال اول
`مسیر سند: Help/Marketing/email/Email-sender/Email-sender.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Email-sender/Email-sender.md)

اپراتور ارسال ایمیل می تواند پرتال اول و یا SMTP باشد. برای ارسال ایمیل از طریق پرتال اول باید در پرتال اول دارای حساب کاربری باشید و در منوی 1st، مشخصات کاربری، نام کاربری و رمز عبور خود را وارد کرده باشید.
آدرس ایمیلی که ایمیل‌های ویژه شما از آن ارسال می‌شود از طریق این صفحه قابل تغییر می‌باشد.

ابتدا از طریق نام کاربری خود در سایت www.1st.ir  وارد شوید و سپس مانند شکل زیر عمل کنید:

**1**. در بالای صفحه روی نام خود و سپس روی دکمه **" میخواهم فروشنده شوم"** کلیک کنید.

![IMG-0779](</kb-assets/kb-images/Help/Marketing/email/Email-sender/advertising-mail-1st-1.webp>)

**2**. سپس در صفحه پیش رو، روی دکمه سه خط، مانند شکل کلیک کنید تا تب منو برای شما باز شود.

![IMG-0780](</kb-assets/kb-images/Help/Marketing/email/Email-sender/advertising-mail-1st-2.webp>)

**4و3**. در منوی باز شده، در قسمت **"تبلیغات و ارتباط با مشتری"** کلیک کرده و سپس **"پنل ارسال ایمیل"** را کلیک کنید.

![IMG-0781](</kb-assets/kb-images/Help/Marketing/email/Email-sender/advertising-mail-1st-3.webp>)

**5**. در پنل ارسال ایمیل وارد تنظیمات ایمیل می‌شوید. مانند شکل زیر

![IMG-0782](</kb-assets/kb-images/Help/Marketing/email/Email-sender/advertising-mail-1st-4.webp>)

**6**.در این کادر ایمیل پیش‌فرض جهت ارسال و نام فرستنده بصورت پیش‌فرض نوشته شده است که در صورت نیاز می‌توان تغییر داد.

![IMG-0783](</kb-assets/kb-images/Help/Marketing/email/Email-sender/advertising-mail-1st-5.webp>)

![IMG-0783](</kb-assets/kb-images/Help/Marketing/email/Email-sender/advertising-mail-1st-5.webp>)

## مدیریت ارسال گروهی
`مسیر سند: Help/Marketing/email/send-group-email/send-group-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/send-group-email/send-group-email.md)

با استفاده از این قابلیت امکان تعریف برنامه های گروهی برای ارسال پیام به گروه و یا دسته ای ار مخاطبان فراهم می شود در صفحه اول، می توان لیست برنامه های تنظیم شده را مشاهده کرد که با استفاده از فیلتر های مختلف می توان به برنامه مورد نظر دسترسی پیدا کرد .

 اما برای اجرای یک برنامه جدید باید بر روی دکمه " ارسال گروهی جدید " در سمت راست و بالای صفحه کلیک کرده و با گذراندن چند گام ساده، برنامه را به راحتی اجرا کرد .

 لطفا ابتدا [اطلاعات مشترک بین ابزارها](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/moshtarak-abzar/moshtarak-abzar.md) را مطالعه فرمایید و طبق گام های زیر برای ارسال گروهی جدید اقدام فرمایید

 گام 1- [اطلاعات اولیه ارسال گروهی](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Advertising-event-email/1-avalie-roydad-email/1-avalie-roydad-email.md)

گام 2-  تنظیم متن

گام 3-  انتخاب مخاطبان

![IMG-0801](</kb-assets/kb-images/Help/Marketing/email/send-group-email/advertising-sendinggroupmail-home.webp>)

## گام 3 - مدیریت مخاطبان ارسال گروهی ایمیل
`مسیر سند: Help/Marketing/email/send-group-email/3-mokhatab-email/3-mokhatab-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/send-group-email/3-mokhatab-email/3-mokhatab-email.md)

برای اطلاعات بیشتر به لینک  انتخاب مخاطبان  مراجعه نمایید .

این مخاطبان باید شامل پروفایل هایی باشند که آدرس ایمیل در آن ها وجود داشته باشد .

![IMG-0804](</kb-assets/kb-images/Help/Marketing/email/send-group-email/3-mokhatab-email/advertising-sendinggroupmail-thirdstep1.webp>)

## گام 2 -  محتوای پیام ارسال گروهی ایمیل
`مسیر سند: Help/Marketing/email/send-group-email/2-tanzim-matn-email/2-tanzim-matn-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/send-group-email/2-tanzim-matn-email/2-tanzim-matn-email.md)

در این گام می توانید متن مورد نظر برای ارسال را وارد و ویرایش کنید . از طریق منوی بالای صفحه (که شامل فایل، قالب و راهنمایی متن هوشمند می شود)، می توانید متون مورد نظر خود را که قبلا نوشته و در سیستم کامپیوتر خود ذخیره نموده اید وارد کنید، یا از قالب هایی که برای راحتی کار شما در نظر گرفته شده، استفاده کنید. همچنین امکان استفاده از متن هوشمند (به عنوان یکی از ویژگی های خاص پیام گستر) در این گام برای شما فراهم شده است

لطفا ابتدا گام دوم - [محتوی پیام](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/moshtarak-abzar/gam-do/gam-do.md) در اطلاعات مشترک ابزارها را مطالعه کنید.

![IMG-0803](</kb-assets/kb-images/Help/Marketing/email/send-group-email/2-tanzim-matn-email/advertising-sendinggroupmail-secondstep.webp>)

**1. قرار دادن تصویر در متن:** به قسمت طریقه ایجاد یک  [ایمیل عکس دار](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Photo-email/Photo-email.md) مراجعه کنید.

**2. لینک آدرس اینترنتی:** استفاده از قابلیت لینک، در هر قسمت از متن که بخواهید می توانید یک آدرس اینترنتی را با کلیک بر آیکون InsertLink در بالای کادر متن به صورت لینک درآورید .کافی است URL مربوط به آن را در کادر آن وارد نمایید.

3. به قسمت [ایمیل ویژه - هوشمند](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/email/Smart-email/smart-email.md) مراجعه کنید.

## گام 1 -  اطلاعات پیام ارسال گروهی ایمیل
`مسیر سند: Help/Marketing/email/send-group-email/1-avalie-email/1-avalie-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/send-group-email/1-avalie-email/1-avalie-email.md)

به بخش گام اول - اطلاعات پیام در اطلاعات مشترک ابزارها مراجعه کنید.

این مخاطبان باید شامل پروفایل هایی باشند که آدرس ایمیل در آن ها وجود داشته باشد

![IMG-0802](</kb-assets/kb-images/Help/Marketing/email/send-group-email/1-avalie-email/advertising-sendinggroupmail-firststep.webp>)

## لیست ایمیل‌‌های ارسالی
`مسیر سند: Help/Marketing/email/Send-List-email/send-list.-email.md` · [منبع](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/Help/Marketing/email/Send-List-email/send-list.-email.md)

در یک برنامه تبلیغاتی برای مشاهده لیست ایمیل‌های ارسالی از مسير **ابزار تبليغات** > **ایمیل** > **ليست ایمیل‌هاي ارسالی** اقدام کنيد.
 در این صفحه ایمیل‌های ارسالی، آدرس گیرنده، تاریخ ارسال، وضعیت ارسال، وضعیت تحویل، وضعیت دنبال، محتوای پیام و گیرندگان قابل مشاهده است.

>**نکته**

>برای اطلاعات بیشتر در خصوص لیست ارسال ها به قسمت  [اطلاعات مشترک لیست ارسال](https://github.com/1stco/PayamGostarDocs/blob/master/Help/Marketing/sms/Send-ist/moshtarake-liste-ersal.md) مراجعه کنید.

![IMG-0795: لیست ایمیل‌های ارسالی](</kb-assets/kb-images/Help/Marketing/email/Send-List-email/ListofSentEmailsAdvertising.webp>)

**1**. با کليک راست بر روي يک ایمیل گزينه‌هاي زير مشاهده مي‌شود:

- **جزئیات ارسال**: در این قسمت جزئیات مرتبط با ارسال ایمیل مانند کد رهگیری، وضعیت تحویل و ارسال را می‌توانید مشاهده کنید.

![IMG-0796: جزئیات ایمیل ارسالی](</kb-assets/kb-images/Help/Marketing/email/Send-List-email/SendingEmailDetails.webp>)

- **سعی در ارسال دوباره**: در این گزينه، ایمیل دوباره ارسال خواهد شد.

- **جستجوی پروفایل مرتبط**: پروفایل‌هایی را که در نرم‌افزار شامل این ایمیل هستند نمایش می‌دهد.

- **باز کردن پروفایل مرتبط**: در صورتی که بسته به رسانه تبلیغاتی، اطلاعات ایمیل موردنظر، در پیام گستر ثبت شده باشد، با
انتخاب این گزینه پروفایل مربوط به این ایمیل  باز خواهد شد.

- **اضافه به گروه**: در صورتی که ایمیل مربوط به یک پروفایل در پیام گستر باشد، می‌توان از همین بخش آن را به گروه هدف خاصی برای پیگیری‌های آینده اضافه نمود.

**2. وضعیت ارسال و وضعیت تحویل**: این دو ستون می‌توانند به آگاهی شما از نتیجه ایمیل‌های ارسالی کمک کنند.

**3.محتوای پیام**: در ستون محتوای پیام، می توانید، متن ایمیل ارسالی خودر را ببینید .

**4. گیرندگان**: در ستون گیرندگان، آدرس ایمیل گیرندگان قابل مشاهده است.

**5. حذف کردن**: برای حذف سابقه ایمیل ارسال‌شده کافی است ایمیل‌های مورد نظر را با تیک انتخاب و سپس دکمه حذف را کلیک کنید.

**6.فرستادن به اکسل**: با استفاده از اين گزينه می‌توانید لیست ارسال‌های انتخاب شده را در قالب فایل اکسل دریافت کنید.

درقسمت فیلترها، با توجه فیلدهای مشخص‌شده می‌توانید دامنه نمایش ایمیل‌ها را محدود کنید.

![IMG-0797: فیلتر ایمیل‌های ارسال‌شده](</kb-assets/kb-images/Help/Marketing/email/Send-List-email/FilterSentEmail.webp>)

**1. وضعیت ارسال**: انواع وضعیت ارسال به شرح زیر است

- **در صف ارسال**: ایمیل به‌درستی در صف ارسال قرار گرفته و در حال ارسال است.

- **ارسال‌شده به مرکز**: ایمیل به‌درستی به پنل مرکز ارسال شده است.

- **ارسال‌شده به مخاطب**: مخاطب ایمیل را به‌درستی دریافت کرده است.

- **ارسال ناموفق**: مخاطب ایمیل را دریافت نکرده است.

- **ارسال دوباره**: نشان‌دهنده تلاش مجدد برای ارسال است.

**2. وضعیت تحویل**: انواع وضعیت تحویل به شرح زیر است

- **نامشحص**: هنوز مرکز پاسخی برای وضعیت تحویل ایمیل به مخاطب برای نرم افزار ارسال نکرده است.

- **تحویل داده شده**: ایمیل به مخاطب تحویل داده شده است.

- **ناموفق**: ایمیل به مخاطب تحویل داده نشده است.

**3 .از تاریخ/تا تاریخ**: ابتدا و انتهای بازه زمانی ارسال را در این قسمت مشخص کنید.

**4. به روز رسانی لیست**: با استفاده از این گزینه می‌توانید تعیین کنید که این لیست ارسال، هر چند ثانیه یکبار به‌روزرسانی شود.

**5. وضعیت دنبال**: اگر در ایمیل ارسال‌شده لینکی وجود داشته باشد و مخاطب آن را باز کرده باشد، وضعیت به دنبال‌شده تغییر می‌کند و در غیر این صورت دنبال‌نشده است.

**6. روش ارسال**: خط ارسال‌کننده ایمیل را در این قسمت مشخص کنید.

**7. ارسال به**: در این قسمت ایمیل مقصد را مشخص کنید.

**8. موضوع**: در این قسمت می‌توانید جستجو را بر اساس موضوع انجام دهید.
