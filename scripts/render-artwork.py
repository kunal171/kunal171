#!/usr/bin/env python3
"""Build deterministic, self-contained profile SVGs with light/dark palettes.

Run from anywhere with Python 3. No API token, fonts, JavaScript or build service
is required. CSS motion has a static reduced-motion counterpart inside each SVG.
"""
from math import cos, sin, pi
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    "dark": dict(bg="#0b1020", panel="#10182b", ink="#f4f1ea", muted="#acb6cd", line="#34405b", gold="#f0cc86", violet="#b5a0ff", mint="#85e0cc"),
    "light": dict(bg="#f8f6f0", panel="#efedf7", ink="#1f2942", muted="#56647d", line="#cdcddd", gold="#906019", violet="#6950be", mint="#147f72"),
}


def text(x, y, value, size=18, color="ink", extra="", p=None):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{p[color]}" {extra}>{escape(value)}</text>'


def spark(x, y, r, color, cls=""):
    return f'<path class="{cls}" transform="translate({x} {y})" d="M0 {-r} Q2 -2 {r} 0 Q2 2 0 {r} Q-2 2 {-r} 0 Q-2 -2 0 {-r}Z" fill="{color}"/>'


def start(width, height, title, description, p):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{description}</desc>
<defs>
  <radialGradient id="aura"><stop stop-color="{p['violet']}" stop-opacity=".2"/><stop offset="1" stop-color="{p['bg']}" stop-opacity="0"/></radialGradient>
  <linearGradient id="thread"><stop stop-color="{p['violet']}"/><stop offset=".5" stop-color="{p['gold']}"/><stop offset="1" stop-color="{p['mint']}"/></linearGradient>
</defs>
<style>
text {{font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif}}
.mono {{font-family: ui-monospace, 'SFMono-Regular', Consolas, monospace; letter-spacing: 2px}}
.spin {{transform-box: fill-box; transform-origin: center; animation: orbit 36s linear infinite}}
.reverse {{animation-direction: reverse; animation-duration: 48s}}
.twinkle {{animation: twinkle 6s ease-in-out infinite alternate}}
.late {{animation-delay: -3s}}
.pulse {{animation: pulse 5s ease-in-out infinite}}
.flow {{stroke-dasharray: 5 13; animation: flow 5s linear infinite}}
.orbit-dot {{transform-box: view-box; transform-origin: 600px 170px; animation: orbit 12s linear infinite}}
@keyframes orbit {{to {{transform:rotate(360deg)}}}}
@keyframes twinkle {{from {{opacity:.4}} to {{opacity:1}}}}
@keyframes pulse {{0%,100% {{opacity:.4}} 50% {{opacity:.9}}}}
@keyframes flow {{to {{stroke-dashoffset:-180}}}}
@media (prefers-reduced-motion:reduce) {{.spin,.twinkle,.pulse,.flow,.orbit-dot {{animation:none!important}}}}
</style>
<rect width="{width}" height="{height}" rx="24" fill="{p['bg']}"/>
'''


def header(p):
    s = start(1200, 350, "Kunal — Rust backend engineer", "Trading systems, networking and on-chain infrastructure. A quiet constellation and a compass star accompany the name.", p)
    s += f'<circle cx="962" cy="170" r="225" fill="url(#aura)"/>'
    s += text(64, 57, "KUNAL171", 15, "muted", 'class="mono"', p)
    s += text(59, 176, "Kunal", 108, "ink", 'font-weight="700" letter-spacing="-6"', p)
    s += spark(376, 146, 14, p['gold'])
    s += text(64, 230, "Rust backend engineer", 30, p=p)
    s += f'<path d="M64 261H116" stroke="{p["gold"]}" stroke-width="2"/>'
    s += text(64, 300, "Trading systems  /  Networking  /  On-chain infrastructure", 19, "muted", p=p)
    s += f'<g stroke="{p["line"]}" fill="none"><circle cx="968" cy="165" r="105"/><circle cx="968" cy="165" r="125" stroke-dasharray="2 11"/><path d="M823 165H1113M968 20V310" stroke-dasharray="2 9"/><path d="M845 74L1064 249M864 257L1073 71" opacity=".55"/></g>'
    s += f'<g class="spin"><ellipse cx="968" cy="165" rx="136" ry="46" transform="rotate(-32 968 165)" stroke="url(#thread)" stroke-width="1.4" fill="none"/><circle cx="1076" cy="93" r="5" fill="{p["mint"]}"/></g>'
    s += f'<g class="spin reverse"><path d="M968 76L1057 165L968 254L879 165Z" fill="none" stroke="{p["violet"]}" stroke-opacity=".45"/></g>'
    s += spark(968, 165, 37, p['gold'], "pulse")
    s += f'<circle cx="968" cy="165" r="8" fill="{p["ink"]}"/>'
    for x, y, r, col in [(816, 63, 7, 'gold'), (1119, 268, 8, 'violet'), (1109, 47, 4, 'mint'), (828, 263, 4, 'mint')]:
        s += spark(x, y, r, p[col], "twinkle")
    s += f'<path d="M24 329H1176" stroke="{p["line"]}" stroke-opacity=".6"/>'
    return s + '</svg>\n'


def magic(p):
    s = start(1200, 340, "Systems alchemy", "A conceptual animation: packets, events and orders pass through a glowing compass, then become validated, applied and committed state. This is artwork, not contribution or performance data.", p)
    s += f'<circle cx="600" cy="170" r="172" fill="url(#aura)"/>'
    s += text(42, 45, "SYSTEMS ALCHEMY", 14, "muted", 'class="mono"', p)
    s += text(1158, 45, "01 / A SMALL EXPERIMENT", 12, "muted", 'class="mono" text-anchor="end"', p)
    for i, label in enumerate(['packets', 'events', 'orders']):
        y = 101 + i * 68
        s += f'<rect x="88" y="{y}" width="184" height="46" rx="10" fill="{p["panel"]}" stroke="{p["line"]}"/>'
        s += text(112, y + 29, label, 19, p=p)
        s += f'<path d="M272 {y+23}C380 {y+23} 405 170 480 170" stroke="{p["line"]}" fill="none"/>'
        s += f'<path class="flow" style="animation-delay:-{i*1.7}s" d="M272 {y+23}C380 {y+23} 405 170 480 170" stroke="{p["violet"]}" stroke-width="2" fill="none"/>'
    s += f'<g fill="none" stroke="{p["line"]}"><circle cx="600" cy="170" r="112"/><circle cx="600" cy="170" r="101"/><circle cx="600" cy="170" r="65"/></g>'
    s += f'<g class="spin" fill="none" stroke="{p["violet"]}" stroke-width="1.5"><path d="M600 70L687 220H513Z"/><circle cx="600" cy="170" r="89" stroke-dasharray="20 26"/></g>'
    s += f'<g class="spin reverse" stroke="{p["gold"]}" stroke-width="1.2">'
    for i in range(24):
        a = i * pi / 12
        x1, y1 = 600 + 119*cos(a), 170 + 119*sin(a)
        x2, y2 = 600 + (128 if i % 3 == 0 else 123)*cos(a), 170 + (128 if i % 3 == 0 else 123)*sin(a)
        s += f'<path d="M{x1:.2f} {y1:.2f}L{x2:.2f} {y2:.2f}"/>'
    s += '</g>'
    s += spark(600, 170, 37, p['gold'], "pulse")
    s += f'<circle cx="600" cy="170" r="7" fill="{p["ink"]}"/>'
    s += f'<circle class="orbit-dot" cx="600" cy="58" r="4" fill="{p["mint"]}"/>'
    for i, (label, col) in enumerate([('validate', 'violet'), ('apply', 'gold'), ('commit', 'mint')]):
        y = 101 + i * 68
        s += f'<path d="M720 170C795 170 820 {y+23} 928 {y+23}" stroke="{p["line"]}" fill="none"/>'
        s += f'<path class="flow" style="animation-delay:-{i*1.7+2.5}s" d="M720 170C795 170 820 {y+23} 928 {y+23}" stroke="{p[col]}" stroke-width="2" fill="none"/>'
        s += f'<rect x="928" y="{y}" width="184" height="46" rx="10" fill="{p["panel"]}" stroke="{p["line"]}"/>'
        s += f'<circle cx="952" cy="{y+23}" r="3" fill="{p[col]}"/>'
        s += text(968, y + 29, label, 19, p=p)
    for x, y, r, col in [(407, 80, 8, 'gold'), (790, 265, 7, 'mint'), (758, 67, 5, 'violet'), (432, 274, 4, 'violet')]:
        s += spark(x, y, r, p[col], 'twinkle late')
    s += f'<path d="M42 315H1158" stroke="{p["line"]}" stroke-opacity=".5"/>'
    return s + '</svg>\n'


def mobile_header(p):
    s = start(640, 340, "Kunal — Rust backend engineer", "Trading, networking and on-chain infrastructure, with a compass-star illustration.", p)
    s += text(32, 43, "KUNAL171", 15, "muted", 'class="mono"', p)
    s += text(28, 143, "Kunal", 92, "ink", 'font-weight="700" letter-spacing="-5"', p)
    s += text(32, 202, "Rust backend engineer", 26, p=p)
    s += f'<path d="M32 228H79" stroke="{p["gold"]}" stroke-width="2"/>'
    s += text(32, 274, "Trading systems / Networking", 23, "muted", p=p)
    s += text(32, 309, "On-chain infrastructure", 23, "muted", p=p)
    s += f'<circle cx="507" cy="117" r="112" fill="url(#aura)"/>'
    s += f'<g class="spin" fill="none" stroke="{p["line"]}"><circle cx="507" cy="117" r="73"/><path d="M507 36L588 117L507 198L426 117Z"/><circle cx="507" cy="117" r="88" stroke-dasharray="2 12"/></g>'
    s += spark(507, 117, 32, p['gold'], 'pulse')
    s += spark(598, 222, 8, p['violet'], 'twinkle')
    s += spark(421, 44, 6, p['mint'], 'twinkle late')
    return s + '</svg>\n'


def mobile_magic(p):
    s = start(600, 520, "Systems alchemy", "Packets, events and orders enter a glowing compass; validated, applied and committed state emerge below. Decorative artwork, not live activity data.", p)
    s += text(300, 36, "SYSTEMS ALCHEMY", 16, "muted", 'class="mono" text-anchor="middle"', p)
    s += f'<circle cx="300" cy="260" r="160" fill="url(#aura)"/>'
    for i, (top, bottom, col) in enumerate([('packets', 'validate', 'violet'), ('events', 'apply', 'gold'), ('orders', 'commit', 'mint')]):
        x = 30 + i * 190
        for y, label in [(76, top), (424, bottom)]:
            s += f'<rect x="{x}" y="{y}" width="160" height="46" rx="10" fill="{p["panel"]}" stroke="{p["line"]}"/>'
            s += text(x+80, y+30, label, 22, "ink", 'text-anchor="middle"', p)
        route = f'M{x+80} 122C{x+80} 168 300 131 300 150M300 370C300 389 {x+80} 380 {x+80} 424'
        s += f'<path d="{route}" stroke="{p["line"]}" fill="none"/>'
        s += f'<path class="flow" style="animation-delay:-{i*1.7}s" d="{route}" stroke="{p[col]}" fill="none" stroke-width="2"/>'
    s += f'<circle cx="300" cy="260" r="110" stroke="{p["line"]}" fill="none"/>'
    s += f'<g class="spin" fill="none" stroke="{p["violet"]}"><path d="M300 166L381 307H219Z"/><circle cx="300" cy="260" r="94" stroke-dasharray="18 25"/></g>'
    s += f'<g class="spin reverse" fill="none" stroke="{p["gold"]}"><circle cx="300" cy="260" r="122" stroke-dasharray="1 15"/></g>'
    s += spark(300, 260, 36, p['gold'], 'pulse')
    s += spark(129, 265, 9, p['mint'], 'twinkle')
    s += spark(465, 224, 7, p['violet'], 'twinkle late')
    return s + '</svg>\n'


if __name__ == '__main__':
    (ROOT / 'assets').mkdir(exist_ok=True)
    for theme, palette in PALETTES.items():
        for name, build in [('header', header), ('systems-alchemy', magic), ('header-mobile', mobile_header), ('systems-alchemy-mobile', mobile_magic)]:
            path = ROOT / 'assets' / f'{name}-{theme}.svg'
            path.write_text(build(palette), encoding='utf-8')
            print(path.relative_to(ROOT))
