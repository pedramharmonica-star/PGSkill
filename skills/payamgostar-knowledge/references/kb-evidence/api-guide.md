# راهنمای بازیابی API رسمی

## فهرست
- سرویس‌ها
- احراز هویت و نشانی‌ها
- کیفیت منابع و استفاده از نمونه‌ها

## سرویس‌ها

۲۲ سند PDF از صفحه مستندات وب‌سرویس دریافت شده‌اند. نام‌های جدول، نمونه شناسه‌های موجود در سندند؛ امضای کامل، همه عملیات یا سازگاری نصب فعلی را نشان نمی‌دهند. قبل از ارائه کد، متن و جدول پارامترهای متد دقیق را بخوان.

| سند | دامنه | متدهای منتخب برای جست‌وجو | کارت |
|---|---|---|---|
| Appointment-2.pdf | قرارملاقات | `SearchAppointment, SaveAppointment, FindAppointmentById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Appointment-2.pdf) (`c95d3890d77adcfbe7f217e2`) |
| Authentication.pdf | احراز هویت | `AuthenticateUsernameAndPassword, Authenticate, ChangePassword` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/07/Authentication.pdf) (`0dddf9a28c19d03096e70123`) |
| BusinessNote.pdf | یادداشت | `SaveBusinessNote, GetBusinessNote` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/07/BusinessNote.pdf) (`fdf443cec2afa6c3d041d980`) |
| Contract.pdf | قرارداد | `SaveContract, SearchContract, FindContractById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Contract.pdf) (`bd052a390fe5e3e4720cd055`) |
| CrmObjectType.pdf | انواع موجودیت و اطلاعات نوع | `GetCrmObjectTypeInfo, GetCrmObjectTypeList` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2021/04/CrmObjectType.pdf) (`29a12fe0d06f2d8fc25ffb53`) |
| EPay.pdf | لینک پرداخت | `CreatePaymentLink` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2021/04/EPay.pdf) (`40dd1c3e149d6d5132a33393`) |
| Form.pdf | فرم | `SaveForm, SearchForm, FindFormById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Form.pdf) (`4b623c22a1b2b4c547559cef`) |
| Identity-2.pdf | هویت عمومی و سرنخ | `SearchIdentity, QualifyLead, FindIdentityById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Identity-2.pdf) (`84e71666150822328c181584`) |
| Inventory.pdf | موجودی | `GetRemainingStock` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2021/04/Inventory.pdf) (`d42cf70f66e98fbcc18bfa41`) |
| Invoice.pdf | فاکتور و پیش‌فاکتور | `SaveInvoice, SearchInvoice, FindInvoiceById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Invoice.pdf) (`caccd00979294756d27e70a1`) |
| MoneyAccount.pdf | حساب مالی | `GetMoneyAccountList, GetMoneyAccount` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/MoneyAccount.pdf) (`a4d22e450e586addbf8a4ebe`) |
| Opportunity-1.pdf | فرصت | `SaveOpportunity, SearchOpportunity, FindOpportunityById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Opportunity-1.pdf) (`8bcbbd16061e903fdd7b71e8`) |
| Organization.pdf | هویت حقوقی | `SearchOrganization, SaveOrganization, FindOrganizationById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Organization.pdf) (`925a87ea962a9531f11a053f`) |
| Person.pdf | هویت حقیقی | `SearchPerson, SavePerson, FindPersonById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Person.pdf) (`0405f1f811e66b1bb6f82a06`) |
| PhoneLog.pdf | ثبت تماس | `SearchPhoneLog, FindPhoneLogById, DeletePhoneLogById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/PhoneLog.pdf) (`fe369c5ae9de2cbcf7936298`) |
| PriceList.pdf | لیست قیمت | `SavePriceList, DeletePriceList` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2021/04/PriceList.pdf) (`acb65ce9b325cb2b56d5793f`) |
| ProcessEngine.pdf | موتور فرآیند | `Start, Next, Continue` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2021/04/ProcessEngine.pdf) (`0e59117f7b6cc9b9f6286d00`) |
| product.pdf | محصولات | `SaveProduct, FindProductByCode, GetProductBySerialNumber` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/07/product.pdf) (`6d625f4747e3bcf27ec27bd1`) |
| Receipt-payment.pdf | دریافت و پرداخت | `SearchReceipt, SearchPayment, FindReceiptByNumber` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Receipt-payment.pdf) (`2a4b10c093469be643f1114b`) |
| Task.pdf | وظیفه | `SaveTask, SearchTask, FindTaskById` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2023/08/Task.pdf) (`c4f192ba5b4f46d7b2b2d96c`) |
| Ticket.pdf | درخواست پشتیبانی | `SaveTicket, SearchTicket, GetHistoryByTicketId` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2021/04/Ticket.pdf) (`739203a54db20a7b9a2a571d`) |
| Users.pdf | کاربران | `GetUser, GetUserList, GetUserByExtension` | [مرجع](https://developer.payamgostar.com/wp-content/uploads/2021/04/Users.pdf) (`f01c9c5d621ba0226953e38e`) |

## احراز هویت و نشانی‌ها

- وجود REST نیز در دامنه مشخص مستند است: [یادداشت ۲.۸.۷.۱](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.7.1.md) (`repo-e008ded2ea8a6443`) از find فرصت و افزوده‌شدن Create/Delete/Update در REST سخن می‌گوید؛ [یادداشت ۲.۸.۵](https://github.com/1stco/PayamGostarDocs/blob/e6143c66b1746f251ae840745e7fe070607aee10/releasenote/ReleaseNote2.8.5.md) (`repo-6df871bd1dd7f281`) انتقال فیلدهای لیستی با REST را بیان می‌کند. محصول را صرفاً SOAP معرفی نکن. این شواهد، REST بودن Authentication/SaveInvoice، OAuth2 یا پوشش همه موجودیت‌ها را ثابت نمی‌کنند.

- مستندات صفحه توسعه‌دهندگان SOAP نام‌گذاری شده‌اند. پشتیبانی REST/OAuth2/JWT را فقط از وجود Authentication یا نمونه Node.js/PHP نتیجه نگیر. زبان client، نوع پروتکل را تعیین نمی‌کند.
- در PDF احراز هویت، نشانی نمونه `/Services/IAuthentication.svc` است؛ در PDF Invoice الگوی `/services/api/iinvoice.svc` دیده می‌شود. نشانی یک سرویس را با تغییر نام موجودیت برای سرویس دیگر تولید نکن. دامنه و HTTPS نصب مشتری را از تنظیمات و WSDL واقعی بگیر.
- در `AuthenticateUsernameAndPassword` ورودی حساب فراخوان با حساب مورد اعتبارسنجی متفاوت است: `username`, `password`, `userNameToValidate`, `passwordToValidate`. حروف و امضای نسخه واقعی را بازبینی کن. این متد در سند برای اعتبارسنجی حساب توصیف شده است، نه مدرک ورود یکپارچه سازمانی.
- `SaveInvoice` در صفحه ۷ فایل PDF (شماره چاپی ۱) ورودی‌های `userName`, `password`, `invoiceInfo` دارد. `InvoiceInfo` و فیلدهای مرتبط را از ادامه همان سند بخوان؛ این نمونه به همه سرویس‌ها تعمیم‌پذیر نیست.
- نمونه رسمی C#، WCF و فایل‌های WSDL/XSD مربوط به Person و Form دارد. نمونه PHP و Node.js مربوط به Person نیز در مخزن پیوندشده از سایت وجود دارند؛ این‌ها شاهد الگوی مصرف سرویس هستند، نه فهرست همه APIهای محصول.

## کیفیت منابع و استفاده از نمونه‌ها

- نسخه سند PDF با نسخه محصول یک چیز نیست. بسیاری از تاریخ‌های PDF قدیمی‌تر از آخرین Release Notes هستند. روش‌های جدید ممکن است در PDF منعکس نشده باشند.
- در Appointment اشاره‌ای به نام متد مرتبط با Invoice و املای متفاوت برخی نام‌ها دیده می‌شود. نام‌های مشابه یا عبارات ناسازگار را خودسرانه تصحیح نکن؛ متن متد، نمونه کد و WSDL نصب را تطبیق بده.
- استخراج متن PDF می‌تواند ترتیب ستون‌های فارسی و انگلیسی را جابه‌جا کند. هنگام ابهام در نام پارامتر، نوع، اجباری بودن یا عدد، صفحه را رندر و تصویر جدول را بررسی کن.
- مثال‌های عمومی ممکن است آدرس محلی و credential نمایشی داشته باشند. در کد پیشنهادی از جای‌نگهدار و تنظیمات امن استفاده کن؛ داده واقعی یا حساب نمونه را به محیط مشتری اعمال نکن.
- نبود نام متد در این جدول کوتاه، نبود آن متد در سند را ثابت نمی‌کند. فهرست کامل را از همان PDF و WSDL بخوان.
