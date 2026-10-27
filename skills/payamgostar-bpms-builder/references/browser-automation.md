# ساخت با مرورگر (برای ایجنت‌ها)

- **ورود را کاربر انجام می‌دهد.** ایجنت رمز وارد نمی‌کند. نشانی و رمز را جایی ذخیره نکن.
- **alert:** پیام‌های پیام‌گستر `alert()` هستند و رندر صفحه را قفل می‌کنند. بعد از هر بارگذاری صفحه یا iframe، پیش از کلیک ذخیره: `window.alert=m=>{(window.__alerts=window.__alerts||[]).push(m)}` و همین را روی `iframe.contentWindow` هم بگذار. اگر صفحه قفل شد، از کاربر بخواه پیام را بخواند و OK بزند. `confirm` را فقط وقتی override کن که کاربر همان کار را صریحاً خواسته است.
- **دیالوگ‌ها iframe هستند:** آخرین iframe قابل‌مشاهده = `[...document.querySelectorAll('iframe')].filter(f=>f.offsetParent).pop()`. می‌توانی `src` آن را بدون `DialogView=True` در تب اصلی باز کنی.
- **شناسه‌های کنترل‌ها** (پسوند id، با `[id$="…"]`):
  - نوع آیتم (`EditCrmObjectType.aspx`): `rptTextBoxes_ctl00/01_txtLocalizedNameField`، کد، چک‌باکس «فعال» (label «فعال»).
  - گروه‌فیلد: `rptTextBoxes_ctl00/01_txtLocalizedNameField`، `drpColumns`، `chkExpandForView`، `btnSave`.
  - فیلد کشویی (`CrmFieldEdit/EditDropDownListField.aspx`): `Name_rptTextBoxes_ctl00/01_…`، `ltip_rptTextBoxes_ctl01_…`، `drpPropertyGroup`، `txtUserKey`، `CrmFieldEditFormCustomActions_btnSave` (ماندن)، `btnSaveAndExit`.
  - مقدار لیست (`GetCrmTypeFieldValue.aspx`، iframe تو در تو): `ctl00_C_txtCrmTypeFieldValue`، `btnConfirm`. دکمه تأیید با رویداد keyup فعال می‌شود: `w.jQuery(inp).trigger('keyup')`.
  - حالت (کارتابل/پایان، `Process/EditProcessState.aspx`): `txtName`، `txtStateCode`، `tTextBoxes_ctl01_txtLocalizedNameField`، `drpStateType` (۱ معمولی، ۲ اولیه)، `dhEndTime_txtDay`، `chkOnEndSetFollowUp`، `btnSave`.
  - اقدام (`Process/EditProcessStateAction.aspx`): `txtName`، `drpStates` (حالت بعدی)، `txtActionCode`، `ImageButton1` (ذخیره).
  - نمایش فیلدها (`ProcessTypeStateFields/EditVisibility`): selectهای `Groups_<i>__Properties_<j>__DisplayMode` (۰ نمایش، ۱ مخفی، ۲ غیرفعال).
- **کارهای طولانی را خرد کن:** هر فراخوانی JavaScript کمتر از ۴۰ ثانیه. بعد از هر ذخیره ۳ تا ۵ ثانیه صبر کن و نتیجه را از فهرست بخوان، نه از پیام.
- **دکمه‌هایی که postback دارند** (ایجاد کارتابل، افزودن حالت نهایی) را با کلیک واقعی بزن و بعد در فراخوانی جدا فرم را پر کن.
- رکورد آزمایشی: `EditForm.aspx?TypeId=<شناسه نوع>`. باز کردن رکورد موجود: `/_SiteCommon/Handler/CrmObjectFinder.ashx?Id=<شناسه>`.
