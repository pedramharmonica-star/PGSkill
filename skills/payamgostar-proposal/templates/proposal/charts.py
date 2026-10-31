# -*- coding: utf-8 -*-
# Static SVG charts for RTL Persian proposal pages (print). Palette validated with dataviz/validate_palette.js:
#   single series = OR; two categories = OR + BL (all checks pass); ordinal ramp = ORD (passes --ordinal).
OR, BL = '#F26122', '#2C5AA0'
ORD = ['#F7894E', '#F26122', '#D4520F', '#B0420B']
INK, MUTED, GRID, TRACK = '#2B2F36', '#6E747F', '#E8E9EC', '#F1F2F4'
FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
def fa(x): return str(x).translate(FA)
def esc(s): return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

PHYS = {'end': 'start', 'start': 'end', 'middle': 'middle'}   # physical anchor -> anchor for rtl text
def _t(x, y, s, size=14, col=INK, anchor='end', weight=500, extra=''):
    """anchor is physical: 'end' = text ends at x (right-aligned), 'start' = text starts at x and runs right"""
    return f'<text x="{x:.1f}" y="{y:.1f}" direction="rtl" font-family="YB" font-size="{size}" font-weight="{weight}" fill="{col}" text-anchor="{PHYS[anchor]}" dominant-baseline="middle" {extra}>{esc(s)}</text>'

def _bar_left(x_right, y, length, h, col, r=4):
    """bar anchored at x_right (baseline, square) growing left; rounded data-end on the left"""
    if length <= 0: return ''
    r = min(r, h / 2, length)
    x0 = x_right - length
    return (f'<path d="M{x_right:.1f},{y:.1f} H{x0 + r:.1f} Q{x0:.1f},{y:.1f} {x0:.1f},{y + r:.1f} V{y + h - r:.1f} '
            f'Q{x0:.1f},{y + h:.1f} {x0 + r:.1f},{y + h:.1f} H{x_right:.1f} Z" fill="{col}"/>')

def _bar_up(x, y_base, w, length, col, r=4):
    if length <= 0: return ''
    r = min(r, w / 2, length)
    y0 = y_base - length
    return (f'<path d="M{x:.1f},{y_base:.1f} V{y0 + r:.1f} Q{x:.1f},{y0:.1f} {x + r:.1f},{y0:.1f} H{x + w - r:.1f} '
            f'Q{x + w:.1f},{y0:.1f} {x + w:.1f},{y0 + r:.1f} V{y_base:.1f} Z" fill="{col}"/>')

def svg(w, h, body):
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="direction:ltr;overflow:visible">{body}</svg>'

def hbars(items, w=400, label_w=120, bar_h=18, gap=12, col=OR, unit='', vmax=None, size=14, top=4, val_w=46):
    """items: [(label, value)] -> RTL horizontal bars, label on the right, value at the bar end"""
    vmax = vmax or max(v for _, v in items)
    x_base = w - label_w - 10
    span = x_base - val_w
    out = []
    y = top
    for lab, v in items:
        L = span * v / vmax
        out.append(_t(w, y + bar_h / 2, lab, size, INK))
        out.append(_bar_left(x_base, y, L, bar_h, col))
        out.append(_t(x_base - L - 6, y + bar_h / 2, fa(v) + unit, size, MUTED, 'end', 700))
        y += bar_h + gap
    out.insert(0, f'<line x1="{x_base}" y1="{top - 4}" x2="{x_base}" y2="{y - gap + 4}" stroke="{GRID}" stroke-width="1.5"/>')
    return svg(w, y - gap + top + 4, ''.join(out))

def funnel(items, w=300, label_w=96, bar_h=24, gap=8, size=14, val_w=40):
    vmax = items[0][1]
    span = w - label_w - val_w - 20
    cx = val_w + 10 + span / 2
    out, y = [], 4
    for i, (lab, v) in enumerate(items):
        L = span * v / vmax
        out.append(_t(w, y + bar_h / 2, lab, size, INK))
        out.append(f'<rect x="{cx - L / 2:.1f}" y="{y}" width="{L:.1f}" height="{bar_h}" rx="4" fill="{ORD[min(i, len(ORD) - 1)]}"/>')
        out.append(_t(val_w, y + bar_h / 2, fa(v), size, MUTED, 'end', 700))
        y += bar_h + gap
    return svg(w, y - gap + 8, ''.join(out))

def columns(labels, values, w=420, h=200, col=OR, unit='', size=13, show=None):
    """vertical columns; values labeled only on first, last and max (selective direct labels)"""
    pad_b, pad_t = 26, 22
    n = len(values); vmax = max(values) * 1.1
    cw = (w - 8) / n; bw = cw * 0.52
    base = h - pad_b
    show = show if show is not None else {0, n - 1, values.index(max(values))}
    out = [f'<line x1="0" y1="{base}" x2="{w}" y2="{base}" stroke="{GRID}" stroke-width="1.5"/>']
    for i, (lab, v) in enumerate(zip(labels, values)):
        x = w - 4 - cw * (i + 1) + (cw - bw) / 2   # RTL: first column on the right
        L = (base - pad_t) * v / vmax
        out.append(_bar_up(x, base, bw, L, col))
        out.append(_t(x + bw / 2, base + 15, lab, size, MUTED, 'middle', 500))
        if i in show:
            out.append(_t(x + bw / 2, base - L - 11, fa(v) + unit, size, INK, 'middle', 700))
    return svg(w, h, ''.join(out))

def line(labels, values, w=420, h=200, col=OR, unit='', size=13, ymax=None):
    pad_b, pad_t, pad_x = 26, 26, 22
    n = len(values); ymax = ymax or max(values) * 1.25
    base = h - pad_b
    xs = [w - pad_x - (w - 2 * pad_x) * i / (n - 1) for i in range(n)]   # RTL time axis
    ys = [base - (base - pad_t) * v / ymax for v in values]
    out = []
    for g in (0.5, 1.0):
        gy = base - (base - pad_t) * g
        out.append(f'<line x1="0" y1="{gy:.1f}" x2="{w}" y2="{gy:.1f}" stroke="{GRID}" stroke-width="1" stroke-dasharray="3 4"/>')
        out.append(_t(2, gy - 9, fa(round(ymax * g)) + unit, 11, MUTED, 'start', 500))
    out.append(f'<line x1="0" y1="{base}" x2="{w}" y2="{base}" stroke="{GRID}" stroke-width="1.5"/>')
    pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
    out.append(f'<polygon points="{xs[0]:.1f},{base} {pts} {xs[-1]:.1f},{base}" fill="{col}" fill-opacity=".10"/>')
    out.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>')
    for i, (x, y) in enumerate(zip(xs, ys)):
        out.append(_t(x, base + 15, labels[i], size, MUTED, 'middle', 500))
    out.append(f'<circle cx="{xs[-1]:.1f}" cy="{ys[-1]:.1f}" r="5.5" fill="{col}" stroke="#fff" stroke-width="2"/>')
    out.append(_t(xs[-1] + 10, ys[-1] - 16, fa(values[-1]) + unit, size + 1, INK, 'start', 700))
    return svg(w, h, ''.join(out))

SEGN = [0]
def seg100(segs, w=420, h=22, size=14, labels=True):
    """segs: [(label, value, color)] -> one 100% bar (RTL, first segment on the right), 2px gaps, rounded ends"""
    SEGN[0] += 1; cid = f'sg{SEGN[0]}'
    tot = sum(v for _, v, _ in segs)
    n = len(segs)
    out = [f'<defs><clipPath id="{cid}"><rect x="0" y="0" width="{w}" height="{h}" rx="4"/></clipPath></defs><g clip-path="url(#{cid})">']
    x = w
    pos = []
    for lab, v, col in segs:
        L = (w - 2 * (n - 1)) * v / tot
        out.append(f'<rect x="{x - L:.1f}" y="0" width="{L:.1f}" height="{h}" fill="{col}"/>')
        pos.append((x, L)); x -= L + 2
    out.append('</g>')
    if labels:
        ly = h + 20
        for i, ((lab, v, col), (xr, L)) in enumerate(zip(segs, pos)):
            if i == 0: ax, anc = xr, 'end'
            elif i == n - 1: ax, anc = xr - L, 'start'
            else: ax, anc = xr - L / 2, 'middle'
            sw = f'<rect x="{(ax - 10) if anc == "end" else ax if anc == "start" else ax - 5:.1f}" y="{ly - 5}" width="10" height="10" rx="2" fill="{col}"/>'
            tx = ax - 16 if anc == 'end' else (ax + 16 if anc == 'start' else ax)
            out.append(sw + _t(tx, ly, f'{lab} {fa(v)}', size, INK, anc, 600))
    return svg(w, h + (34 if labels else 0), ''.join(out))

def stacked(rows, w=1000, label_w=280, bar_h=22, gap=16, cols=(OR, BL), size=17, total_w=60):
    """rows: [(label, [v1, v2])] absolute stacked bars, RTL; 2px gap between segments; total at the end"""
    vmax = max(sum(v) for _, v in rows)
    x_base = w - label_w - 12
    span = x_base - total_w
    out, y = [], 4
    for lab, vals in rows:
        out.append(_t(w, y + bar_h / 2, lab, size, INK))
        x = x_base
        nz = [j for j, v in enumerate(vals) if v > 0]
        for j in nz:
            L = span * vals[j] / vmax
            if j == nz[-1]:
                out.append(_bar_left(x, y, L, bar_h, cols[j]))
            else:
                out.append(f'<rect x="{x - L:.1f}" y="{y}" width="{L:.1f}" height="{bar_h}" fill="{cols[j]}"/>')
            x -= L + 2
        out.append(_t(x - 8, y + bar_h / 2, fa(sum(vals)), size, MUTED, 'end', 700))
        y += bar_h + gap
    out.insert(0, f'<line x1="{x_base}" y1="0" x2="{x_base}" y2="{y - gap + 8}" stroke="{GRID}" stroke-width="1.5"/>')
    return svg(w, y - gap + 10, ''.join(out))

def meter(value, vmax, w=420, h=16, col=OR, unknown=False):
    out = [f'<rect x="0" y="0" width="{w}" height="{h}" rx="{h / 2}" fill="{TRACK}"/>']
    if unknown:
        out.append(f'<defs><pattern id="hatch" width="10" height="10" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><rect width="4" height="10" fill="#D6D8DD"/></pattern></defs>'
                   f'<rect x="0" y="0" width="{w}" height="{h}" rx="{h / 2}" fill="url(#hatch)"/>')
    else:
        L = w * min(value / vmax, 1)
        out.append(f'<rect x="{w - L:.1f}" y="0" width="{L:.1f}" height="{h}" rx="{h / 2}" fill="{col}"/>')
    return svg(w, h, ''.join(out))

def legend(items, size=15):
    return '<div class="lgd">' + ''.join(f'<span><i style="background:{c}"></i>{esc(t)}</span>' for t, c in items) + '</div>'
