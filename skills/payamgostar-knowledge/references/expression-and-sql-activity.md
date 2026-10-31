# Expression و فعالیت اجرای دستورات پایگاه‌داده (تخصیص داده پیشرفته)

مرجع کامل «کوئری زدن در فرایند» پیام‌گستر: خواندن مقدار یک فیلد از جای دیگر (از دیتابیس خود پیام‌گستر یا یک دیتابیس SQL Server دیگر) و ریختن آن در فیلد آیتمِ تحت فرایند، یا نوشتن داده در دیتابیس دیگر.

**منابع:** جزوه رسمی «Custom Expression و فعالیت اجرای دستورات پایگاه داده» (انتشار ۱۴۰۰/۰۵/۱۸، ۴۶ صفحه، متن و همه تصویرها خوانده شد) + مقاله‌های مرکز دانش در `kb/Help-Settings-Personalization-crm-Overview-Process-design.md` («تخصیص مقدار پیشرفته با استفاده از expression»، «نوشتن expression برای تخصیص مقدار پیشرفته» 2.8.x، «راهنمای استفاده از Custom Expression در فرآیند» 2.7.5.3 و 2.8.7، «نحوه نوشتن دستورات Expression» 2.7.0، «فعالیت اجرای دستورات پایگاه‌داده» و نسخه 2.8.7، «فعالیت تخصیص مقدار»، «فعالیت تصمیم چند شرطی») + Release Noteهای 2.6.0 تا 2.8.7.
**تصویرها:** `expression-images/` (آناتومی دستور، نمودار روابط جدول‌ها، سه صفحه فعالیت SQL).
**ساخت عملی در فرایند:** اسکیل `payamgostar-bpms-builder`، فایل `references/expression-sql-howto.md` و اسکریپت `scripts/check_expression.py`.

---

## ۱. خلاصه در یک نگاه
| موضوع | پاسخ کوتاه |
|---|---|
| چیست؟ | دستورهایی شبیه LINQ در #C که در طول فرایند از دیتابیس پیام‌گستر مقدار می‌خوانند و در فیلد «مقصد» می‌ریزند |
| کجا نوشته می‌شود؟ | سه فعالیت سیستمی فرایند: **تخصیص مقدار** (چک‌باکس «اعمال» + «عبارت»)، **تصمیم چند شرطی** (چک‌باکس «عبارت» در شرط)، **اجرای دستورات پایگاه‌داده** (SQL Activity) |
| شکل کلی | `@(Expression);` و در فعالیت SQL: `SELECT @(Expression);` |
| خواندن از دیتابیس دیگر | فقط در فعالیت «اجرای دستورات پایگاه‌داده» با «اتصال به پایگاه داده دیگر»؛ فقط **Microsoft SQL Server**، با رشته اتصال |
| نوشتن در دیتابیس دیگر | همان فعالیت با دستور SQL (مثلاً `UPDATE`)؛ Expression داخل دستور جایگذاری می‌شود |
| ماژول | «تخصیص داده پیشرفته (اجرای دستور پایگاه داده، Expression)»، پیش‌نیاز: مدیریت چرخه‌های کاری + BPMS (ر.ک. بخش ۲ و C58) |
| از چه نسخه‌ای | 2.6.0 (فعالیت SQL و Expression در تخصیص مقدار و چندشرطی)؛ دامنه آیتم‌ها تا 2.8.7 گسترش یافت (بخش ۴) |
| SQL Server توصیه‌شده | نسخه **2017 به بالا** |

---

## ۲. ماژول، ویرایش و نسخه
- **ماژول:** در تعرفه سایت (`pricing.md`): «تخصیص داده پیشرفته (اجرای دستور پایگاه داده، Expression)» ۲۳٬۰۰۰٬۰۰۰ تومان، پیش‌نیاز **BPMS**؛ در لوکال پیشرفته «بسته تخصیص داده پیشرفته» ۵۲٬۰۰۰٬۰۰۰ با پیش‌نیاز «فرایندهای پیشرفته». در فهرست امکانات نسخه **پیشرفته**: «یکپارچه‌سازی پیشرفته پایگاه داده (SQL در فرایند) و Expression».
- Release Note 2.6.0: استفاده از Expression در تخصیص مقدار و چندشرطی «نیازمند ماژول **امکانات پیشرفته BPMS**» است.
- KB (مقاله تخصیص مقدار پیشرفته): «فقط در **نسخه سازمانی** قابل استفاده می‌باشد».
- ⚠ **تناقض C58** (`conflicts.md`): KB می‌گوید «فقط نسخه سازمانی»، تعرفه آن را ماژول خریدنی کنار BPMS (و جزو امکانات پیشرفته) آورده. قاعده موقت: در پیشنهاد مشتری **ماژول «تخصیص داده پیشرفته» را با پیش‌نیاز BPMS** بیاور و برای ویرایش استاندارد بنویس «نیازمند تأیید تیم فروش»؛ «فقط سازمانی» را به مشتری نگو.
- همیشه همراه ادعا بیاور: ماژول (هزینه جدا)، نسخه نرم‌افزار (برای آیتم‌های تازه: 2.6.1، 2.7.1، 2.8.7)، و اینکه SQL Server 2017+ توصیه شده.

### سیر نسخه‌ها (از Release Note)
| نسخه | تغییر |
|---|---|
| 2.6.0 | فعالیت جدید «اجرای دستورات پایگاه‌داده» و Expression در تخصیص مقدار و چندشرطی؛ اعتبارسنجی فیلد Expression؛ جدول‌های تازه در کوئری‌ساز و الزامی شدن `order by` در کوئری‌ساز |
| 2.6.1 | Expression روی **دریافت و پرداخت** |
| 2.7.0 | اگر فیلد مقصد **متن** باشد، هم‌نوعی مبدأ و مقصد لازم نیست |
| 2.7.1 | Expression روی **فرصت** |
| 2.7.5.3 | **ItemKey** (کد زیرنوع) برای فیلدهای اضافه: `Field@ItemKey` |
| 2.8.7 | Expression روی **دریافت، پرداخت، قرارملاقات، تماس تلفنی**؛ از این نسخه روی **همه آیتم‌ها به‌جز رسید و حواله انبار** |

---

## ۳. مفاهیم پایه
- **آیتم جاری (This):** آیتمی که فرایند روی آن طراحی شده و الان در فرایند است. دستور همیشه با `this` شروع می‌شود.
- **مبدأ:** آیتم و فیلدی که مقدار از آن خوانده می‌شود. **مقصد:** فیلدی از آیتم جاری که پر می‌شود.
  - فرایند را روی آیتم **مقصد** بساز. مبدأ می‌تواند **هر آیتمی** باشد (حتی قرارملاقات و تراکنش انبار)؛ فقط مقصد محدود است.
- **چهار نسبت مبدأ با آیتم جاری:**
  1. **خود آیتم:** `@(this.Select(Subject));`
  2. **هویت مرتبط (Identity):** `@(this.Select(Identity.Mobile));` (برای هویت `Parent` لازم نیست)
  3. **سابقه‌ها (Children):** آیتم‌هایی که از روی آیتم جاری و متصل به آن ثبت شده‌اند: `@(this.Select(Children.Quote.Number));`
  4. **پدر (Parent):** آیتمی که آیتم جاری در سوابق آن ثبت شده: `@(this.Select(Parent.Opportunity.Subject));`
- **زنجیره پدر و فرزند:** اگر از روی فرصت پیش‌فاکتور و از روی آن فاکتور ثبت شود: `فرصت > پیش‌فاکتور > فاکتور`. فاکتور فرزندِ پیش‌فاکتور **و** فرصت است؛ فرصت پدرِ پیش‌فاکتور و فاکتور است.
- `Children` و `Parent` را می‌توان بعد از `this` یا داخل `Where` نوشت؛ فرقی ندارد (`this.Children.Select(Ticket.EmailAddress)` = `this.Select(Children.Ticket.EmailAddress)`).
- **اولین سابقه:** بدون مرتب‌سازی یا شرط، `Children` «اولین سابقه‌ای که **یافت شود**» را برمی‌گرداند، **نه** قدیمی‌ترین یا جدیدترین. هر جا ممکن است چند سابقه از یک نوع باشد، `Order`/`OrderDes` + `Take` یا `Where` بگذار.

---

## ۴. کدام آیتم‌ها مقصد Expression می‌شوند (به تفکیک نسخه)
| آیتم | جزوه ۱۴۰۰ و KB 2.7.0 | تخصیص مقدار (KB) | 2.8.x (مقاله تخصیص پیشرفته) | 2.8.7 |
|---|---|---|---|---|
| فرم، هویت، وظیفه، درخواست پشتیبانی | ✓ | ✓ | ✓ | ✓ |
| پیش‌فاکتور، فاکتور، فاکتور برگشت (خرید و فروش) | ✓ | ✓ | ✓ | ✓ |
| فرصت | ✗ (قرمز در نمودار) | ✓ (2.7.1) | ✓ | ✓ |
| دریافت و پرداخت | ✗ | ✓ (2.6.1) | — | ✓ |
| قرارداد | ✗ | — | ✓ | ✓ |
| قرارملاقات، تماس تلفنی | ✗ | — | — | ✓ |
| یادداشت، فایل | ✗ | — | — | مستند نشده |
| **رسید و حواله انبار** | ✗ | ✗ | ✗ | **✗ (استثنای صریح؛ فقط دستور SQL خام)** |

- در نمودار جزوه (`expression-images/table-relations.png`) آیتم‌های قرمز (Payment، Receipt، Contract، BusinessNote، PhoneLog، Opportunity، File، Appointment، Input/OutputInventoryTransaction) «در فعالیت‌های تخصیص مقدار و چند شرطی» قابل استفاده نبودند؛ نسخه‌های بعد بیشترشان را باز کرده‌اند. **ملاک: نسخه نرم‌افزار مشتری.**
- قدیمی (جزوه): در فعالیت SQL هم Expression فقط روی فرم، هویت، وظیفه، تیکت و فاکتورها؛ برای آیتم دیگر (مثلاً تماس) فقط SQL خام. 2.8.7: فقط رسید و حواله استثنا هستند.
- مقاله چندشرطی (نسخه قدیمی) هنوز فهرست محدود (فرم، هویت، وظیفه، تیکت، فاکتورها) را می‌گوید؛ برای نسخه ≥2.8.7 روی دمو تست کن.

---

## ۵. نوع فیلد مقصد و قاعده هم‌نوعی
**فیلدهای قابل مقداردهی با Expression** (مقصد، و فیلد اضافه قابل انتخاب به‌عنوان «پارامتر خروجی» فعالیت SQL):
Html · پول · تاریخ شمسی · تاریخ میلادی · چک‌باکس · ساعت · عدد · متن · کاربر · گروه · لینک · شرکت/شخص.

قواعد:
1. در تخصیص مقدار و چندشرطی **نوع مبدأ و مقصد باید یکسان** باشد (نوع فیلدهای پیش‌فرض در ستون «نوع فیلد» جدول‌های بخش ۱۲ آمده).
2. از **2.7.0**: اگر مقصد **متن** باشد، نوع مبدأ مهم نیست.
3. مبدأ **لیست کشویی (مشخصه/Index)** ← مقصد را **متن** بگذار؛ فقط **شماره ردیف گزینه (Index)** منتقل می‌شود. برای متن گزینه: پس از آن یک **چندشرطی** روی همان فیلد + برای هر Index یک **تخصیص مقدار** با متن ثابت.
4. مبدأ کاربر (`CreatorId`، `AssignedToId`، `RelatedUserIdSales`…) ← مقصد **کاربر**. در فیلد متن، Id کاربر می‌نشیند که به درد کاربر نمی‌خورد.
5. پول ← پول، تاریخ شمسی ← تاریخ شمسی، عدد ← عدد. `Probability`، `DiscountPercent` و `PercentCompleted` عدد هستند، نه پول.

---

## ۶. نحو (Syntax)
### کلیدواژه‌ها
| کلیدواژه | کار |
|---|---|
| `this` | آیتم جاری؛ ابتدای هر دستور |
| `Select(...)` | فیلد خروجی |
| `Identity` | هویت مرتبط با آیتم جاری |
| `Children` | سوابق آیتم جاری (پیش‌فرض: اولین سابقه یافت‌شده) |
| `Parent` | آیتم پدر |
| `Where(...)` | شرط |
| `Order(...)` | مرتب‌سازی **صعودی** (روی تاریخ: اول = **قدیمی‌ترین**) |
| `OrderDes(...)` | مرتب‌سازی **نزولی** (روی تاریخ: اول = **جدیدترین**) |
| `Take(n)` | ردیف nام از نتایج مرتب‌شده |
| `TakeOrDefault(n,"x")` | ردیف nام؛ اگر نبود، مقدار پیش‌فرض `x` |
| `&&` و `\|\|` | «و» و «یا» بین شرط‌ها؛ پرانتز برای گروه‌بندی |
| `==`، `>`، `>=`، `<`، `<=` | مقایسه (در مثال‌ها `==` و `>` و `>=` و `<=` آمده) |
| `Convert.ToDateTime("2020-08-31")` | ثابت تاریخ میلادی برای مقایسه |
| `Type.Code` | کد زیرنوع آیتم، مثلاً `Children.Type.Code=="FR123"` |
| `BillableObjectTypeindex` | نوع آیتم مالی: **8 = فاکتور برگشت از فروش**، **7 = فاکتور برگشت از خرید** (زیر `Children.Invoice`) |

### قالب کلی (KB 2.8.x)
```
@(this.Select(نسبت.نام‌جدول.کلیدفیلدپیش‌فرض));
@(this.Select(نسبت.نام‌جدول.کلیدفیلداضافه@کدزیرنوع));
```
- **نسبت:** `Identity` / `Parent` / `Children`؛ برای خود آیتم حذف می‌شود.
- **نام جدول:** نام انگلیسی جدول (بخش ۱۲): `Form`، `Opportunity`، `Quote`، `Invoice`، `Ticket`، `Task`، `Contract`، `Appointment`، `PhoneLog`، `Receipt`، `Payment`… برای `Identity` لازم نیست.
- **کلید فیلد پیش‌فرض:** از جدول‌های بخش ۱۲ یا از بخش **کوئری‌ساز** پیام‌گستر.
- **کلید فیلد اضافه:** «کلید کاربر» که هنگام ساخت فیلد در شخصی‌سازی تعیین شده.
- **کد زیرنوع (ItemKey):** فقط برای فیلد اضافه؛ در صفحه شخصی‌سازی همان زیرنوع (کد نوع / کلید کاربر آیتم). از 2.7.5.3.
- **حروف کوچک و بزرگ مهم است** (`Select`، `OrderDes`، `CreateDate`). مثال‌های رسمی گاهی `SELECT` یا `children` نوشته‌اند؛ امن‌ترین شکل همان شکل جدول‌هاست.
- **کلید فیلدها و موجودیت‌ها باید یکتا باشند.**

### آناتومی یک دستور کامل (تصویر `expression-images/expression-anatomy.png`)
```
@(this.Where(Children.Form.Subject=="فرم شکایت").Select(Children.Form.Email).Order(Children.Form.CreateDate).TakeOrDefault(1,"none"));
```
| بخش | نام در جزوه |
|---|---|
| `this` | آیتم جاری |
| `Children` | مسیر دسترسی به موجودیت |
| `Form` | نام جدول |
| `Subject` / `Email` / `CreateDate` | کلید فیلد |
| `Where(...=="فرم شکایت")` | شرط |
| `Select(...)` | انتخاب فیلد برای نمایش در خروجی |
| `Order(...)` | مرتب‌سازی نتایج؛ داخلش کلید فیلد مبنای مرتب‌سازی |
| `TakeOrDefault(1, ...)` | انتخاب ردیف nام از نتایج مرتب‌شده + خروجی پیش‌فرض |

> تصویر جزوه مقدار پیش‌فرض را «ندارد» (فارسی) نوشته، ولی KB 2.8.x صریحاً می‌گوید پیش‌فرض باید **متن انگلیسی یا عدد** باشد و فارسی نمایش داده نمی‌شود. همیشه انگلیسی یا عدد بنویس.

### قالب مرتب‌سازی (KB 2.8.x، تصویر `expression-template-for-order-2.8.0`)
```
@(this.Select(Children.Item.SourceField[@ItemKey]).Order|OrderDes(Children.Item.SortField[@ItemKey]).Take(n));
```
`@ItemKey` اول فقط اگر فیلد مبدأ اضافه باشد؛ `@ItemKey` دوم فقط اگر فیلد مبنای مرتب‌سازی اضافه باشد.

### فیلد اضافه از نوع «آیتم CRM» (مرجع به آیتم دیگر)
نوع آیتم را بعد از کلید فیلد بنویس:
```
@(this.frmk@myformtype.Form.Select(customerno@otherformtype));
@(this.Select(frmk@myformtype.Form.customerno@otherformtype));   ← معادل
```
(فیلد `frmk` از نوع فرم در آیتم جاری با زیرنوع `myformtype`؛ فیلد `customerno` در فرمی با زیرنوع `otherformtype`.) نسخه‌های پیش از 2.7.5.3 همین را بدون `@` می‌نوشتند: `@(this.frmk.Form.Select(customerno));`.

**محدودیت:** در تخصیص مقدار و چندشرطی فقط از **آیتم جاری، سوابق آن و پدر آن** می‌توان خواند. اگر یک **سابقه** فیلدی از نوع آیتم CRM داشته باشد، فقط خود آن آیتم را می‌توان خواند، نه فیلدهای درونش (یک سطح عمیق‌تر ممنوع). فیلد مرجع روی **خود آیتم جاری** (مثال بالا) مجاز است.

---

## ۷. کتابخانه دستورها (همه مثال‌های رسمی)
| # | نیاز | دستور | مقصد |
|---|---|---|---|
| 1 | عنوان آیتم جاری | `@(this.Select(Subject));` | متن |
| 2 | ایجادکننده آیتم | `@(this.Select(CreatorId));` | کاربر |
| 3 | موبایل هویت مرتبط | `@(this.Select(Identity.Mobile));` | متن |
| 4 | ایمیل هویت (شکل قدیمی) | `@(this.Identity.Select(Email));` | متن |
| 5 | فیلد اضافه هویت (رشته تحصیلی، زیرنوع مخاطب حقیقی `Hoviat`) | `@(this.Select(Identity.Major1@Hoviat));` | متن |
| 6 | فیلد اضافه هویت (شکل دیگر) | `@(this.Identity.Select(pphali@typeali));` | هم‌نوع |
| 7 | عنوان فرصتِ پدر (روی فاکتور) | `@(this.Select(Parent.Opportunity.Subject));` | متن |
| 8 | فیلد اضافه فرصت پدر (تاریخ پیشنهادی تحویل) | `@(this.Select(Parent.Opportunity.DeliveryDate@SalesOpportunity));` | تاریخ |
| 9 | مبلغ محقق‌شده فرصت پدر | `@(this.Parent.Select(Opportunity.RealizedValue));` | پول |
| 10 | شماره پیش‌فاکتور سابقه (روی فرصت) | `@(this.Select(Children.Quote.Number));` | متن |
| 11 | فیلد اضافه پیش‌فاکتور سابقه (نحوه تسویه) | `@(this.Select(Children.Quote.SettlementTerms@SalesOpportunity));` ⚠ | متن |
| 12 | ایمیل تیکت سابقه | `@(this.Select(Children.Ticket.EmailAddress));` | متن |
| 13 | توضیحات **قدیمی‌ترین** تیکت | `@(this.Select(Children.Ticket.Description).Order(Children.Ticket.CreateDate).Take(1));` | Html |
| 14 | توضیحات **جدیدترین** تیکت | `@(this.Select(Children.Ticket.Description).OrderDes(Children.Ticket.CreateDate).Take(1));` | Html |
| 15 | فیلد اضافه قدیمی‌ترین تیکت | `@(this.Select(Children.Ticket.FirstResult@CustomerTicket).Order(Children.Ticket.CreateDate).Take(1));` | هم‌نوع |
| 16 | مرتب‌سازی روی فیلد اضافه | `@(this.Select(Children.Ticket.Result@CustomerTicket).OrderDes(Children.Ticket.EndDate@CustomerTicket).Take(1));` | هم‌نوع |
| 17 | دومین تیکت از آخر، با پیش‌فرض | `@(this.Select(Children.Ticket.Description).OrderDes(Children.Ticket.CreateDate).TakeOrDefault(2,"Only one ticket"));` | متن |
| 18 | عنوان سومین فرم، اگر نبود 0 | `@(this.Select(Children.Form.Subject).Order(Children.Form.CreateDate).TakeOrDefault(3,"0"));` | متن |
| 19 | تاریخ پایان قرارداد «نمایندگی» | `@(this.Where(Children.Contract.Subject=="نمایندگی").Select(Children.Contract.EndDate));` | تاریخ |
| 20 | توضیحات پیش‌فاکتورِ دارای تخفیف | `@(this.Where(Children.Quote.Discount>0).Select(Children.Quote.Description));` | Html |
| 21 | فیلد فرمِ سابقه با عنوان مشخص | `@(this.Where(Children.Form.Subject=="فرم دوم").Select(Children.Form.polformat@typeb));` | هم‌نوع |
| 22 | شرط عددی روی فیلد اضافه | `@(this.Where(Children.Form.number == 99).Select(Children.Form.polformat@typeb));` | هم‌نوع |
| 23 | شرط «یا» | `@(this.Where(Children.Form.number == 670 \|\| Children.Form.poljoin == 400).Select(Children.Form.polformat));` | هم‌نوع |
| 24 | ترکیب «و» و «یا» | `@(this.Children.Form.Where(Children.Form.npfali@mytype1==90&&(Children.Form.poljoin@mytype1 == 30\|\|Children.Form.numfirst@mytype1==18)).Select(Children.Form.polformat@mytype1));` | هم‌نوع |
| 25 | بازه تاریخ ویرایش | `@(this.Where(Children.Form.ModifyDate >= Convert.ToDateTime("2020-08-31") && Children.Form.ModifyDate <= Convert.ToDateTime("2020-09-01")).Select(Children.Form.polformat));` | هم‌نوع |
| 26 | فیلد فرم با زیرنوع FR123 | `@(this.Select(Children.Form.polformat@FR123));` (2.8.x) یا `@(this.Where(Children.Type.Code == "FR123").Select(Children.Form.polformat));` (قدیمی) | هم‌نوع |
| 27 | مبلغ نهایی فاکتور برگشت از فروش سابقه | `@(this.Where(Children.Invoice.BillableObjectTypeindex == 8).Select(Children.Invoice.FinalValue));` | پول |
| 28 | مبلغ نهایی فاکتور برگشت از خرید سابقه | `@(this.Where(Children.Invoice.BillableObjectTypeindex == 7).Select(Children.Invoice.FinalValue));` | پول |
| 29 | ایمیل آخرین «فرم شکایت» با پیش‌فرض | `@(this.Where(Children.Form.Subject=="فرم شکایت").Select(Children.Form.Email).OrderDes(Children.Form.CreateDate).TakeOrDefault(1,"none"));` | متن |

⚠ ردیف 11: KB برای فیلد پیش‌فاکتور کد زیرنوع **فرصت** (`SalesOpportunity`) را آورده؛ منطقاً باید کد زیرنوع **آیتم مبدأ** (پیش‌فاکتور) باشد (قاعده ردیف ۱۵ و ۱۶). کد زیرنوعِ آیتمی را بگذار که فیلد در آن ساخته شده و روی دمو تست کن.

---

## ۸. فعالیت تخصیص مقدار با Expression
- فیلد را با چک‌باکس **«اعمال»** فعال کن، سپس **«عبارت»** را تیک بزن و دستور را در کادر همان فیلد بنویس.
- اگر «اعمال» فعال و مقدار خالی باشد، فیلد **خالی** می‌شود.
- **کادر قرمز** پس از ورود یا ذخیره = دستور نادرست. **آبی شدن** = نحو قابل‌قبول، **نه** درستی قطعی. فقط اجرای آزمایشی درستی را ثابت می‌کند.
- توصیه KB: دستور را در Notepad بنویس و بعد بچسبان (جلوگیری از به‌هم‌ریختگی جهت متن فارسی).
- همین فعالیت «ثبت لحظه تخصیص» هم دارد (تاریخ و ساعت اجرای فعالیت در فیلد تاریخ/ساعت) که Expression نمی‌خواهد.

## ۹. فعالیت تصمیم چند شرطی با Expression
- همه شرط‌ها روی **یک فیلد** هستند؛ پس از تعریف اولین شرط، فیلد شرط قفل می‌شود.
- در هر شرط: عنوان، عملگر/مقدار، و با تیک **«عبارت»** می‌توان مقدار مقایسه را با Expression ساخت؛ سپس حالت بعدی.
- «حالت پیش‌فرض» (هیچ شرطی برقرار نیست) و «حالت بعدی در صورت خطا» را حتماً تعیین کن.
- نوع فیلد شرط باید با نوع مبدأ یکسان باشد.

---

## ۱۰. فعالیت اجرای دستورات پایگاه‌داده (SQL Activity)
**هدف:** انتقال داده از پیام‌گستر به بانک‌های اطلاعاتی دیگر و برعکس، با نوشتن کوئری.

**مسیر:** تنظیمات ← شخصی‌سازی CRM ← نمای کلی ← ویرایش چرخه کاری ← فعالیت جدید ← نوع عملیات «**اجرای دستورات پایگاه داده**» (تصویر `sql-activity-new.png`؛ کنار «تخصیص مقدار»، «تصمیم چند شرطی»، «فراخوانی سرویس» و…).

**تنظیمات:**
| گزینه | توضیح |
|---|---|
| «پایگاه داده پیام‌گستر» | رشته اتصال لازم نیست؛ فقط «دستور» |
| «اتصال به پایگاه داده دیگر» | «نوع پایگاه داده»: فعلاً فقط **Microsoft SQL Server**؛ «رشته‌ی اتصال»؛ دکمه **«تست»** (پیام موفقیت اتصال) |
| رشته اتصال | `Data Source:<آدرس سرور SQL>;Initial Catalog:<نام دیتابیس>;user id:<نام کاربری SQL>; Password:<رمز>` (عیناً شکل تصویر KB؛ رمز را هیچ‌جا ذخیره یا مستند نکن) |
| «دستور» | ویرایشگر کد؛ SQL خام و/یا Expression |
| «خروجی دارد» + «پارامتر خروجی» | نتیجه در فیلد انتخاب‌شده آیتم جاری ریخته می‌شود. **بدون تیک:** هیچ فیلدی از آیتم جاری پر نمی‌شود و داده طبق کوئری به آیتم دیگر یا دیتابیس دیگر منتقل می‌شود |
| «حالت بعدی در صورت اجرای موفق» / «در صورت خطا» | هر دو الزامی (ستاره‌دار) |

**Expression در این فعالیت:** `SELECT @(Expression);` — مثلاً `SELECT @(this.Select(Children.Contract.FinalValue));`
- جزوه: Expression در فعالیت SQL فقط روی فرم، هویت، وظیفه، تیکت و فاکتورها؛ برای آیتم دیگر فقط SQL خام. 2.8.7: همه‌جا به‌جز **رسید و حواله** (برای این دو فقط SQL).
- در این فعالیت **همه جدول‌ها** (InvoiceDetail، Product، User، AppointmentAttendant…) قابل استفاده‌اند؛ در تخصیص مقدار و چندشرطی این جدول‌ها فقط داخل `Where`.
- توصیه رسمی: SQL Server **2017 به بالا**.

**نمونه‌های رسمی:**
```sql
SELECT @(this.Select(Subject));                         -- عنوان آیتم جاری ← پارامتر خروجی
SELECT @(this.Identity.Select(Email));                  -- ایمیل هویت مرتبط
SELECT @(this.Select(mtn));                             -- فیلد اضافه متنی با کلید mtn
SELECT @(this.Select(Children.Contract.FinalValue));    -- مبلغ نهایی اولین قرارداد سابقه
SELECT @(this.Where(Children.Ticket.Subject=="ایمپورت").Select(Children.Ticket.EmailAddress));

-- نوشتن در دیتابیس دیگر (اتصال به پایگاه داده دیگر، بدون «خروجی دارد»):
update [Products] set [ProductName] =
@(this.Select(Subject));
Where productId='9DC87DFA-0F80-49BE-956B-70D974FB1F77'
```
(متن KB نمونه سوم را `SELECT @(this.Select(mtn)(;` چاپ کرده که غلط تایپی است.)

**آنچه مستند نیست (پیش از قول به مشتری روی محیط آزمون تست شود):**
- اگر کوئری چند ردیف یا چند ستون برگرداند، کدام مقدار در پارامتر خروجی می‌نشیند (منطقاً ستون اول ردیف اول؛ تأیید نشده).
- Expression داخل SQL به‌صورت پارامتر جایگذاری می‌شود یا متن (نقش کوتیشن و `;` در نمونه `update`).
- Timeout، تراکنش، و رفتار هنگام قطع بودن دیتابیس مقصد (فقط «حالت بعدی در صورت خطا» مستند است).
- پشتیبانی از Stored Procedure و چند دستور پشت سر هم.

**پارامتر خروجی؛ فیلدهای پیش‌فرض قابل انتخاب (جزوه):**
| آیتم | فیلدها |
|---|---|
| دریافت/پرداخت | مبلغ نهایی، کد شعبه، شماره کارت دریافت، شماره پیگیری، توضیحات، شماره چک، تاریخ رسید |
| پیش‌فاکتور خرید/فروش | تاریخ صدور، تاریخ انقضا، توضیحات، اضافات، مبلغ تخفیف، مالیات، عوارض |
| فاکتور خرید/فروش و برگشتی‌ها | تاریخ صدور، توضیحات، اضافات، مبلغ تخفیف، مالیات، عوارض |
| تماس تلفنی | عنوان، مکالمه با، مدت تماس، توضیحات، زمان تماس |
| یادداشت | عنوان، توضیحات |
| وظیفه | عنوان، درصد تکمیل، تاریخ شروع، موعد مقرر، توضیحات |
| قرارملاقات | عنوان، تاریخ شروع، موعد مقرر (تاریخ پایان)، آدرس، توضیحات، طول و عرض جغرافیایی |
| قرارداد | عنوان، تاریخ شروع، تاریخ پایان، مبلغ نهایی |
| فرم | عنوان |
| درخواست پشتیبانی | توضیحات |
| فرصت | عنوان، تاریخ بسته شدن، مسئول، مبلغ نهایی، احتمال موفقیت، تاریخ موفقیت، تاریخ شکست، مبلغ تخفیف، مبلغ کل |
| مخاطب حقوقی | نام تجاری، ایمیل پیش‌فرض، مسئول پشتیبانی، مسئول فروش، مسئول سایر، تاریخ مشتری شدن، توضیحات، شماره ثبت، کد اقتصادی |
| مخاطب حقیقی | نام، نام خانوادگی، ایمیل پیش‌فرض، وب‌سایت، تاریخ مشتری شدن، مسئول فروش، پشتیبانی و سایر، توضیحات، کد ملی |
| فیلد اضافه | Html، پول، تاریخ شمسی، تاریخ میلادی، چک‌باکس، ساعت، عدد، کاربر، گروه، لینک، متن، شرکت/شخص |

---

## ۱۱. محدودیت‌ها و قواعد (چک‌لیست)
1. Expression فقط در سه فعالیت: تخصیص مقدار، تصمیم چند شرطی، اجرای دستورات پایگاه‌داده.
2. مقصد فقط آیتم‌های بخش ۴ (به نسخه مشتری بستگی دارد)؛ رسید و حواله هرگز (فقط SQL خام).
3. در تخصیص مقدار و چندشرطی: فقط آیتم جاری، سوابق و پدر؛ داخل فیلدِ آیتم‌CRM یک سابقه نمی‌شود رفت.
4. در تخصیص مقدار و چندشرطی، `Select` فقط فیلدهای موجودیت‌های CRM؛ جدول‌های InvoiceDetail، InvoiceDetailProductItem، ProductItem، Product، User، AppointmentAttendant فقط در `Where`. در فعالیت SQL همه جدول‌ها آزادند.
5. نوع مبدأ = نوع مقصد (مگر مقصد متن، از 2.7.0). لیست کشویی فقط Index می‌دهد.
6. حساس به حروف کوچک و بزرگ؛ کلیدها یکتا.
7. `TakeOrDefault`: پیش‌فرض انگلیسی یا عدد.
8. چند سابقه از یک نوع ← حتماً `Order`/`OrderDes`+`Take` یا `Where`.
9. فاکتور برگشت در نسخه جزوه مستقیم پشتیبانی نمی‌شد؛ از `Children.Invoice` با `BillableObjectTypeindex` 8 یا 7.
10. خواندن و نوشتن در دیتابیس دیگر فقط با فعالیت SQL و فقط SQL Server.
11. جزوه: «قابلیت Expression در حال بهبود و توسعه است» ← رفتار را روی نسخه مشتری تست کن.
12. برای کلید فیلدهای پیش‌فرض به **کوئری‌ساز** (بخش گزارش‌ساز) مراجعه کن؛ از 2.6.0 جدول‌های تازه دارد و `order by` در آن الزامی است.

13. **فیلد تصویر و فایل** در فهرست مقصدهای Expression نیست. در فعالیت تخصیص مقدار فقط فایل ثابت می‌گیرد (دمو 2.8.8.2). کپی عکس از آیتم دیگر مستند نیست؛ مسیرهای جایگزین: فیلد مرجع از نوع «فرم» برای دیدن عکس در فرم مبدأ، یا راهکار سفارشی (SQL یا وب‌سرویس) که **نیازمند تأیید تیم فنی** است.
14. فیلد **«لیست آیتم سی آر ام»** در فعالیت تخصیص مقدار به‌عنوان مقصد دیده نمی‌شود (دمو 2.8.8.2). خواندن از آن به‌عنوان مبدأ (کدام آیتم لیست) **مستند نیست**؛ فقط فیلد تکی آیتم CRM مستند است.

## ۱۲. جدول تعاریف موجودیت‌ها (Property Definition)
نوع فیلد = PropertyDisplayName (برای قاعده هم‌نوعی). «مشخصه» یعنی لیست کشویی (Index).

**فیلدهای مشترک همه آیتم‌های CRM:**
| کلید | نوع | نام |
|---|---|---|
| AssignedToId | لیست کاربران | مالک |
| CreateDate | تاریخ شمسی | تاریخ ایجاد |
| CreatorId | لیست کاربران | ایجادکننده |
| CrmObjectTypeIndex | مشخصه | نوع آیتم |
| Description | Html | توضیحات |
| IdentityId | شرکت/شخص | مرتبط با (در هویت: `Id` متن، شناسه هویت) |
| ModifierId | لیست کاربران | ویرایش‌کننده |
| ModifyDate | تاریخ شمسی | تاریخ ویرایش |
| RefId | متن | شناسه مرجع |
| SourceCampaignId | کمپین تبلیغاتی | شناسه ارتباط با مشتری (نه در تماس تلفنی، وظیفه، قرارملاقات، فرم، رسید انبار) |
| StageChangeDate / StageChangedBy / StageId | تاریخ شمسی / لیست کاربران / مرحله | تاریخ تغییر مرحله / تغییردهنده / مرحله (نه در هویت، وظیفه، رسید و حواله انبار) |
| Subject | متن | عنوان |
| Summary | Html | خلاصه |
| PriorityIndex | مشخصه | اولویت (تیکت، قرارداد، فرم، فرصت، هویت، انبار) |

**نوع موجودیت (Type):** `Code` (متن، کد زیرنوع).

**دریافت (Receipt) / پرداخت (Payment):** ParentCrmObjectId (آیتم CRM، شناسه پدر)، ApproveDate (تاریخ)، ApproverId (کاربر)، NumberedById (کاربر)، NumberedDate (تاریخ)، FinalValue (پول، مبلغ نهایی)، Number (متن)، RejectDate (تاریخ)، RejectedById (کاربر)، RemainedValue (پول، باقیمانده)، IsPayed (چک‌باکس، پرداخت شده)، PayDate (تاریخ واریز)، PaymentMethodIndex (مشخصه، روش دریافت)، PaymentTypeIndex (مشخصه، نوع دریافت)، SettledDate (تاریخ سررسید)، BranchCode (متن، کد شعبه)، ChequeBankIndex (مشخصه، بانک)، ChequeNo (متن)، Receipt_CardNo (متن، شماره کارت)، RefNo (متن، شماره پیگیری).

**پیش‌فاکتور فروش (Quote) / خرید (PurchaseQuote):** ApproveDate، ApproverId، BillableObjectStateIndex (مشخصه، وضعیت آیتم مالی)، CreditValue (پول، بستانکاری)، DebitValue (پول، بدهکاری)، FinalValue (پول)، Number (متن)، NumberedById، NumberedDate، PaidValue (پول، پرداختی)، RejectDate، RejectedById، RemainedValue (پول)، AdditionalCosts (پول، اضافات)، Discount (پول، تخفیف)، DiscountPercent (عدد)، InvoiceDate (تاریخ فاکتور)، PriceListId (لیست قیمت)، Tax (پول، مجموع مالیات و عوارض)، TaxPercent (عدد)، Toll (پول، عوارض)، TollPercent (عدد)، TotalAmount (عدد، مقدار کل)، TotalValue (پول، مبلغ کل)، TotalValueWithDiscount (پول)، TotalValueWithTax (پول)، Vat (پول، مالیات)، VatPercent (عدد)، **ExpireDate** (تاریخ انقضا)، InvoiceDetailContainer (لیست اقلام فاکتور).

**فاکتور فروش (Invoice) / خرید (PurchaseInvoice) و فاکتور برگشت از فروش (ReturnSaleInvoice) / از خرید (ReturnPurchaseInvoice):** همان فیلدهای پیش‌فاکتور + **ReceivedValue** (پول، دریافتی)، بدون ExpireDate.

**تماس تلفنی (PhoneLog):** CallTypeIndex (مشخصه، نوع تماس)، Duration (مدت زمان، مدت مکالمه)، StartTime (ساعت شروع؛ در جدول «تاریخ شمسی»)، TalkedTo (متن، مکالمه با).

**یادداشت (BusinessNote):** فقط فیلدهای مشترک.

**وظیفه (Task):** DueDate (تاریخ سررسید)، PercentCompleted (عدد)، StartDate (تاریخ)، TaskStatusIndex (مشخصه، وضعیت).

**قرارملاقات (Appointment):** AppointmentStatus (مشخصه)، CalendarId (تقویم)، DueDate (تاریخ پایان)، EndTime (ساعت)، IsAllDay (چک‌باکس)، Latitude / Longitude (عدد)، Location (متن، مکان)، RoomId (اتاق)، StartDate (تاریخ)، StartTime (ساعت).

**درخواست پشتیبانی (Ticket):** EmailAddress (متن)، ImpactIndex (مشخصه، تأثیرگذاری)، Number (متن)، ResponseStatusIndex (مشخصه، پاسخ)، SeverityIndex (مشخصه، شدت)، StatusIndex (مشخصه، وضعیت).

**قرارداد (Contract):** فیلدهای مالی (Approve…، BillableObjectStateIndex، Credit/DebitValue، FinalValue، Number، Numbered…، Paid/Received/RemainedValue، Reject…) + EndDate (تاریخ پایان)، IsBillable (چک‌باکس، جنبه مالی دارد)، StartDate (تاریخ شروع).

**فرم (Form):** فقط فیلدهای مشترک (+ PriorityIndex).

**فرصت (Opportunity):** ClosedDateTime (تاریخ بسته شدن)، EstimatedValue (پول، برآورد)، FailDate، FinalValue (پول)، LostCauseIndex (مشخصه، دلیل شکست)، OppSourceTypeIndex (مشخصه، منبع)، OppStatusTypeIndex (مشخصه، وضعیت)، OppTypeIndex (مشخصه، نوع)، Probability (عدد)، PurchaseProcessIndex (مشخصه، پروسه خرید)، RealizedValue (پول، محقق‌شده)، SuccessDate، TotalDiscount (پول)، TotalDiscountPercent (عدد)، TotalValue (پول)، WonCauseIndex (مشخصه، دلیل موفقیت).

**هویت (Identity) ـ مخاطب حقوقی:** Id، AreaCode / AreaCodes، Balance (پول، مانده حساب)، City / Cities، ClassificationRuleId (کلاس مشتری)، ColorId (رنگ)، Country / Countries، CPFirstName / CPLastName / CPGender / CPMobiles (رابط)، CustomerDate (تاریخ مشتری شدن)، CustomerNo (شماره مشتری)، DetailAddress / DetailAddresses، EconomicCode، Email / Emails، Fax / Faxes، FullAddress / FullAddresses، ManagerFirstName / ManagerLastName / ManagerGender / ManagerMobiles، Mobile / Mobiles، RegisterNo، Registerdate، RelatedUserIdOther / RelatedUserIdSales / RelatedUserIdSupport (لیست کاربران، مسئول متفرقه/فروش/پشتیبانی)، Tel / Tels، TeleFax / TeleFaxes، TelephonyPassword، Website (لینک)، ZipCode / ZipCodes. (همه متن مگر اشاره شده.)

**هویت ـ مخاطب حقیقی:** همان (بدون CP*، Manager*، EconomicCode، RegisterNo) + FirstName، LastName، Gender، NationalCode (متن)، PersonPrefixIndex (مشخصه، پیشوند)، BirthDate (تاریخ تولد)، UserId (لیست کاربران).

**رسید انبار (EnterInventoryTransaction) / حواله انبار (ExitInventoryTransaction):** ApproveDate، ApproverId، AtfNumber (شماره عطف)، EnterCauseIndex / ExitCauseIndex (مشخصه)، InventoryId (انبار)، InventoryTransactionDetailContainer (اقلام)، InventoryTransactionTypeIndex (مشخصه)، InvoiceId (متن، فاکتور)، Number، ReceiverDesc (گیرنده)، SerialNumber، ShipperDesc، SrcDstInventoryId (انبار مقصد)، TotalValue (پول)، TransactionStatusIndex (مشخصه)، TransDate (تاریخ انتقال).

**جدول‌های غیر CRM (در تخصیص مقدار و چندشرطی فقط در Where؛ در SQL آزاد):**
- **User:** SecurityItemId، UserName، ActivationDate، CommissionPercent.
- **AppointmentAttendant (مدعوین قرارملاقات):** Id، AppointmentId، AttendantTypeIndex، UserId، IdentityId، NickName، Email، Mobile، Fax، RefCode، PresenceIsRequired.
- **Product:** Id، RefId، Name، Number، ProductGroupId، IsService، UnitPrice، LastPriceUpdate، ProductUnitTypeIndex، Description، CommissionPercent، LastEditDate، DoInventory (اعمال نقطه سفارش)، MinimumSupplyThreshold (نقطه سفارش)، DisplayIndex، UnitBuyPrice، TechInfo، CommissionPriceTypeIndex، Brand، MadeIn، Taxable، SaleAble، BuyAble، IsCommission.
- **InvoiceDetail (ردیف فاکتور):** Id، InvoiceId، ContainerId، Index، ProductId، Description (نام محصول)، BaseUnitPrice، Count، TotalUnitPrice، TotalToll، TotalVat، FinalUnitPrice، Serial، InvoiceProperty0 … InvoiceProperty10 (ستون‌های اضافه ردیف).
- **InvoiceDetailProductItem:** Id، ProductId، Serial، InventoryId، ProductItemId، InvoiceDetailId، ProductItemStatusIndex، ProductionDate، ExpireDate، WarrantyDurationMonth، WarrantyStartDate، WarrantyEndDate، WarrantyStartTypeIndex.

## ۱۳. روابط جدول‌ها (تصویر `expression-images/table-relations.png`)
- **CrmObject(This):** Form، Task، Ticket، Identity، PurchaseInvoice، PurchaseQuote، Quote، Invoice، ReturnPurchaseInvoice، ReturnInvoice (+ آیتم‌های قرمز بخش ۴).
- از هر CrmObject: **Parent** و **Children** ← Identity، Form، Invoice، Quote، PurchaseInvoice، PurchaseQuote، Ticket، Appointment، Contract، Input/OutputInventoryTransaction، Payment، Receipt، Task، BusinessNote، PhoneLog، Opportunity، File؛ و **Type**، **ModifierUser**، **CreatorUser**، **AssignedToUser**.
- فاکتورها و پیش‌فاکتورها ← **InvoiceDetail** ← **InvoiceDetailProductItem** ← **ProductItem**.
- **Simple Object Extended Property Relations** (فیلد اضافه از نوع آیتم که می‌تواند به این‌ها اشاره کند): Identity، Position، Department، User، Group، Invoice، Quote، PurchaseInvoice، PurchaseQuote، Form، Appointment، Receipt، Payment، Contract، Input/OutputInventoryTransaction.

## ۱۴. اشتباه‌های مستندات (برای اینکه کپی نشوند)
- جزوه مثال ۱۳: «عنوان **آخرین** فرم» را با `Order(...CreateDate).Take(1)` نوشته؛ `Order` صعودی است و **قدیمی‌ترین** را می‌دهد. برای آخرین: `OrderDes`.
- جزوه مثال ۱۱ بازه تاریخ را با `||` نوشته؛ KB با `&&`. برای «بین دو تاریخ» `&&` درست است.
- `SELECT @(this.Select(mtn)(;` غلط تایپی است ← `SELECT @(this.Select(mtn));`.
- مثال ۱۰ قدیمی `@(this.Form.Where(Children.number==90...` شکل ناقص است؛ شکل 2.8.x: `@(this.Children.Form.Where(Children.Form.npfali@mytype1==90&&(...)).Select(...))`.
- KB مثال ۱۰ تیکت `FirstResult@` و `CustomerTicket` را در دو خط شکسته و `///////` اضافه دارد؛ در کادر فعالیت همه را در **یک خط** بنویس.
- TakeOrDefault با پیش‌فرض فارسی در تصویر جزوه ← پیش‌فرض انگلیسی یا عدد.

## ۱۵. عیب‌یابی
| نشانه | علت محتمل | راه‌حل |
|---|---|---|
| کادر قرمز | نحو غلط (پرانتز، `;`، `@(`، حروف بزرگ و کوچک، `==` به‌جای `=`) | `scripts/check_expression.py` در اسکیل bpms-builder؛ مقایسه با کتابخانه بخش ۷ |
| آبی ولی فیلد خالی می‌ماند | کلید فیلد یا کد زیرنوع غلط؛ سابقه یا پدر وجود ندارد؛ نوع مبدأ و مقصد ناهمسان | کلید را از کوئری‌ساز یا شخصی‌سازی چک کن؛ رکورد آزمایشی با سابقه بساز؛ مقصد متن را امتحان کن |
| مقدار عجیب (عدد یا GUID) | مبدأ لیست کشویی یا کاربر، مقصد متن | مقصد کاربر بگذار یا چندشرطی روی Index |
| مقدار از سابقه «اشتباه» | بدون Order، اولین سابقه یافت‌شده برمی‌گردد | `OrderDes(...CreateDate).Take(1)` یا `Where` |
| متن پیش‌فرض نمایش داده نمی‌شود | پیش‌فرض فارسی | انگلیسی یا عدد |
| فعالیت SQL به «حالت خطا» می‌رود | رشته اتصال، دسترسی کاربر SQL، شبکه، نسخه SQL زیر 2017، Expression روی رسید/حواله | «تست» اتصال؛ کوئری را اول در SSMS روی دیتابیس آزمون اجرا کن |
| Expression روی آیتمی کار نمی‌کند | نسخه نرم‌افزار قدیمی‌تر از گسترش آن آیتم | جدول بخش ۴ و نسخه مشتری |

## ۱۶. توصیه‌های ما (نه متن رسمی)
- برای اتصال به دیتابیس دیگر یک **کاربر SQL با حداقل دسترسی** (فقط جدول‌ها و عملیات لازم) بساز؛ رمز را فقط در خود فعالیت وارد کن و در مستندات، ایمیل یا مخزن ننویس.
- `UPDATE`/`DELETE` بدون `WHERE` ننویس؛ اول روی کپی آزمون اجرا کن.
- برای هر فعالیت SQL «حالت بعدی در صورت خطا» را به یک کارتابل بررسی (مثلاً «خطای انتقال داده») ببر، نه به پایان.
- اگر نیاز «فراخوانی API» است نه دیتابیس، فعالیت **فراخوانی سرویس** مناسب‌تر است.
- در پاسخ RFP: «خواندن و نوشتن داده از/به SQL Server سامانه‌های دیگر در فرایند (ماژول تخصیص داده پیشرفته)» = **دارد با ماژول**؛ Oracle، MySQL و PostgreSQL مستقیم = **مستند نشده** (فقط SQL Server؛ مسیر جایگزین: وب‌سرویس یا Linked Server سمت مشتری، نیازمند تأیید تیم فنی).
