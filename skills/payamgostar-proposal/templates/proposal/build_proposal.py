# -*- coding: utf-8 -*-
"""PayamGostar proposal builder (approved layout, 1405/08/09).

Usage:
  python3 build_proposal.py <data.py> <out_dir>
  cd <out_dir> && NODE_PATH=$(npm root -g) node <this folder>/render.js proposal.html Proposal.pdf

All customer content lives in <data.py> (see example_data.py for every field). This file holds only the
approved layout and PayamGostar's own, sourced content (company facts, install prerequisites, security,
deployment unit, SLA rules, web services). Never commit a real customer's data file to the repository.
"""
import os, sys, html, re, math, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import charts as CH
REPO = (os.environ.get('PG_ASSETS') or os.path.normpath(os.path.join(HERE, '..', '..', 'assets'))).rstrip('/') + '/'   # skills/payamgostar-proposal/assets/

spec = importlib.util.spec_from_file_location('data', sys.argv[1])
D = importlib.util.module_from_spec(spec); spec.loader.exec_module(D)
OUT = sys.argv[2]
DATA_DIR = os.path.dirname(os.path.abspath(sys.argv[1]))
def asset(p):
    """screenshot path: absolute, relative to the data file, or relative to assets/"""
    if p.startswith('<') or p.startswith('file://'): return p
    for base in (DATA_DIR + '/', REPO):
        if os.path.exists(base + p): return 'file://' + base + p
    return 'file://' + p

C = D.CLIENT_SHORT
AW = getattr(D, 'AGENT_WORD', 'نماینده')   # who uses the agents club: نماینده، پیمانکار، تأمین‌کننده …
R = D.ROWS
CATS = D.CATS
CATN = dict(CATS)
FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
def fa(x): return str(x).translate(FA)
TBD = re.compile(r'\[\[(.*?)\]\]')
def e(s): return TBD.sub(lambda m: f'<span class="tbd">{m.group(1)}</span>', html.escape(s))
FOOT = D.FOOTER
stat = {}
for r in R:
    c = r[0][0]; stat.setdefault(c, {'K': 0, 'J': 0, 'F': 0}); stat[c][r[3]] += 1
TOT = {k: sum(v[k] for v in stat.values()) for k in 'KJF'}
CSS = open(os.path.join(HERE, 'style.css'), encoding='utf-8').read().replace('{{REPO}}', 'file://' + REPO)

pages, KEY = [], {}
pno = [1]
def corner():
    return f'<div class="bar"></div><div class="hexwrap"><div class="h"><img src="file://{REPO}logo/payamgostar-mark-160.png"></div></div>'
def foot():
    pno[0] += 1
    return f'<div class="foot"><span class="pg">{fa(pno[0])}</span><span>{FOOT}</span></div>'
def head(eyebrow, title):
    return f'<div class="eyebrow">{eyebrow}</div><h1>{e(title)}</h1><div class="uline"></div>'
def page(body, cls='', key=None):
    if key: KEY[key] = len(pages) + 1
    pages.append(f'<section class="page {cls}">{body}</section>')

XM = '<svg class="x" viewBox="0 0 40 40"><use href="#xm"/></svg>'
ARROW = '<div class="arrow"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F26122" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg></div>'
ICONS = {
 'form': '<path d="M6 3h9l3 3v15H6z"/><path d="M9 11h6M9 15h6"/>',
 'user': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><path d="M16 9h5M18.5 6.5L21 9l-2.5 2.5"/>',
 'users': '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 15c3 0 6 1.5 6 4.5"/>',
 'clock': '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l3 2M9 2h6"/>',
 'send': '<path d="M21 4L10 15"/><path d="M21 4l-7 17-4-6-6-4z"/>',
 'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 'chat': '<path d="M4 5h16v11H8l-4 4z"/><path d="M8 9h8M8 12h5"/>',
 'check': '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l3 3 5-6"/>',
 'home': '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 'key': '<circle cx="8" cy="15" r="4"/><path d="M11 12l8-8M16 7l3 3"/>',
 'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 'link': '<path d="M10 14a5 5 0 007 0l3-3a5 5 0 00-7-7l-1 1"/><path d="M14 10a5 5 0 00-7 0l-3 3a5 5 0 007 7l1-1"/>',
 'star': '<path d="M12 3l2.8 5.8 6.2.9-4.5 4.4 1 6.2L12 17.4 6.5 20.3l1-6.2L3 9.7l6.2-.9z"/>',
 'cal': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 'coin': '<circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .9-3 2.2 0 3 6 1.6 6 4.6 0 1.3-1.3 2.2-3 2.2-1.4 0-2.6-.6-3-1.6M12 6v2M12 16v2"/>',
 'tool': '<path d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 005.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
 'db': '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
 'server': '<rect x="3" y="3" width="18" height="7" rx="2"/><rect x="3" y="14" width="18" height="7" rx="2"/><path d="M7 6.5h.01M7 17.5h.01M11 6.5h6M11 17.5h6"/>',
 'search': '<circle cx="11" cy="11" r="7"/><path d="M21 21l-5-5"/>',
 'flow': '<rect x="3" y="3" width="7" height="6" rx="1.5"/><rect x="14" y="15" width="7" height="6" rx="1.5"/><path d="M6.5 9v4a2 2 0 002 2H14"/>',
 'cap': '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/>',
 'life': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M5.6 5.6l3.6 3.6M14.8 14.8l3.6 3.6M18.4 5.6l-3.6 3.6M9.2 14.8l-3.6 3.6"/>',
 'up': '<path d="M12 19V5M5 12l7-7 7 7"/>',
}
def icon(n, col='#F26122', s=28, sw=1.8):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[n]}</svg>'

# ---------- hexagon mosaic (cover, back cover) ----------
def hexpts(cx, cy, r):
    return ' '.join(f'{cx + r*math.cos(math.radians(-90+60*k)):.1f},{cy + r*math.sin(math.radians(-90+60*k)):.1f}' for k in range(6))
MOS = [0]
def mosaic(cells, r=150, gap=7, w=980, h=1080):
    rr = r - gap
    defs, body = [], []
    MOS[0] += 1; n = MOS[0] * 100
    defs.append(f'<linearGradient id="og{MOS[0]}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7894E"/><stop offset="1" stop-color="#E8570E"/></linearGradient>'
                f'<filter id="sh{MOS[0]}" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#1C1F23" flood-opacity=".22"/></filter>')
    for cx, cy, kind, *arg in cells:
        pts = hexpts(cx, cy, rr)
        if kind in ('img', 'shot'):
            n += 1
            defs.append(f'<clipPath id="hc{n}"><polygon points="{pts}"/></clipPath>')
            src = arg[0]; par = arg[1] if len(arg) > 1 else 'xMidYMid'
            body.append(f'<g filter="url(#sh{MOS[0]})"><g clip-path="url(#hc{n})"><rect x="{cx-r}" y="{cy-r}" width="{2*r}" height="{2*r}" fill="#fff"/>'
                        f'<image href="{src}" x="{cx-r}" y="{cy-r}" width="{2*r}" height="{2*r}" preserveAspectRatio="{par} slice"/></g></g>')
            if kind == 'shot':
                body.append(f'<polygon points="{pts}" fill="none" stroke="#F4C3A8" stroke-width="3"/>')
        elif kind == 'or':
            body.append(f'<g filter="url(#sh{MOS[0]})"><polygon points="{pts}" fill="url(#og{MOS[0]})"/></g>')
            ir = rr * 0.46
            body.append(f'<polygon points="{hexpts(cx, cy, ir)}" fill="#fff"/>')
            s = ir * 1.05
            body.append(f'<image href="file://{REPO}logo/payamgostar-mark-160.png" x="{cx-s/2}" y="{cy-s/2}" width="{s}" height="{s}"/>')
        elif kind == 'deep':
            body.append(f'<polygon points="{pts}" fill="#B8460F"/>')
        elif kind == 'solid':
            body.append(f'<polygon points="{pts}" fill="url(#og{MOS[0]})"/>')
        elif kind == 'tint':
            body.append(f'<polygon points="{pts}" fill="#FDD9C4"/>')
        elif kind == 'pale':
            body.append(f'<polygon points="{pts}" fill="#FFF3EC"/>')
        elif kind == 'line':
            body.append(f'<polygon points="{hexpts(cx, cy, rr-2)}" fill="none" stroke="#F4C3A8" stroke-width="3"/>')
    return f'<svg class="mosaic" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs>{"".join(defs)}</defs>{"".join(body)}</svg>'

def grid(i, j, r=150, x0=30, y0=40):
    dx = math.sqrt(3) * r
    return x0 + j*dx + (i % 2) * dx/2, y0 + i*1.5*r

def cell(i, j, kind, *arg, **kw):
    x, y = grid(i, j, **kw)
    return (x, y, kind, *arg)


def flow(steps):
    out = []
    for i, (ic, t) in enumerate(steps):
        hl = ' hl' if i == 0 else ''
        col = '#fff' if i == 0 else '#F26122'
        out.append(f'<div class="step{hl}"><div class="ic">{icon(ic, col)}</div><div><div class="n">{fa(i+1)}</div><div class="s">{e(t)}</div></div></div>')
    return f'<div class="flowtitle">چرخه عملیاتی در {C}</div><div class="flow">' + ARROW.join(out) + '</div>'

def flow2(title, steps):
    out = []
    for i, (ic, t) in enumerate(steps):
        hl = ' hl' if i == 0 else ''
        col = '#fff' if i == 0 else '#F26122'
        out.append(f'<div class="step{hl}"><div class="ic">{icon(ic, col)}</div><div class="s">{e(t)}</div></div>')
    return f'<div class="flowtitle f2">{e(title)}</div><div class="flow f2">' + ARROW.join(out) + '</div>'


SYM = '<svg width="0" height="0" style="position:absolute"><defs><symbol id="xm" viewBox="0 0 40 40"><rect x="2" y="2" width="36" height="36" rx="10" fill="#FFF3EC"/><path d="M12 12l16 16M28 12L12 28" stroke="#F26122" stroke-width="4.2" stroke-linecap="round"/><circle cx="12" cy="12" r="3" fill="#F26122"/><circle cx="28" cy="28" r="3" fill="#F26122"/><circle cx="28" cy="12" r="3" fill="#F26122"/><circle cx="12" cy="28" r="3" fill="#F26122"/></symbol></defs></svg>'


OFF1 = f'file://{REPO}images/company/office-1.jpg'
OFF2 = f'file://{REPO}images/company/office-2.jpg'

def divider(t, s, key=None):
    page(f'<div class="dv-mark"><img src="file://{REPO}logo/payamgostar-mark-160.png"></div><div class="dv-t">{e(t)}</div><div class="dv-s">{e(s)}</div><div class="dv-ring"></div>' + foot(), 'divider', key)

def chip(cat):
    s = stat[cat]
    parts = [f'<span class="ck">{fa(s["K"])} کامل</span>']
    if s['J']: parts.append(f'<span class="cj">{fa(s["J"])} جزئی</span>')
    return f'<div class="chip2">{" ".join(parts)}<small>از {fa(sum(s.values()))} ردیف</small></div>'

def solution(S, first=False):
    capsh = ''.join(f'<div class="cap">{XM}<div><h3>{e(h)}</h3><p>{e(p)}</p></div></div>' for h, p in S['caps'])
    co = ''.join(f'<div class="callout" style="left:{x}px;top:{y}px">{fa(i+1)}</div>' for i, (x, y) in enumerate(S['callouts']))
    lg = ''.join(f'<div><b>{fa(i+1)}</b>{e(t)}</div>' for i, t in enumerate(S['legend']))
    ch = chip(S['cat']) if S.get('cat') else ''
    img = S['img']
    shot = img if img.startswith('<') else f'<img class="shot" src="{asset(img)}">'
    body = corner() + head(f'<b>راهکار {fa(S["no"])}</b><i class="sep"></i>{e(S["catname"])}', S['title']) + f'''
<div class="need"><div class="lbl">نیاز {e(C)}</div><div class="txt">{e(S["need"])}</div>{ch}</div>
<div class="caps">{capsh}</div>
<div class="shotwrap"><div class="blob"></div><div class="ring"></div><div class="dot" style="left:880px;top:118px"></div><div class="dot" style="left:-6px;top:300px;background:#F26122"></div>
<div class="browser" style="width:840px"><div class="top"><span></span><span></span><span></span><div class="url">{S["url"]}</div></div>
<div class="apphead"><div class="t"><em>{e(S["apptitle"][0])}</em>{e(S["apptitle"][1])}</div><img src="file://{REPO}logo/payamgostar-mark-160.png"></div>
<div class="shotbox">{shot}</div></div>{co}</div>
<div class="legend">{lg}</div>''' + flow(S['steps']) + foot()
    page(body, key='sol' if first else None)

# ================= pages =================
# 1 cover
cov = [cell(0, 0, 'tint'), cell(0, 1, 'img', OFF1, 'xMinYMid'), cell(0, 2, 'line'),
       cell(1, -1, 'pale'), cell(1, 0, 'img', OFF2, 'xMinYMid'), cell(1, 1, 'or'), cell(1, 2, 'line'),
       cell(2, 0, 'deep'), cell(2, 1, 'img', OFF1, 'xMaxYMid'), cell(2, 2, 'img', OFF2, 'xMaxYMid'),
       cell(3, -1, 'line'), cell(3, 0, 'solid'), cell(3, 1, 'tint'),
       cell(4, 0, 'line'), cell(4, 1, 'pale')]
rfp = f'<div class="c2-rfp">{D.COVER_KICKER}</div>' if D.COVER_KICKER else ''
page(mosaic(cov) + f'''
<img class="c2-logo" src="file://{REPO}logo/payamgostar-light-horizontal-631.png">{rfp}
<div class="c2-title">{e(D.COVER_TITLE)}</div>
<div class="c2-client">{e(D.CLIENT)}</div>
<div class="c2-sub">{e(D.COVER_SUB)}</div>
<div class="c2-meta"><div><b>پیشنهاددهنده</b>شرکت راهکار هوشمند پیام‌گستر</div><div><b>تاریخ</b>{e(D.DATE)}</div><div><b>پیوست جدا</b>{e(D.ATTACHMENT)}</div></div>
<div class="c2-slogan">فناوری در مدار مشتری</div>''', 'cover2')

# 2 TOC (page numbers filled at the end; entries only for pages that exist)
def has(k): return k in BUILT
BUILT = {'exec', 'needs', 'glance', 'cust', 'map', 'sol', 'table', 'edition', 'api', 'install', 'sec', 'lom', 'road', 'du', 'dep'}
if getattr(D, 'KPI', None): BUILT.add('kpi')
if getattr(D, 'DEMO', None): BUILT.add('demo')
if getattr(D, 'SLA', None): BUILT.add('sla')
TOCG = [('شناخت و معرفی', [('خلاصه مدیریتی', 'exec'), (f'شناخت ما از نیاز {C}', 'needs'), ('پیام‌گستر در یک نگاه', 'glance'), ('مشتریان و گواهی‌نامه‌ها', 'cust'), ('نقشه راهکار', 'map')]),
        ('راهکار', [(f'راهکار در {fa(len(D.SOLUTIONS))} حوزه کاری', 'sol'), ('نمونه داشبورد شاخص‌ها', 'kpi'), (f'جدول تطبیق {fa(len(R))} نیاز', 'table'), ('سناریوهای نمایش عملی', 'demo')]),
        ('فنی و تجاری', [('نسخه پیشنهادی', 'edition'), ('وب‌سرویس و مستندات', 'api'), ('نصب', 'install'), ('امنیت و مالکیت داده', 'sec'), ('فهرست اقلام پیشنهادی', 'lom')]),
        ('اجرا و پشتیبانی', [('نقشه راه اجرا', 'road'), ('واحد استقرار پیام‌گستر', 'du'), (f'استقرار برای {C}', 'dep'), ('سطح خدمت پشتیبانی', 'sla')])]
def tocgroup(g):
    t, items = g
    return f'<div class="tg"><div class="tgh">{e(t)}</div>' + ''.join(f'<div class="ti"><span>{e(a)}</span><em>{{{{P:{k}}}}}</em></div>' for a, k in items if has(k)) + '</div>'
page(corner() + head('فهرست', 'آنچه در این پیشنهاد می‌خوانید') + f'<div class="toc3"><div class="tcol3">{tocgroup(TOCG[0])}{tocgroup(TOCG[1])}</div><div class="tcol3">{tocgroup(TOCG[2])}{tocgroup(TOCG[3])}</div></div>' + foot())

# 3 executive summary
cols = ''.join(f'<div><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in D.EXEC_COLS)
page(corner() + head('خلاصه مدیریتی', D.EXEC_TITLE) + f'''
<div class="ex-lead">{D.EXEC_LEAD}</div>
<div class="ex-cols">{cols}</div>
<div class="ex-num"><div class="big">{fa(len(R))}</div><div class="lab">نیاز {e(D.NEED_SOURCE)}، ردیف‌به‌ردیف پاسخ داده شد</div>
 <div class="exseg">{CH.seg100([('پوشش کامل', TOT['K'], CH.OR), ('پوشش جزئی با راه جایگزین', TOT['J'], CH.BL)], w=470, h=26, size=17)}</div>
 <div class="exzero">ردیف بدون پوشش: {fa(TOT['F'])}</div></div>
<div class="ex-ed"><b>نسخه و نصب:</b> {D.EDITION_LINE} شرح کامل در صفحه {{{{P:edition}}}}.</div>''' + foot(), key='exec')

# 4 needs
nh = ''.join(f'<div class="nd"><div class="mi">{icon(i)}</div><h3>{e(t)}</h3><p>{e(p)}</p></div>' for i, t, p in D.NEEDS)
page(corner() + head('شناخت ما از نیاز', f'آنچه {C} از سامانه می‌خواهد') + f'<div class="needs">{nh}</div>' + (f'<div class="scope">{D.SCOPE}</div>' if D.SCOPE else '') + foot(), key='needs')

# 5 glance (company facts: company-facts.md)
grp = ['tejarat-aval-1st', 'hitobit', 'septa-pardakht', 'alovoip']
gh = ''.join(f'<img src="file://{REPO}images/group/{g}.png">' for g in grp)
page(corner() + head('درباره ما', 'پیام‌گستر در یک نگاه') + f'''
<div class="gl-photos"><img src="{OFF1}" style="left:0;top:0;width:520px;height:330px"><img src="{OFF2}" style="left:230px;top:250px;width:530px;height:330px;border:8px solid #fff"></div>
<div class="gl-txt">شرکت راهکار هوشمند پیام‌گستر در سال ۱۳۸۹ در گروه تجارت الکترونیک اول تأسیس شد و نرم‌افزار مدیریت ارتباط با مشتری پیام‌گستر را تولید می‌کند. امروز بیش از ۷۵۰۰ سازمان در صنایع مختلف، فروش، بازاریابی، خدمات و فرایندهای خود را با این نرم‌افزار مدیریت می‌کنند. فرم‌ساز و موتور فرایند پیام‌گستر به سازمان امکان می‌دهد فرایندهایش را بدون برنامه‌نویسی طراحی کند.</div>
<div class="gl-stats">
 <div><b>۱۳۸۹</b><span>آغاز فعالیت</span></div><div><b>+۷۵۰۰</b><span>سازمان مشتری</span></div><div><b>۲۰۰٬۰۰۰</b><span>کاربر</span></div>
 <div><b>۳۰۰٬۰۰۰</b><span>ساعت استقرار</span></div><div><b>۱۳۰</b><span>همکار متخصص</span></div><div><b><bdi>{D.VERSION}</bdi></b><span>آخرین نسخه نرم‌افزار</span></div>
</div>
<div class="gl-group"><span>شرکت‌های گروه تجارت الکترونیک اول</span>{gh}</div>''' + foot(), key='glance')

# 6 customers + 7 certificates
lh = ''.join(f'<div class="lg"><img src="file://{REPO}customer-logos/{l}.png"></div>' for l in D.CUSTOMER_LOGOS)
page(corner() + head('مشتریان', 'برخی از سازمان‌هایی که با پیام‌گستر کار می‌کنند') + f'<div class="logos">{lh}</div><div class="note">{e(D.LOGO_NOTE)}</div>' + foot(), key='cust')
page(corner() + head('گواهی‌نامه‌ها', 'مجوزها و ارزیابی امنیتی') + f'''
<div class="certs">
 <div class="cert"><img src="file://{REPO}certificates/afta-certificate.png"><h3>گواهی ارزیابی امنیتی محصول (افتا)</h3><p>شماره <bdi>CBP-C1470-0301</bdi>، صادرشده به نام هلدینگ مادر: تجارت سامانه‌های الکترونیک اول دانش‌محور اوراسیا</p></div>
 <div class="cert"><img src="file://{REPO}certificates/nezam-senfi-membership.png"><h3>مجوز سازمان نظام صنفی رایانه‌ای استان تهران</h3><p>پدیدآورنده نرم‌افزارهای رایانه‌ای، شماره ۱۴۰۱۴۸۱۶</p></div>
</div>''' + foot())

# 8 solution map
ah = ''.join(f'<div class="mp-a"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in D.AUDIENCES)
ch = ''.join(f'<div class="mp-c"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in D.COMPONENTS)
page(corner() + head('نقشه راهکار', 'همه گروه‌های مخاطب روی یک نرم‌افزار') + f'''
<div class="map"><div class="mp-col"><div class="mp-h">گروه‌های مخاطب {e(C)}</div>{ah}</div>
<div class="mp-mid"><div class="core"><img src="file://{REPO}logo/payamgostar-mark-160.png"><b>پرونده یکپارچه</b><span>{e(D.CORE_TEXT)}</span></div></div>
<div class="mp-col"><div class="mp-h">اجزای پیام‌گستر</div>{ch}</div></div>''' + foot(), key='map')

# solutions
divider('راهکار پیشنهادی', f'{fa(len(D.SOLUTIONS))} حوزه کاری {C}؛ برای هر حوزه، تصویر نرم‌افزار، قابلیت‌ها و چرخه عملیاتی')
for i, S in enumerate(D.SOLUTIONS):
    solution(S, first=(i == 0))

# KPI sample dashboard (charts only; data labelled as sample)
if getattr(D, 'KPI', None):
    K = D.KPI
    kh = ''.join(f'<div class="kp"><h3>{e(t)}</h3><p>{e(sub)}</p><div class="kc">{c}</div></div>' for t, sub, c in K['panels'])
    others = ''.join(f'<span class="kch">{e(x)}</span>' for x in K.get('others', []))
    page(corner() + head('گزارش‌ها و شاخص‌ها', K['title']) + f'''<div class="kpig">{kh}</div>
<div class="kfoot">{'<span class="kft">شاخص‌های دیگر:</span>' + others if others else ''}<span class="knote">داده‌های این صفحه ساختگی است و فقط شکل نمایش را نشان می‌دهد. شاخص‌ها با گزارش‌ساز پیشرفته ساخته می‌شوند (شخصی‌سازی)؛ زمان و هزینه پس از بررسی تیم فنی.</span></div>''' + foot(), key='kpi')

# compliance: divider, coverage chart, tables
divider('جدول تطبیق نیازها', f'پاسخ ردیف‌به‌ردیف به {fa(len(R))} شناسه نیاز' + (f'، {D.TABLE_FORMAT}' if getattr(D, 'TABLE_FORMAT', '') else ''), key='table')
COV = CH.stacked([(CATN[c], [stat[c]['K'], stat[c]['J']]) for c, _ in CATS if c in stat], w=1060, label_w=330, bar_h=26, gap=19, size=19, total_w=40)
page(corner() + head('جدول تطبیق نیازها', f'پوشش {fa(len(R))} نیاز به تفکیک حوزه') + f'''
<div class="cov-chart">{CH.legend([('پوشش کامل', CH.OR), ('پوشش جزئی با راه جایگزین', CH.BL)])}{COV}</div>
<div class="cov-side"><div class="cv"><b>{fa(TOT['K'])}</b><span>پوشش کامل</span><p>قابلیت آماده یا پیکربندی‌شدنی که نیاز را کامل برآورده می‌کند.</p></div>
<div class="cv j"><b>{fa(TOT['J'])}</b><span>پوشش جزئی</span><p>بخشی از نیاز آماده است و برای بقیه، شرط یا راه جایگزین در جدول آمده است.</p></div>
<div class="cv z"><b>{fa(TOT['F'])}</b><span>بدون پوشش</span></div></div>''' + foot())
PRI = {'ا': 'الزام', 'ت': 'ترجیحی', 'خ': 'اختیاری'}
ST = {'K': ('کامل', 'st-k'), 'J': ('جزئی', 'st-j'), 'F': ('فاقد', 'st-f')}
groups = [[r for r in R if r[0][0] == c] for c, _ in CATS]
groups = [g for g in groups if g]
for gi, chunk in enumerate(groups):
    c = chunk[0][0][0]
    rows = ''
    for r in chunk:
        lab, cl = ST[r[3]]
        alt = f'<div class="alt">◆ {e(r[6])}</div>' if r[6] else ''
        pr = f'<small>{PRI.get(r[1][:1], r[1])}، فاز {r[1][1:]}</small>' if r[1] else ''
        rows += f'<tr><td class="id"><bdi>{r[0]}</bdi>{pr}</td><td class="nd2">{e(r[2])}</td><td><span class="st {cl}">{lab}</span><div class="mt">{e(r[4])}</div></td><td class="ans">{e(r[5])}{alt}</td><td class="md">{e(r[7])}</td></tr>'
    page(corner() + head(f'جدول تطبیق، صفحه {fa(gi+1)} از {fa(len(groups))}', CATN[c]) + f'''
<table class="ct"><thead><tr><th>شناسه</th><th>نیاز {e(C)}</th><th>پوشش و روش تأمین</th><th>پاسخ پیام‌گستر و راه جایگزین</th><th>ماژول</th></tr></thead><tbody>{rows}</tbody></table>
<div class="ctnote">◆ شرط یا راه جایگزین. روش «API» یعنی اتصال با وب‌سرویس پیام‌گستر؛ برنامه‌نویسی آن شخصی‌سازی است و سمت {e(C)} یا پیمانکار آن انجام می‌شود. موارد نارنجی نیازمند تأیید تیم فنی پیام‌گستر است.</div>''' + foot())

# demo scenarios
if getattr(D, 'DEMO', None):
    mh = ''.join(f'<tr><td class="id"><bdi>{a}</bdi></td><td>{e(b)}</td><td>{e(c)}</td></tr>' for a, b, c in D.DEMO)
    page(corner() + head('نمایش عملی', D.DEMO_TITLE) + f'''
<table class="ct demo"><thead><tr><th>کد</th><th>سناریوی {e(C)}</th><th>آنچه روی نرم‌افزار نشان می‌دهیم</th></tr></thead><tbody>{mh}</tbody></table>
<div class="ctnote">{D.DEMO_NOTE}</div>''' + foot(), key='demo')

# edition (rules: editions-licensing-services.md; standard limits shown as meters)
PROCS, FORMS = D.PROCS, D.FORMS
NT = len(PROCS) + len(FORMS)
fl = ''.join(f'<span>{e(x)}</span>' for x in FORMS)
pl = ''.join(f'<span>{e(x)}</span>' for x in PROCS)
if D.EDITION == 'standard':
    LIM = [('کاربر نام‌دار', D.MAX_USERS, 100, False, f'بزرگ‌ترین سناریو {fa(D.MAX_USERS)} کاربر، سقف ۱۰۰'),
           ('نوع فرم و فرایند فعال', NT, 30, False, f'{fa(len(PROCS))} فرایند و {fa(len(FORMS))} فرم، جمعاً {fa(NT)} از سقف ۳۰'),
           (f'{AW} فعال در باشگاه نمایندگان', D.AGENTS or 0, 15, D.AGENTS is None, 'سقف ۱۵ نفر' + ('؛ تعداد در درخواست مشتری نیامده است' if D.AGENTS is None else f'؛ {fa(D.AGENTS)} نفر')),
           ('کاربر فعال باشگاه مشتریان', D.CLUB_USERS or 0, 5000, D.CLUB_USERS is None, 'سقف ۵۰۰۰ نفر' + ('؛ تعداد در درخواست مشتری نیامده است' if D.CLUB_USERS is None else f'؛ {fa(D.CLUB_USERS)} نفر'))]
    right = '<h3>سقف‌های ویرایش استاندارد و وضعیت ' + e(C) + '</h3>' + ''.join(f'<div class="lim"><div class="lh"><b>{e(t)}</b><span>{e(n)}</span></div>{CH.meter(v, m, w=760, h=16, unknown=u)}</div>' for t, v, m, u, n in LIM) + \
        f'<div class="callbox">اگر پس از نیازسنجی یکی از این سقف‌ها رد شود، مثلاً بیش از ۱۵ {AW} فعال در پنل کار کنند، ارتقا از ویرایش استاندارد به پیشرفته ممکن است. همگام‌ساز راهکاران، ارتباط با Power BI و مرکز تماس سیسکو فقط در ویرایش پیشرفته‌اند.</div>'
    title = 'ویرایش استاندارد، نصب درون‌سازمانی'
else:
    right = '<h3>دلیل انتخاب ویرایش پیشرفته</h3><ul class="why">' + ''.join(f'<li>{e(x)}</li>' for x in D.ENTERPRISE_REASONS) + '</ul>'
    title = 'ویرایش پیشرفته (سازمانی)، نصب درون‌سازمانی'
page(corner() + head('نسخه پیشنهادی', title) + f'''
<div class="edi"><div class="l">
 <p>{D.EDITION_TEXT}</p>
 <p><b>مدل نصب:</b> درون‌سازمانی (On-Premise) روی سرور {e(C)}؛ پایگاه داده و پیوست‌ها روی سرورهای {e(C)} ذخیره می‌شوند.</p>
 <div class="tl"><h4>{fa(len(PROCS))} فرایند</h4><div class="tags">{pl}</div><h4>{fa(len(FORMS))} فرم</h4><div class="tags t2">{fl}</div></div>
</div>
<div class="r">{right}</div></div>''' + foot(), key='edition')

# web services and documentation (kb-evidence/api-guide.md)
SV = [('احراز هویت', 'Authentication'), ('هویت حقیقی', 'Person'), ('هویت حقوقی', 'Organization'), ('هویت عمومی و سرنخ', 'Identity'), ('فرصت', 'Opportunity'),
      ('فاکتور و پیش‌فاکتور', 'Invoice'), ('دریافت و پرداخت', 'Receipt / Payment'), ('حساب مالی', 'MoneyAccount'), ('قرارداد', 'Contract'), ('فرم', 'Form'),
      ('وظیفه', 'Task'), ('درخواست پشتیبانی', 'Ticket'), ('قرارملاقات', 'Appointment'), ('ثبت تماس', 'PhoneLog'), ('یادداشت', 'BusinessNote'),
      ('محصولات', 'Product'), ('لیست قیمت', 'PriceList'), ('موجودی', 'Inventory'), ('لینک پرداخت', 'EPay'), ('موتور فرایند', 'ProcessEngine'),
      ('انواع آیتم', 'CrmObjectType'), ('کاربران', 'Users')]
svh = ''.join(f'<div class="sv"><b>{e(p)}</b><bdi>{x}</bdi></div>' for p, x in SV)
scope = ''.join(f'<li>{x}</li>' for x in D.API_SCOPE)
page(corner() + head('یکپارچگی', 'وب‌سرویس و مستندات پیام‌گستر') + f'''
<div class="two">
 <div class="c" style="flex:.85">
  <h3>{icon('link', s=26)} اتصال با وب‌سرویس</h3>
  <ul><li>پیام‌گستر وب‌سرویس مستند را رایگان در اختیار {e(C)} قرار می‌دهد. مستندات هر سرویس، شامل متدها، پارامترها و نمونه درخواست، در <bdi>developer.payamgostar.com</bdi> است.</li>
  <li>سرویس‌های رسمی از نوع SOAP/WCF هستند. برای فرصت، REST هم مستند است: جست‌وجو، و از نسخه <bdi>2.8.7.1</bdi> ایجاد، ویرایش و حذف.</li>
  <li>در موتور فرایند، فعالیت «فراخوانی سرویس» داده را در یک مرحله از فرایند به سامانه دیگر می‌فرستد.</li></ul>
  <h3>{icon('tool', s=26)} دامنه اتصال در این پیشنهاد</h3>
  <ul>{scope}<li>پیام‌گستر خدمات برنامه‌نویسی و شخصی‌سازی ارائه نمی‌دهد، مگر آنکه در پیش‌فاکتور صراحتاً قید شود.</li></ul>
 </div>
 <div class="c">
  <h3>{icon('db', s=26)} ۲۲ سرویس مستند</h3>
  <div class="svg2">{svh}</div>
  <div class="callbox docs"><b>مستندات رسمی وب‌سرویس:</b> <bdi>developer.payamgostar.com</bdi></div>
 </div>
</div>''' + foot(), key='api')

# install (installation-requirements.md, official document 1404/03/15)
HW = [('CPU Benchmark (Multithread)', ['7500', '9500', '12500', '16000', '22000']),
      ('RAM', ['8GB+', '16GB+', '32GB+', '64GB+', '128GB+']),
      ('Network', ['100MB', '1GB', '1GB', '1GB', '1GB']),
      ('Disk (فقط نرم‌افزار خام)', ['20GB', '30GB', '40GB', '60GB', '100GB']),
      ('Read (پیشنهادی)', ['IOPS>50000<br>Throughput>50', '>60000<br>>60', '>70000<br>>70', '>75000<br>>80', '>85000<br>>100']),
      ('Write (پیشنهادی)', ['IOPS>20000<br>Throughput>30', '>25000<br>>35', '>30000<br>>40', '>40000<br>>45', '>50000<br>>50'])]
BANDS = ['۱ تا ۱۰ کاربر', '۱۰ تا ۲۰ کاربر', '۲۰ تا ۵۰ کاربر', '۵۰ تا ۱۰۰ کاربر', '۱۰۰ تا ۱۵۰ کاربر']
HLB = set(D.INSTALL_BANDS)
th = '<th>سخت‌افزار سرور</th>' + ''.join(f'<th class="{"hl" if i in HLB else ""}">{b}</th>' for i, b in enumerate(BANDS))
tr = ''.join('<tr><td>' + e(a) + '</td>' + ''.join(f'<td class="{"hl" if i in HLB else ""}"><bdi>{v}</bdi></td>' for i, v in enumerate(vals)) + '</tr>' for a, vals in HW)
notes = ['با ماژول مرکز تماس یا همگام‌ساز مالی، برای هر کدام ۴ گیگابایت به RAM جدول اضافه شود.',
         'سیستم‌عامل: Windows Server 2022 یا 2025 (Standard یا Datacenter). نصب روی ویندوز کلاینت ممکن نیست.',
         'پایگاه داده: SQL Server 2022 (Enterprise یا Enterprise-Core). Instance اختصاصی را کارشناس پیام‌گستر نصب می‌کند.',
         'در ماشین مجازی، CPU، RAM، دیسک و شبکه Dedicated باشد. مجازی‌سازی روی Hyper-V client پشتیبانی نمی‌شود.',
         'پایگاه داده و نسخه پشتیبان روی دو درایو جدا. بیش از ۵۰ کاربر: وب و پایگاه داده روی دو سرور جدا (پیشنهادی).',
         'پیامک، ایمیل، باشگاه مشتریان، فرم عمومی، لینک اشتراک‌گذاری و اپلیکیشن به اینترنت و IP Static نیاز دارند.',
         'گواهی SSL معتبر روی سرور. نرم‌افزار در شبکه داخلی و اینترنت فقط HTTPS یا فقط HTTP کار می‌کند.',
         'آنتی‌ویروس پیش از نصب نصب شود و مسیرهای پیام‌گستر از اسکن مستثنا شوند. سرور پیام‌گستر خاموش نشود.',
         'نصب حضوری یا ریموت (Remote Desktop یا AnyDesk). محتوای DVD نصب پیش از جلسه روی سرور کپی شود.',
         'اگر پیش‌نیازها در روز نصب آماده نباشد، نصب مجدد طبق تعرفه سایت هزینه دارد.']
nl = ''.join(f'<li>{e(x)}</li>' for x in notes)
page(corner() + head('پیش‌نیازهای سخت‌افزار و نرم‌افزار', 'نصب') + f'''
<table class="inst"><tr>{th}</tr>{tr}</table>
<div class="ilegend"><i></i>{e(D.INSTALL_LEGEND)}</div>
<ul class="inotes">{nl}</ul>
<div class="iread">فایل کامل پیش‌نیازهای نصب پیام‌گستر (ویرایش ۱۴۰۴/۰۳/۱۵) پیوست این پیشنهاد است. پیش از جلسه نصب، آن را کامل مطالعه کنید.</div>''' + foot(), key='install')

# security (technical-architecture-security.md)
page(corner() + head('امنیت و مالکیت داده', 'کنترل دسترسی، ثبت رخداد و مالکیت داده') + f'''
<div class="two three">
 <div class="c"><h3>{icon('key', s=26)} ورود و دسترسی</h3><ul>
  <li>سیاست رمز عبور، قفل و رفع قفل حساب، و مدت نشست قابل تنظیم؛ مدیر نشست هر کاربر را منقضی می‌کند.</li>
  <li>ورود با کد یک‌بارمصرف پیامکی (از نسخه <bdi>2.8.7</bdi>) برای همه کاربران یا کاربر مشخص.</li>
  <li>تعیین IP و ساعت مجاز ورود برای هر کاربر.</li>
  <li>مجوز مشاهده، ایجاد، ویرایش، حذف و خروجی اکسل برای هر نوع آیتم، بر اساس نقش و سمت کاربر؛ دسترسی تا سطح فیلد.</li></ul></div>
 <div class="c"><h3>{icon('shield', s=26)} ثبت رخداد و رمزنگاری</h3><ul>
  <li>سوابق ورود کاربران و فعالیت‌ها (ایجاد، ویرایش، حذف، ارجاع) با زمان، کاربر و IP.</li>
  <li>رمز عبور کاربران به‌صورت Hash ذخیره می‌شود.</li>
  <li>نرم‌افزار با گواهی SSL معتبر فقط روی HTTPS اجرا می‌شود.</li>
  <li>رمزنگاری پایگاه داده (TDE) و رمزنگاری نسخه پشتیبان، با امکانات SQL Server در زیرساخت {e(C)} انجام می‌شود.</li></ul></div>
 <div class="c"><h3>{icon('db', s=26)} مالکیت داده</h3><ul>
  <li>در نصب درون‌سازمانی، پایگاه داده و همه پیوست‌ها روی سرورهای {e(C)} ذخیره می‌شود و پیام‌گستر به آن دسترسی دائمی ندارد.</li>
  <li>دسترسی پشتیبانی پیام‌گستر به سرور فقط با اجازه {e(C)} و برای هر نشست جدا انجام می‌شود.</li>
  <li>نسخه پشتیبان کامل پایگاه داده در اختیار {e(C)} است؛ خروجی اکسل و وب‌سرویس هم در دسترس است.</li>
  <li>گواهی ارزیابی امنیتی محصول از افتا، شماره <bdi>CBP-C1470-0301</bdi>.</li></ul></div>
</div>
''' + flow2('مسیر داده در نصب درون‌سازمانی', [('users', f'کاربران {C} و پنل‌های مشتری و {AW}'), ('shield', 'ارتباط رمزنگاری‌شده HTTPS با گواهی SSL'), ('server', f'وب‌سرور پیام‌گستر روی سرور {C}'), ('db', f'پایگاه داده SQL Server روی سرور {C}'), ('cal', 'نسخه پشتیبان روی درایو جدا')]) + foot(), key='sec')

# LOM (grouped cards; prices only in the pre-invoice)
def codes(c): return '، '.join(f'<bdi>{x}</bdi>' for x in c.split('، ')) if c else ''
lgh = ''.join(f'<div class="lc{" opt" if t == "اختیاری" else ""}"><div class="lch"><b>{e(t)}</b><em>{codes(c)}</em></div><ul>' + ''.join(f'<li>{e(x)}</li>' for x in items) + '</ul></div>' for c, t, items in D.LOM_GROUPS)
page(corner() + head('فهرست اقلام پیشنهادی', D.LOM_TITLE) + f'<div class="lomg">{lgh}</div><div class="ctnote">{D.LOM_NOTE}</div>' + foot(), key='lom')

# roadmap (graphic; hours only, no dates)
HB, HX = D.HOURS_BASE, D.HOURS_EXTRA
RM = [('server', 'نصب', f'نصب نرم‌افزار و SQL Server روی سرور {C} توسط کارشناس پیام‌گستر، حضوری یا ریموت.', f'نرم‌افزار آماده کار روی سرور {C}'),
      ('search', 'نیازسنجی', f'جلسه با مسئول هر فرایند در {C} برای تعیین فرم‌ها، فرایندها، نقش‌ها و دسترسی‌ها.', f'مستند طراحی فرایند برای تأیید {C}'),
      ('flow', 'استقرار فرم‌ها و فرایندها', f'ساخت فرم‌ها، {fa(len(PROCS))} فرایند، کارتابل‌ها، دسترسی‌ها و اعلان‌ها روی نرم‌افزار.', 'فرم‌ها و فرایندهای فعال'),
      ('users', 'ورود هویت‌ها', 'ورود اشخاص و سازمان‌ها با فایل اکسل و کنترل تکرار.', 'پرونده اشخاص و سازمان‌ها'),
      ('cap', 'آموزش', f'آموزش هر نقش روی فرایندهای خود {C}، در جلسات استقرار؛ به‌علاوه وبینارهای گروهی و مرکز دانش.', 'مستند راهنمای کاربران'),
      ('life', 'بهره‌برداری و پشتیبانی', D.SUPPORT_LINE, 'تیکت پشتیبانی')]
xs = [1685 - i*290 for i in range(6)]
LY = 420
svg = [f'<svg class="road" width="1920" height="760" viewBox="0 230 1920 760"><defs><linearGradient id="rl" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#FDD9C4"/><stop offset="1" stop-color="#F26122"/></linearGradient>'
       f'<filter id="rsh" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#B8460F" flood-opacity=".25"/></filter></defs>']
svg.append(f'<rect x="{xs[-1]}" y="{LY-5}" width="{xs[0]-xs[-1]}" height="10" rx="5" fill="url(#rl)"/>')
def bracket(x1, x2, y, label, col):
    return (f'<path d="M{x1} {y+26} V{y} H{x2} V{y+26}" fill="none" stroke="{col}" stroke-width="3" stroke-linecap="round"/>'
            f'<foreignObject x="{x2}" y="{y-58}" width="{x1-x2}" height="50"><div xmlns="http://www.w3.org/1999/xhtml" class="brl" style="color:{col}">{label}</div></foreignObject>')
svg.append(bracket(xs[0]+120, xs[0]-120, 300, 'نصب بار اول رایگان', '#6E747F'))
svg.append(bracket(xs[1]+120, xs[4]-120, 300, f'{fa(HB + HX)} نفرساعت استقرار', '#F26122'))
svg.append(bracket(xs[5]+120, xs[5]-120, 300, 'پشتیبانی سال اول', '#6E747F'))
cols = ['#FAB48C', '#F8A276', '#F7894E', '#F57538', '#F26122', '#D9530F']
for i, (ic, t, d, o) in enumerate(RM):
    x = xs[i]
    svg.append(f'<g filter="url(#rsh)"><polygon points="{hexpts(x, LY, 74)}" fill="{cols[i]}"/></g>')
    svg.append(f'<polygon points="{hexpts(x, LY, 58)}" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="2"/>')
    svg.append(f'<g transform="translate({x-22},{LY-30})">{icon(ic, "#fff", 44, 1.7)}</g>')
    svg.append(f'<text x="{x}" y="{LY+40}" text-anchor="middle" font-family="YB" font-weight="900" font-size="22" fill="#fff">{fa(i+1)}</text>')
svg.append('</svg>')
nodes = ''.join(f'<div class="rm-node" style="left:{x-130}px;top:520px"><h3>{e(t)}</h3><p>{e(d)}</p></div><div class="rm-out" style="left:{x-125}px"><small>خروجی</small>{e(o)}</div>' for x, (ic, t, d, o) in zip(xs, RM))
page(corner() + head('نقشه راه اجرا', 'از نصب تا بهره‌برداری') + ''.join(svg) + nodes +
     f'<div class="rm-foot">ترتیب گام‌ها ثابت است. ساعت هر گام پس از نیازسنجی و با تأیید {e(C)} قطعی می‌شود.</div>' + foot(), key='road')

# deployment unit (implementation.md)
DU = [('مدیر پروژه اختصاصی', f'هماهنگی جلسات استقرار، پیگیری خروجی هر گام و گزارش پیشرفت به {C}.'),
      ('کارشناسان ارشد استقرار', 'دانش‌آموختگان کارشناسی ارشد و دکتری مهندسی صنایع که دوره داخلی استقرار پیام‌گستر را گذرانده‌اند.'),
      ('نیازسنجی پیش از ساخت', 'هر فرایند پیش از پیاده‌سازی با مسئول آن در سازمان مشتری بررسی و مستند می‌شود.'),
      ('کیفیت‌سنجی پس از هر جلسه', 'پس از هر جلسه استقرار، نظر مشتری درباره کیفیت جلسه ثبت و پیگیری می‌شود.'),
      ('بازرسی فنی دوره‌ای', 'تیم فنی تنظیمات و کارایی سامانه مشتری را به‌صورت دوره‌ای بررسی می‌کند.'),
      ('تیم موفقیت مشتری', 'پس از استقرار، یک تیم ۶ نفره با شناخت صنعت مشتری همراه سازمان می‌ماند.')]
dh = ''.join(f'<div class="it"><div class="mi">{icon(i)}</div><div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>' for i, (t, d) in zip(['user', 'cap', 'search', 'check', 'tool', 'users'], DU))
page(corner() + head('واحد استقرار پیام‌گستر', f'تیمی که فرایندهای {C} را روی نرم‌افزار می‌سازد') + f'''
<img class="du-photo" src="{OFF2}">
<div class="du-big"><b>۳۰۰٬۰۰۰</b><span>ساعت استقرار در سازمان‌های مشتری پیام‌گستر</span></div>
<div class="du-list">{dh}</div>''' + foot(), key='du')

# deployment for the customer (hours only: 15 h ~ 2 processes)
pg = ''.join(f'<div><b>{fa(i+1)}</b>{e(p)}</div>' for i, p in enumerate(PROCS))
extra = f' و {fa(HX)} نفرساعت استقرار تکمیلی' if HX else ''
page(corner() + head(f'استقرار برای {C}', 'ساعت استقرار و فرایندهای قابل پیاده‌سازی') + f'''
<div class="dp-hours"><b>{fa(HB + HX)}</b><span>نفرساعت استقرار تخصصی</span>
<p>{fa(HB)} نفرساعت بسته پایه استقرار که همراه خرید ارائه می‌شود{extra}.</p>
<p>مبنای برآورد: هر ۱۵ نفرساعت استقرار، حدود ۲ فرایند. برای {fa(len(PROCS))} فرایند {e(C)}، {fa((HB + HX) // 15)} برابر بسته پایه.</p></div>
<div class="dp-list"><h3>فرایندهایی که در این ساعت‌ها پیاده‌سازی می‌شوند</h3><div class="dp-grid">{pg}</div></div>
<div class="dp-note callbox">{D.DEP_NOTE}</div>''' + foot(), key='dep')

# SLA (only if the customer asked): customer severities mapped to SEV-1/SEV-2 of the chosen package
if getattr(D, 'SLA', None):
    PILL = {'ok': ('برآورده', 'p-ok'), 'up': ('بهتر از درخواست', 'p-up'), 'no': ('برآورده نمی‌شود', 'p-no')}
    PK = D.SLA_PACKAGE
    def sevrow(name, ex, sev, ms):
        mh = ''.join(f'<div class="sm"><div class="smh"><span>{e(t)}</span><i class="pill {PILL[st][1]}">{PILL[st][0]}</i></div><div class="smv"><span>{e(C)}</span><b>{e(rq)}</b></div><div class="smv"><span>{PK}</span><b class="pgv">{e(pg)}</b></div></div>' for t, rq, pg, st in ms)
        return f'<div class="sev"><div class="sn"><b>{e(name)}</b><span>{e(ex)}</span><em><bdi>{sev}</bdi></em></div>{mh}</div>'
    sh = ''.join(sevrow(*x) for x in D.SLA)
    why = ''.join(f'<li>{e(x)}</li>' for x in D.SLA_WHY)
    page(corner() + head('پشتیبانی', 'سطح خدمت پشتیبانی (SLA)') + f'''
<div class="sevs">{sh}</div>
<div class="sla-side"><div class="sla-badge"><span>بسته پیشنهادی</span><b>{PK} SLA</b><em>{e(D.SLA_BADGE)}</em></div><ul class="why">{why}</ul></div>
<ul class="sla-notes2">
 <li>ساعت کاری SLA: شنبه تا چهارشنبه{'، ۹ تا ۱۹' if PK == 'Premium' else '، ۹ تا ۱۷:۳۰'}. پیگیری شبانه‌روزی رخداد بحرانی تعهد نمی‌شود؛ بسته پشتیبانی پلاتینیوم دو تیکت اضطراری در سال و تماس تلفنی دارد.</li>
 <li>SLA پیام‌گستر دو سطح شدت دارد. رخدادی که بیش از ۸۰٪ کاربران را بدون راه‌حل موقت متوقف کند SEV-1 است و بقیه SEV-2؛ سطح هر رخداد را تیم پشتیبانی پیام‌گستر تعیین می‌کند.</li>
 <li>پیوست SLA جداگانه خریده می‌شود و هزینه آن اضافه بر پشتیبانی است. جریمه تأخیر به‌صورت امتیاز اعتباری محاسبه می‌شود.</li>
 <li>در نصب درون‌سازمانی، زیرساخت، دسترس‌پذیری سرور و پشتیبان‌گیری با {e(C)} است و پیام‌گستر مسئول نرم‌افزار است.</li>
</ul>''' + foot(), key='sla')

# back cover (company-facts.md)
back = [cell(0, 0, 'line'), cell(0, 1, 'tint'), cell(1, 0, 'solid'), cell(1, 1, 'img', OFF1, 'xMaxYMid'), cell(1, 2, 'line'),
        cell(2, 0, 'pale'), cell(2, 1, 'or'), cell(3, 0, 'img', OFF2, 'xMinYMid'), cell(3, 1, 'deep'), cell(4, 0, 'tint'), cell(4, 1, 'line')]
page(mosaic(back) + f'''
<img class="b2-logo" src="file://{REPO}logo/payamgostar-light-horizontal-631.png">
<div class="b2-slogan">فناوری در مدار مشتری</div>
<div class="b2-info">
 <div><b>نشانی</b><span>تهران، شهرک غرب، بلوار دادمان، خیابان بهارستان، پلاک ۷، ساختمان تجارت الکترونیک اول</span></div>
 <div><b>کد پستی</b><span>۱۴۶۸۸۱۳۶۴۳</span></div>
 <div><b>تلفن</b><span><bdi dir="ltr">۰۲۱-۴۹۷۱۴</bdi></span></div>
 <div><b>نمابر</b><span><bdi dir="ltr">۰۲۱-۴۴۴۲۰۰۷۵</bdi></span></div>
 <div><b>ایمیل</b><span><bdi>info@payamgostar.com</bdi></span></div>
 <div><b>وب‌سایت</b><span><bdi>www.payamgostar.com</bdi></span></div>
</div>''', 'back2')

doc = f'<!DOCTYPE html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{SYM}{"".join(pages)}</body></html>'
doc = re.sub(r'\{\{P:(\w+)\}\}', lambda m: fa(KEY[m.group(1)]), doc)
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, 'proposal.html'), 'w', encoding='utf-8').write(doc)
print(len(pages), 'pages', TOT, KEY)
