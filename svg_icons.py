import re

path = "/sessions/elegant-youthful-wright/mnt/outputs/eportfolio_elie_girardin.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# ── Préserver les images base64 ──────────────────────────────────────
imgs = re.findall(r'data:image/jpeg;base64,[A-Za-z0-9+/=]{200,}', html)
for i, img in enumerate(imgs):
    html = html.replace(img, f'__B64_{i}__', 1)

# ── SVG compacts pour les pills (11px, inline) ───────────────────────
def pill_svg(path_d):
    return (f'<svg width="11" height="11" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="2" style="flex-shrink:0;opacity:.6;vertical-align:middle">'
            f'<path stroke-linecap="round" stroke-linejoin="round" d="{path_d}"/></svg>')

P_MARKETING = pill_svg("M10.34 15.84c-.688-.06-1.386-.09-2.09-.09H7.5a4.5 4.5 0 110-9h.75c.704 0 1.402-.03 2.09-.09m0 9.18c.253.962.584 1.892.985 2.783.247.55.06 1.21-.463 1.511l-.657.38c-.551.318-1.26.117-1.527-.461a20.845 20.845 0 01-1.44-4.282m3.102.069a18.03 18.03 0 01-.59-4.59c0-1.586.205-3.124.59-4.59m0 9.18a23.848 23.848 0 018.835 2.535M10.34 6.66a23.847 23.847 0 008.835-2.535")
P_COMM      = pill_svg("M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 01.865-.501 48.172 48.172 0 003.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z")
P_VENTE     = pill_svg("M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 00-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 00-16.536-1.84M7.5 14.25L5.106 5.272M6 20.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm12.75 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0z")
P_CLIENT    = pill_svg("M15.182 15.182a4.5 4.5 0 01-6.364 0M21 12a9 9 0 11-18 0 9 9 0 0118 0zM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75z")
P_OUTILS    = pill_svg("M9 17.25v1.007a3 3 0 01-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0115 18.257V17.25m6-12V15a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 15V5.25m18 0A2.25 2.25 0 0018.75 3H5.25A2.25 2.25 0 003 5.25m18 0H3")

# ── SVG grands pour les en-têtes de groupes (dans la dark box) ───────
def gh_svg(path_d, extra_paths=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" '
            f'stroke="currentColor" stroke-width="2">'
            f'<path stroke-linecap="round" stroke-linejoin="round" d="{path_d}"/>'
            f'{extra_paths}</svg>')

GH_MARKETING = gh_svg("M10.34 15.84c-.688-.06-1.386-.09-2.09-.09H7.5a4.5 4.5 0 110-9h.75c.704 0 1.402-.03 2.09-.09m0 9.18c.253.962.584 1.892.985 2.783.247.55.06 1.21-.463 1.511l-.657.38c-.551.318-1.26.117-1.527-.461a20.845 20.845 0 01-1.44-4.282m3.102.069a18.03 18.03 0 01-.59-4.59c0-1.586.205-3.124.59-4.59m0 9.18a23.848 23.848 0 018.835 2.535M10.34 6.66a23.847 23.847 0 008.835-2.535m0 0A23.74 23.74 0 0018.795 3m.38 1.125a23.91 23.91 0 011.014 5.395m-1.014 8.855c-.118.38-.245.754-.38 1.125m.38-1.125a23.91 23.91 0 001.014-5.395m0-3.46c.495.413.811 1.035.811 1.73 0 .695-.316 1.317-.811 1.73m0-3.46a24.347 24.347 0 010 3.46")
GH_COMM      = gh_svg("M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 01.865-.501 48.172 48.172 0 003.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z")
GH_VENTE     = gh_svg("M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 00-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 00-16.536-1.84M7.5 14.25L5.106 5.272M6 20.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm12.75 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0z")
GH_CLIENT    = gh_svg("M15.182 15.182a4.5 4.5 0 01-6.364 0M21 12a9 9 0 11-18 0 9 9 0 0118 0zM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75zm-.375 0h.008v.015h-.008V9.75zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75zm-.375 0h.008v.015h-.008V9.75z")
GH_OUTILS    = gh_svg("M9 17.25v1.007a3 3 0 01-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0115 18.257V17.25m6-12V15a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 15V5.25m18 0A2.25 2.25 0 0018.75 3H5.25A2.25 2.25 0 003 5.25m18 0H3")

# ── 1. Restaurer les en-têtes de groupes (emoji → dark box + SVG) ────
html = html.replace(
    '<div class="skill-group-icon">🎯</div>\n          <h3>Marketing</h3>',
    f'<div class="skill-group-icon">{GH_MARKETING}</div>\n          <h3>Marketing</h3>'
)
html = html.replace(
    '<div class="skill-group-icon">💬</div>\n          <h3>Communication</h3>',
    f'<div class="skill-group-icon">{GH_COMM}</div>\n          <h3>Communication</h3>'
)
html = html.replace(
    '<div class="skill-group-icon">🤝</div>\n          <h3>Vente</h3>',
    f'<div class="skill-group-icon">{GH_VENTE}</div>\n          <h3>Vente</h3>'
)
html = html.replace(
    '<div class="skill-group-icon">⭐</div>\n          <h3>Relation Client</h3>',
    f'<div class="skill-group-icon">{GH_CLIENT}</div>\n          <h3>Relation Client</h3>'
)
html = html.replace(
    '<div class="skill-group-icon">🛠️</div>\n          <h3>Outils &amp; Logiciels</h3>',
    f'<div class="skill-group-icon">{GH_OUTILS}</div>\n          <h3>Outils &amp; Logiciels</h3>'
)

# ── 2. Remplacer les emojis dans les pills par des SVG inline ─────────
# On remplace "EMOJI " au début du contenu de chaque pill
replacements = [
    ('🎯 ', P_MARKETING + ' '),
    ('💬 ', P_COMM + ' '),
    ('🤝 ', P_VENTE + ' '),
    ('⭐ ', P_CLIENT + ' '),
    ('🛠️ ', P_OUTILS + ' '),
]
for emoji_prefix, svg_prefix in replacements:
    html = html.replace(f'>{emoji_prefix}', f'>{svg_prefix}')

# ── 3. CSS : restaurer dark-box pour les icônes de groupe ────────────
html = html.replace(
    '    .skill-group-icon { font-size: 1.7rem; line-height: 1; }',
    ('    .skill-group-icon { width: 36px; height: 36px; border-radius: 8px; '
     'background: var(--dark); display: flex; align-items: center; justify-content: center; }\n'
     '    .skill-group-icon svg { color: white; width: 18px; height: 18px; }')
)

# ── 4. CSS : pills en flex pour aligner icône + texte ────────────────
html = html.replace(
    '    .comp-pill { background: #f0f0f0; color: var(--dark); border: 1px solid #ddd; border-radius: 8px; padding: .25rem .7rem; font-size: .78rem; font-weight: 500; }',
    ('    .comp-pill { background: #f0f0f0; color: var(--dark); border: 1px solid #ddd; '
     'border-radius: 8px; padding: .25rem .7rem; font-size: .78rem; font-weight: 500; '
     'display: inline-flex; align-items: center; gap: .3rem; }')
)

# ── Restaurer les images ──────────────────────────────────────────────
for i, img in enumerate(imgs):
    html = html.replace(f'__B64_{i}__', img, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Terminé — {len(html)//1024} KB")
