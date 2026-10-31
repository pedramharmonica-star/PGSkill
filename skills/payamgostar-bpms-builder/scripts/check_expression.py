#!/usr/bin/env python3
"""Lint and explain a PayamGostar Custom Expression (or an SQL-activity command) before pasting it.

Usage:
  python3 check_expression.py '@(this.Select(Identity.Mobile));'
  python3 check_expression.py --activity assign --item Form --dest text --version 2.8.8 '<expr>'
  python3 check_expression.py --activity sql --file command.sql
  python3 check_expression.py --self-test

--activity  assign (تخصیص مقدار) | multi (تصمیم چند شرطی) | sql (اجرای دستورات پایگاه داده)
--item      current item the workflow runs on: Form Opportunity Identity Task Ticket Quote PurchaseQuote
            Invoice PurchaseInvoice ReturnSaleInvoice ReturnPurchaseInvoice Contract Receipt Payment
            Appointment PhoneLog BusinessNote EnterInventoryTransaction ExitInventoryTransaction
--dest      destination field type: text number money date gdate checkbox time user group link html identity
--version   software version of the customer, e.g. 2.8.7 (affects which items support Expression)

Rules come from references/expression-and-sql-activity.md (knowledge skill). Exit code 1 if any ERROR.
A clean result means "syntax looks right", not "it returns the right value": always test-run on a record.
Standard library only.
"""
import argparse, json, re, sys

COMMON = {"AssignedToId": "user", "CreateDate": "date", "CreatorId": "user", "CrmObjectTypeIndex": "index",
          "Description": "html", "IdentityId": "identity", "ModifierId": "user", "ModifyDate": "date",
          "RefId": "text", "SourceCampaignId": "campaign", "StageChangeDate": "date", "StageChangedBy": "user",
          "StageId": "stage", "Subject": "text", "Summary": "html", "PriorityIndex": "index"}
BILL = {"ApproveDate": "date", "ApproverId": "user", "BillableObjectStateIndex": "index", "CreditValue": "money",
        "DebitValue": "money", "FinalValue": "money", "Number": "text", "NumberedById": "user", "NumberedDate": "date",
        "PaidValue": "money", "RejectDate": "date", "RejectedById": "user", "RemainedValue": "money",
        "BillableObjectTypeindex": "index", "BillableObjectTypeIndex": "index"}
INV = dict(BILL, AdditionalCosts="money", Discount="money", DiscountPercent="number", InvoiceDate="date",
           PriceListId="pricelist", Tax="money", TaxPercent="number", Toll="money", TollPercent="number",
           TotalAmount="number", TotalValue="money", TotalValueWithDiscount="money", TotalValueWithTax="money",
           Vat="money", VatPercent="number", InvoiceDetailContainer="container")
IDENT = {"Id": "text", "AreaCode": "text", "AreaCodes": "text", "Balance": "money", "Cities": "text", "City": "text",
         "ClassificationRuleId": "class", "ColorId": "color", "Countries": "text", "Country": "text",
         "CustomerDate": "date", "CustomerNo": "text", "DetailAddress": "text", "DetailAddresses": "text",
         "Email": "text", "Emails": "text", "Fax": "text", "Faxes": "text", "FullAddress": "text",
         "FullAddresses": "text", "Mobile": "text", "Mobiles": "text", "RelatedUserIdOther": "user",
         "RelatedUserIdSales": "user", "RelatedUserIdSupport": "user", "Tel": "text", "TeleFax": "text",
         "TeleFaxes": "text", "TelephonyPassword": "text", "Tels": "text", "Website": "link", "ZipCode": "text",
         "ZipCodes": "text",
         # organisation
         "CPFirstName": "text", "CPGender": "text", "CPLastName": "text", "CPMobiles": "text", "EconomicCode": "text",
         "ManagerFirstName": "text", "ManagerGender": "text", "ManagerLastName": "text", "ManagerMobiles": "text",
         "RegisterNo": "text", "Registerdate": "date",
         # person
         "FirstName": "text", "LastName": "text", "Gender": "text", "NationalCode": "text",
         "PersonPrefixIndex": "index", "BirthDate": "date", "UserId": "user"}
STOCK = {"ApproveDate": "date", "ApproverId": "user", "AtfNumber": "text", "EnterCauseIndex": "index",
         "ExitCauseIndex": "index", "InventoryId": "inventory", "InventoryTransactionDetailContainer": "container",
         "InventoryTransactionTypeIndex": "index", "InvoiceId": "text", "Number": "text", "ReceiverDesc": "text",
         "SerialNumber": "text", "ShipperDesc": "text", "SrcDstInventoryId": "text", "TotalValue": "money",
         "TransactionStatusIndex": "index", "TransDate": "date"}
TABLES = {
    "Form": {}, "BusinessNote": {}, "File": {},
    "Task": {"DueDate": "date", "PercentCompleted": "number", "StartDate": "date", "TaskStatusIndex": "index"},
    "Appointment": {"AppointmentStatus": "index", "CalendarId": "calendar", "DueDate": "date", "EndTime": "time",
                    "IsAllDay": "checkbox", "Latitude": "number", "Location": "text", "Longitude": "number",
                    "RoomId": "room", "StartDate": "date", "StartTime": "time"},
    "Ticket": {"EmailAddress": "text", "ImpactIndex": "index", "Number": "text", "ResponseStatusIndex": "index",
               "SeverityIndex": "index", "StatusIndex": "index"},
    "Contract": dict(BILL, ReceivedValue="money", EndDate="date", IsBillable="checkbox", StartDate="date"),
    "Opportunity": {"ClosedDateTime": "date", "EstimatedValue": "money", "FailDate": "date", "FinalValue": "money",
                    "LostCauseIndex": "index", "OppSourceTypeIndex": "index", "OppStatusTypeIndex": "index",
                    "OppTypeIndex": "index", "Probability": "number", "PurchaseProcessIndex": "index",
                    "RealizedValue": "money", "SuccessDate": "date", "TotalDiscount": "money",
                    "TotalDiscountPercent": "number", "TotalValue": "money", "WonCauseIndex": "index"},
    "PhoneLog": {"CallTypeIndex": "index", "Duration": "duration", "StartTime": "date", "TalkedTo": "text"},
    "Receipt": {"ParentCrmObjectId": "crmitem", "ApproveDate": "date", "ApproverId": "user", "NumberedById": "user",
                "NumberedDate": "date", "FinalValue": "money", "Number": "text", "RejectDate": "date",
                "RejectedById": "user", "RemainedValue": "money", "IsPayed": "checkbox", "PayDate": "date",
                "PaymentMethodIndex": "index", "PaymentTypeIndex": "index", "SettledDate": "date",
                "BranchCode": "text", "ChequeBankIndex": "index", "ChequeNo": "text", "Receipt_CardNo": "text",
                "RefNo": "text"},
    "Quote": dict(INV, ExpireDate="date"), "PurchaseQuote": dict(INV, ExpireDate="date"),
    "Invoice": dict(INV, ReceivedValue="money"), "PurchaseInvoice": dict(INV, ReceivedValue="money"),
    "ReturnSaleInvoice": dict(INV, ReceivedValue="money"), "ReturnPurchaseInvoice": dict(INV, ReceivedValue="money"),
    "ReturnInvoice": dict(INV, ReceivedValue="money"),
    "EnterInventoryTransaction": STOCK, "ExitInventoryTransaction": STOCK,
    "InputInventoryTransaction": STOCK, "OutputInventoryTransaction": STOCK,
    "Identity": IDENT, "Type": {"Code": "text"},
}
TABLES["Payment"] = TABLES["Receipt"]
NON_CRM = {"InvoiceDetail", "InvoiceDetailProductItem", "ProductItem", "Product", "User", "AppointmentAttendant"}
FA = {"Form": "فرم", "Task": "وظیفه", "Appointment": "قرارملاقات", "Ticket": "درخواست پشتیبانی", "Contract": "قرارداد",
      "Opportunity": "فرصت", "PhoneLog": "تماس تلفنی", "Receipt": "دریافت", "Payment": "پرداخت", "Quote": "پیش‌فاکتور فروش",
      "PurchaseQuote": "پیش‌فاکتور خرید", "Invoice": "فاکتور فروش", "PurchaseInvoice": "فاکتور خرید",
      "ReturnSaleInvoice": "فاکتور برگشت از فروش", "ReturnPurchaseInvoice": "فاکتور برگشت از خرید",
      "BusinessNote": "یادداشت", "File": "فایل", "Identity": "هویت", "Type": "نوع (زیرنوع)",
      "EnterInventoryTransaction": "رسید انبار", "ExitInventoryTransaction": "حواله انبار"}
TYPE_FA = {"text": "متن", "number": "عدد", "money": "پول", "date": "تاریخ شمسی", "gdate": "تاریخ میلادی",
           "checkbox": "چک‌باکس", "time": "ساعت", "user": "کاربر", "group": "گروه", "link": "لینک", "html": "Html",
           "identity": "شرکت/شخص", "index": "لیست کشویی (Index)"}
DEST_OK = {"text", "number", "money", "date", "gdate", "checkbox", "time", "user", "group", "link", "html", "identity"}
KEYWORDS = ["Select", "Where", "OrderDes", "Order", "TakeOrDefault", "Take", "Children", "Parent", "Identity"]

# Items that accept Expression as the CURRENT item, by first version (KB + release notes)
ITEM_SINCE = {"Form": "2.6.0", "Identity": "2.6.0", "Task": "2.6.0", "Ticket": "2.6.0", "Quote": "2.6.0",
              "PurchaseQuote": "2.6.0", "Invoice": "2.6.0", "PurchaseInvoice": "2.6.0", "ReturnSaleInvoice": "2.6.0",
              "ReturnPurchaseInvoice": "2.6.0", "Receipt": "2.6.1", "Payment": "2.6.1", "Opportunity": "2.7.1",
              "Contract": "2.8.0", "Appointment": "2.8.7", "PhoneLog": "2.8.7", "BusinessNote": "2.8.7", "File": "2.8.7"}
NEVER = {"EnterInventoryTransaction", "ExitInventoryTransaction", "InputInventoryTransaction", "OutputInventoryTransaction"}


def vt(v):
    return tuple(int(x) for x in re.findall(r"\d+", v or "0"))


def find_expressions(text):
    """Return list of (start, end, inner) for every @( ... ) with balanced parentheses."""
    out, i = [], 0
    while True:
        i = text.find("@(", i)
        if i < 0:
            return out
        depth, j, q = 0, i + 1, None
        while j < len(text):
            c = text[j]
            if q:
                if c == q:
                    q = None
            elif c == '"':
                q = c
            elif c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        out.append((i, j, text[i + 2:j]))
        i = j + 1


def split_calls(inner):
    """this.Where(..).Select(..).Order(..).Take(1) -> [('this',None),('Where','..'),...] (top-level only)."""
    parts, buf, depth, q = [], "", 0, None
    for c in inner:
        if q:
            buf += c
            if c == q:
                q = None
            continue
        if c == '"':
            q = c
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        if c == "." and depth == 0:
            parts.append(buf)
            buf = ""
        else:
            buf += c
    parts.append(buf)
    calls = []
    for p in parts:
        m = re.match(r"^\s*([A-Za-z_][\w@]*)\s*(?:\((.*)\))?\s*$", p, re.S)
        calls.append((m.group(1), m.group(2)) if m else (p.strip(), None))
    return calls


def paths(arg):
    """Dotted member paths inside an argument, outside string literals."""
    s = re.sub(r'"[^"]*"', '""', arg or "")
    return [m.group(0) for m in re.finditer(r"[A-Za-z_][\w]*(?:@[\w]+)?(?:\.[A-Za-z_][\w]*(?:@[\w]+)?)*", s)
            if not re.fullmatch(r"Convert\.ToDateTime|ToDateTime|Convert", m.group(0))]


def analyse_path(p, rel_prefix, rep, ctx):
    """p like Children.Ticket.FirstResult@CustomerTicket. Returns (table, field, type or None)."""
    segs = (rel_prefix + p.split(".")) if rel_prefix else p.split(".")
    rel, table, field = None, None, None
    rest = list(segs)
    if rest and rest[0].lower() in ("children", "parent", "identity") and rest[0] not in ("Children", "Parent", "Identity"):
        rep.warn(f"«{rest[0]}» با حروف کوچک/بزرگ نادرست؛ شکل امن: {rest[0].capitalize()}")
        rest[0] = rest[0].capitalize()
    if rest and rest[0] in ("Children", "Parent", "Identity"):
        rel = rest.pop(0)
        if rel == "Identity":
            table = "Identity"
    if rel == "Parent" and rest and rest[0] == "Identity":
        rep.warn("برای هویت به Parent نیاز نیست: Identity.<فیلد>")
    if rel in ("Children", "Parent") and rest:
        table = rest.pop(0)
        if table not in TABLES and table not in NON_CRM:
            near = [t for t in TABLES if t.lower() == table.lower()]
            if near:
                rep.error(f"نام جدول «{table}» حروف بزرگ/کوچک غلط دارد؛ درست: {near[0]}")
            else:
                rep.warn(f"نام جدول «{table}» در فهرست جدول‌ها نیست (Form, Quote, Invoice, Ticket, Contract, Opportunity …)")
        if table in NON_CRM and ctx["where"] is False and ctx["activity"] in ("assign", "multi"):
            rep.error(f"جدول {table} در تخصیص مقدار/چندشرطی فقط داخل Where مجاز است (در فعالیت SQL آزاد است)")
        if table == "Invoice" and ctx["where"] is False:
            ctx["children_invoice"] = True
    if not rest:
        return table, None, None
    if rel is None and len(rest) >= 3 and rest[1] in TABLES:   # this.Select(frmk@type.Form.customerno@type2)
        rep.info(f"فیلد مرجع «{rest[0]}» از نوع آیتم {rest[1]} و سپس فیلد «{rest[2]}» درون آن")
        table, rest = rest[1], rest[2:]
    field = rest[-1]
    key, _, itemkey = field.partition("@")
    tname = table or ctx.get("item")
    allfields = dict(COMMON, **TABLES[tname]) if tname in TABLES else ({} if tname else dict(COMMON))
    strict = tname in TABLES
    ftype = allfields.get(key)
    if itemkey:
        ftype = None  # extended field: type unknown
        if key in allfields:
            rep.warn(f"«{key}» فیلد پیش‌فرض است؛ @{itemkey} فقط برای فیلد اضافه لازم است")
    elif strict and ftype is None:
        near = [f for f in allfields if f.lower() == key.lower()]
        if near:
            rep.error(f"کلید «{key}» حروف بزرگ/کوچک غلط دارد؛ درست: {near[0]}")
            ftype = allfields[near[0]]
        else:
            rep.warn(f"«{key}» فیلد پیش‌فرض {table or ctx.get('item')} نیست؛ اگر فیلد اضافه است «@کدزیرنوع» "
                     f"را بعدش بگذار (از 2.7.5.3)، و کلید را از شخصی‌سازی یا کوئری‌ساز چک کن")
    return table, field, ftype


class Report:
    def __init__(self):
        self.items = []

    def error(self, m): self.items.append(("ERROR", m))
    def warn(self, m): self.items.append(("WARN", m))
    def info(self, m): self.items.append(("INFO", m))

    @property
    def errors(self): return [m for k, m in self.items if k == "ERROR"]


def check(text, activity="assign", item=None, dest=None, version=None):
    rep = Report()
    ctx = {"activity": activity, "item": item, "where": False}
    raw = text.strip()
    if activity in ("assign", "multi") and "\n" in raw:
        rep.warn("دستور چندخطی است؛ در کادر تخصیص مقدار/چندشرطی در یک خط بنویس")
    if item:
        if item in NEVER:
            rep.error(f"Expression روی {FA.get(item, item)} پشتیبانی نمی‌شود (استثنای صریح 2.8.7)؛ فقط SQL خام در فعالیت SQL")
        elif item in ITEM_SINCE and version and vt(version) < vt(ITEM_SINCE[item]):
            rep.error(f"Expression روی {FA.get(item, item)} از نسخه {ITEM_SINCE[item]} است؛ نسخه مشتری {version}")
        elif item in ITEM_SINCE and vt(ITEM_SINCE[item]) > vt("2.6.0") and not version:
            rep.warn(f"Expression روی {FA.get(item, item)} از نسخه {ITEM_SINCE[item]}؛ نسخه مشتری را چک کن")
    exprs = find_expressions(raw)
    if not exprs:
        if activity == "sql":
            rep.info("دستور SQL خام بدون Expression")
        else:
            rep.error("دستور باید به شکل @(...); باشد")
    if activity == "sql":
        low = re.sub(r"'[^']*'", "''", raw.lower())
        for verb in ("update", "delete"):
            if re.search(rf"\b{verb}\b", low) and not re.search(r"\bwhere\b", low):
                rep.error(f"{verb.upper()} بدون WHERE: همه ردیف‌های جدول تغییر می‌کند")
        if exprs and not re.search(r"\b(select|update|insert|delete|exec|merge)\b", low):
            rep.warn("در فعالیت SQL، Expression باید داخل دستور SQL باشد: SELECT @(Expression);")
        if re.search(r"password\s*[:=]\s*[^;.\s]", raw, re.I):
            rep.warn("رمز در متن دستور دیده شد؛ آن را جایی ذخیره یا ارسال نکن")
    explain = []
    for s, e, inner in exprs:
        tail = raw[e + 1:e + 3]
        if activity in ("assign", "multi") and not tail.startswith(";"):
            rep.warn("بعد از @(...) علامت ; بگذار: @(...);")
        if inner.count('"') % 2:
            rep.error("تعداد کوتیشن \" فرد است")
        if re.search(r"[“”«»]", inner):
            rep.error("کوتیشن فارسی/هوشمند (“ ” « ») به‌کار رفته؛ فقط \" انگلیسی")
        calls = split_calls(inner)
        head = calls[0][0]
        if head != "this":
            if head.lower() == "this":
                rep.warn(f"«{head}» → شکل رسمی KB «this» است")
            else:
                rep.error("دستور باید با this شروع شود")
        names = [c[0] for c in calls[1:]]
        for n in names:
            base = n.split("@")[0]
            for kw in KEYWORDS:
                if base != kw and base.lower() == kw.lower():
                    rep.warn(f"«{base}» → «{kw}» (حساس به حروف بزرگ و کوچک)")
        lname = [n.lower() for n in names]
        if "select" not in lname:
            rep.error("Select(...) ندارد")
        has_order = any(n in ("order", "orderdes") for n in lname)
        has_take = any(n in ("take", "takeordefault") for n in lname)
        if has_take and not has_order:
            rep.warn("Take بدون Order/OrderDes: ترتیب «اولین یافت‌شده» است، نه تاریخ")
        if has_order and not has_take:
            rep.warn("Order بدون Take: بهتر است Take(1) بگذاری تا ردیف دقیق مشخص شود")
        rel_prefix, sel_types, desc = [], [], []
        for name, arg in calls[1:]:
            ln = name.lower()
            if arg is None and ln not in ("children", "parent", "identity") and "@" not in name and name not in TABLES:
                if ln in ("select", "where", "order", "orderdes", "take", "takeordefault"):
                    rep.error(f"{name} پرانتز ندارد")
                else:
                    rel_prefix.append(name)
                continue
            if arg is None:
                rel_prefix.append(name)
                continue
            if ln == "where":
                ctx["where"] = True
                if re.search(r"(?<![=!<>])=(?!=)", re.sub(r'"[^"]*"', '""', arg)):
                    rep.error("در Where برای مقایسه از == استفاده کن، نه =")
                if re.search(r"Convert\.ToDateTime", arg) and re.search(r">=.*\|\|.*<=", arg):
                    rep.warn("بازه تاریخ با || نوشته شده؛ برای «بین دو تاریخ» && درست است")
                if "BillableObjectTypeindex" in arg or "BillableObjectTypeIndex" in arg:
                    m = re.search(r"BillableObjectType[Ii]ndex\s*==\s*(\d+)", arg)
                    if m:
                        desc.append({"8": "فقط فاکتور برگشت از فروش", "7": "فقط فاکتور برگشت از خرید"}.get(m.group(1), f"نوع آیتم مالی {m.group(1)}"))
                for p in paths(arg):
                    analyse_path(p, rel_prefix, rep, ctx)
                desc.append("با شرط: " + arg.strip())
                ctx["where"] = False
            elif ln == "select":
                for p in paths(arg):
                    t, f, ty = analyse_path(p, rel_prefix, rep, ctx)
                    sel_types.append(ty)
                    src = {"Children": "سوابق", "Parent": "آیتم پدر", "Identity": "هویت مرتبط"}.get(
                        (rel_prefix + p.split("."))[0], "خود آیتم جاری")
                    desc.insert(0, f"مقدار «{f}» از {src}" + (f" ({FA.get(t, t)})" if t else ""))
                    if "Children" in (rel_prefix + p.split("."))[:1] and not has_order and "where" not in lname:
                        rep.warn("Children بدون Order/Where: «اولین سابقه یافت‌شده» برمی‌گردد (نه جدیدترین)")
            elif ln in ("order", "orderdes"):
                for p in paths(arg):
                    analyse_path(p, rel_prefix, rep, ctx)
                desc.append(("مرتب صعودی (اول = قدیمی‌ترین) بر " if ln == "order" else "مرتب نزولی (اول = جدیدترین) بر ") + arg.strip())
            elif ln == "takeordefault":
                m = re.match(r"\s*(\d+)\s*,\s*\"([^\"]*)\"\s*$", arg)
                if not m:
                    rep.error('TakeOrDefault(n,"پیش‌فرض") نادرست است')
                else:
                    if re.search(r"[؀-ۿ]", m.group(2)):
                        rep.error("مقدار پیش‌فرض TakeOrDefault فارسی است؛ فقط انگلیسی یا عدد نمایش داده می‌شود")
                    desc.append(f"ردیف {m.group(1)}؛ اگر نبود «{m.group(2)}»")
            elif ln == "take":
                if not re.fullmatch(r"\s*\d+\s*", arg):
                    rep.error("Take(n) فقط عدد می‌گیرد")
                desc.append(f"ردیف {arg.strip()}")
        if dest:
            for ty in sel_types:
                if ty is None:
                    rep.info("نوع فیلد مبدأ (فیلد اضافه) معلوم نیست؛ هم‌نوعی را دستی چک کن")
                elif ty == "index":
                    rep.warn("مبدأ لیست کشویی است: فقط Index (شماره ردیف گزینه) منتقل می‌شود؛ مقصد متن + چندشرطی برای متن گزینه")
                    if dest != "text":
                        rep.error("مبدأ لیست کشویی فقط به مقصد متن")
                elif dest == "text":
                    if ty == "user":
                        rep.warn("مبدأ کاربر در مقصد متن: Id کاربر می‌نشیند؛ مقصد «کاربر» بهتر است")
                    else:
                        rep.info("مقصد متن است: از 2.7.0 هم‌نوعی لازم نیست")
                elif ty != dest and not (ty == "date" and dest == "gdate"):
                    rep.error(f"نوع مبدأ «{TYPE_FA.get(ty, ty)}» با مقصد «{TYPE_FA.get(dest, dest)}» یکسان نیست "
                              f"(در تخصیص مقدار/چندشرطی الزامی است؛ یا مقصد را متن کن)")
        explain.append("؛ ".join(desc))
    return rep, explain


SELF_TESTS = [
    ("@(this.Select(Subject));", {}, 0),
    ("@(this.Select(Identity.Mobile));", {"dest": "text"}, 0),
    ("@(this.Select(Children.Ticket.Description).OrderDes(Children.Ticket.CreateDate).Take(1));", {"dest": "html"}, 0),
    ("@(this.Select(Children.Ticket.Description).OrderDes(Children.Ticket.CreateDate).TakeOrDefault(2,\"Only one ticket\"));", {}, 0),
    ("@(this.Where(Children.Contract.Subject==\"نمایندگی\").Select(Children.Contract.EndDate));", {"dest": "date"}, 0),
    ("@(this.Where(Children.Invoice.BillableObjectTypeindex == 8).Select(Children.Invoice.FinalValue));", {"dest": "money"}, 0),
    ("@(this.Select(Parent.Opportunity.DeliveryDate@SalesOpportunity));", {}, 0),
    ("SELECT @(this.Select(Children.Contract.FinalValue));", {"activity": "sql"}, 0),
    ("update [Products] set [ProductName] = @(this.Select(Subject)); Where productId='9DC87DFA'", {"activity": "sql"}, 0),
    ("@(this.Where(Children.Form.Subject=\"x\").Select(Children.Form.Email));", {}, 1),
    ("@(this.Select(Children.Form.Email).Order(Children.Form.CreateDate).TakeOrDefault(1,\"ندارد\"));", {}, 1),
    ("@(this.Select(CreatorId));", {"dest": "money"}, 1),
    ("@(this.Select(Subject));", {"item": "ExitInventoryTransaction"}, 1),
    ("@(this.Select(Subject));", {"item": "Appointment", "version": "2.8.5"}, 1),
    ("update [Products] set [ProductName] = @(this.Select(Subject));", {"activity": "sql"}, 1),
    ("@(this.Select(Children.Product.Name));", {}, 1),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("expression", nargs="?")
    ap.add_argument("--file")
    ap.add_argument("--activity", default="assign", choices=["assign", "multi", "sql"])
    ap.add_argument("--item")
    ap.add_argument("--dest", choices=sorted(DEST_OK))
    ap.add_argument("--version")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        bad = 0
        for expr, kw, want_err in SELF_TESTS:
            rep, _ = check(expr, **kw)
            got = 1 if rep.errors else 0
            if got != want_err:
                bad += 1
                print("FAIL", expr, kw, rep.items)
        print(f"self-test: {len(SELF_TESTS) - bad}/{len(SELF_TESTS)} passed")
        sys.exit(1 if bad else 0)
    text = open(a.file, encoding="utf-8").read() if a.file else a.expression
    if not text:
        ap.error("expression or --file required")
    rep, explain = check(text, a.activity, a.item, a.dest, a.version)
    if a.json:
        print(json.dumps({"ok": not rep.errors, "findings": rep.items, "explain": explain}, ensure_ascii=False, indent=1))
    else:
        for e in explain:
            if e:
                print("معنی:", e)
        for k, m in rep.items:
            print(f"[{k}] {m}")
        print("نتیجه:", "خطا دارد" if rep.errors else "نحو قابل‌قبول (درستی مقدار را با اجرای آزمایشی چک کن)")
    sys.exit(1 if rep.errors else 0)


if __name__ == "__main__":
    main()
