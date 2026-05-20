import re

path = "/sessions/elegant-youthful-wright/mnt/outputs/eportfolio_elie_girardin.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# ── 1. Préserver les images base64 ──────────────────────────────────────────
imgs = re.findall(r'data:image/jpeg;base64,[A-Za-z0-9+/=]{200,}', html)
for i, img in enumerate(imgs):
    html = html.replace(img, f'__B64_{i}__', 1)
print(f"Préservé {len(imgs)} images base64")

# ── 2. Nouveau bloc <style> complet ─────────────────────────────────────────
new_style = """<style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --dark:   #111111;
      --mid:    #444444;
      --muted:  #888888;
      --light:  #f5f5f5;
      --white:  #ffffff;
      --border: #e0e0e0;
      --radius: 12px;
    }
    html { scroll-behavior: smooth; }
    body { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background: var(--white); color: var(--dark); line-height: 1.6; }

    /* ── Nav ── */
    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 2rem; height: 64px;
      background: rgba(255,255,255,0.95); backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
    }
    .nav-logo { font-weight: 800; font-size: 1.1rem; color: var(--dark); }
    .nav-links { display: flex; gap: 2rem; list-style: none; }
    .nav-links a { text-decoration: none; color: var(--mid); font-size: .9rem; font-weight: 500; transition: color .2s; }
    .nav-links a:hover { color: var(--dark); }

    /* ── Hero (halftone doux) ── */
    .hero {
      min-height: 100vh;
      background: #f6f6f6;
      display: flex; align-items: center; justify-content: center;
      padding: 7rem 3rem 4rem;
      position: relative; overflow: hidden;
    }
    /* Grille de points – masquée par un dégradé radial : dense en bas-gauche, disparaît vers le haut-droite */
    .hero::before {
      content: '';
      position: absolute; inset: 0; z-index: 0; pointer-events: none;
      background-image: radial-gradient(circle, #1a1a1a 1.5px, transparent 1.5px);
      background-size: 16px 16px;
      mask-image: radial-gradient(ellipse at 5% 95%, rgba(0,0,0,.75) 0%, rgba(0,0,0,.3) 38%, rgba(0,0,0,0) 65%);
      -webkit-mask-image: radial-gradient(ellipse at 5% 95%, rgba(0,0,0,.75) 0%, rgba(0,0,0,.3) 38%, rgba(0,0,0,0) 65%);
    }
    .hero-inner {
      position: relative; z-index: 1;
      max-width: 960px; width: 100%;
      display: grid; grid-template-columns: 260px 1fr; gap: 3.5rem; align-items: center;
    }
    .hero-photo {
      width: 240px; height: 300px; border-radius: 16px;
      border: 2px dashed #bbb; background: rgba(0,0,0,.04);
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      gap: .75rem; color: #bbb; font-size: .85rem; text-align: center; padding: 1rem;
      cursor: pointer; transition: border-color .2s, background .2s, color .2s;
    }
    .hero-photo:hover { border-color: var(--dark); background: rgba(0,0,0,.07); color: var(--dark); }
    .hero-photo svg { width: 40px; height: 40px; }
    .hero-status {
      display: inline-flex; align-items: center; gap: .5rem;
      background: rgba(0,0,0,.06); border: 1px solid rgba(0,0,0,.18);
      border-radius: 999px; padding: .35rem 1rem;
      font-size: .82rem; color: var(--dark); font-weight: 600; margin-bottom: 1rem;
    }
    .hero-status::before {
      content: ''; width: 8px; height: 8px; border-radius: 50%;
      background: var(--dark); animation: pulse 2s infinite;
    }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.25} }
    .hero h1 { font-size: clamp(2rem, 4vw, 3.2rem); font-weight: 800; color: var(--dark); letter-spacing: -.02em; margin-bottom: .4rem; }
    .hero-title { font-size: 1.1rem; color: var(--muted); font-weight: 500; margin-bottom: 1.25rem; }
    .hero-desc { color: var(--mid); font-size: .97rem; margin-bottom: 2rem; line-height: 1.8; }
    .hero-badges { display: flex; gap: .65rem; flex-wrap: wrap; margin-bottom: 2rem; }
    .badge { background: rgba(0,0,0,.06); border: 1px solid rgba(0,0,0,.15); color: var(--dark); border-radius: 999px; padding: .3rem .85rem; font-size: .8rem; }
    .hero-cta {
      display: inline-flex; align-items: center; gap: .5rem;
      background: var(--dark); color: var(--white); text-decoration: none;
      padding: .8rem 2rem; border-radius: 999px; font-weight: 600; font-size: .95rem;
      box-shadow: 0 4px 20px rgba(0,0,0,.18); transition: transform .2s, background .2s;
    }
    .hero-cta:hover { transform: translateY(-2px); background: #333; }
    @media (max-width: 700px) {
      .hero-inner { grid-template-columns: 1fr; }
      .hero-photo { width: 150px; height: 190px; margin: 0 auto; }
      .hero { padding: 6rem 1.5rem 3rem; }
    }

    /* ── Sections ── */
    section { padding: 5rem 2rem; }
    .container { max-width: 960px; margin: 0 auto; }
    .section-label {
      display: inline-flex; align-items: center; gap: .5rem;
      background: #ececec; color: var(--dark);
      border-radius: 999px; padding: .3rem .9rem;
      font-size: .8rem; font-weight: 700; letter-spacing: .05em; text-transform: uppercase; margin-bottom: 1rem;
    }
    .section-label svg { width: 14px; height: 14px; }
    h2 { font-size: clamp(1.6rem, 3vw, 2.2rem); font-weight: 800; color: var(--dark); margin-bottom: .5rem; }
    .section-subtitle { color: var(--muted); margin-bottom: 3rem; max-width: 520px; }

    /* ── About ── */
    #about { background: var(--light); }
    .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; align-items: start; }
    .about-text p { color: var(--mid); margin-bottom: 1rem; line-height: 1.8; }
    .about-contact { background: white; border-radius: var(--radius); padding: 1.5rem; box-shadow: 0 2px 12px rgba(0,0,0,.06); }
    .about-contact h3 { font-size: 1rem; margin-bottom: 1rem; color: var(--dark); }
    .contact-item { display: flex; align-items: center; gap: .75rem; margin-bottom: .75rem; color: var(--mid); font-size: .92rem; }
    .contact-item svg { color: var(--dark); flex-shrink: 0; width: 18px; height: 18px; }
    .contact-item a { color: var(--dark); text-decoration: none; }
    .contact-item a:hover { text-decoration: underline; }
    @media (max-width: 640px) { .about-grid { grid-template-columns: 1fr; } }

    /* ── Timeline ── */
    .timeline { position: relative; padding-left: 2rem; }
    .timeline::before { content: ''; position: absolute; left: .6rem; top: 0; bottom: 0; width: 2px; background: var(--dark); border-radius: 2px; }
    .tl-item { position: relative; margin-bottom: 2.5rem; }
    .tl-dot { position: absolute; left: -2rem; width: 14px; height: 14px; border-radius: 50%; background: var(--dark); border: 3px solid white; box-shadow: 0 0 0 3px var(--dark); top: .4rem; }
    .tl-card { background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; box-shadow: 0 2px 12px rgba(0,0,0,.04); transition: box-shadow .2s; }
    .tl-card:hover { box-shadow: 0 6px 24px rgba(0,0,0,.1); }
    .tl-header { display: flex; flex-wrap: wrap; gap: .5rem; justify-content: space-between; align-items: flex-start; margin-bottom: .75rem; }
    .tl-title { font-weight: 700; font-size: 1.05rem; color: var(--dark); }
    .tl-company { font-weight: 600; color: var(--mid); font-size: .92rem; }
    .tl-meta { display: flex; gap: .75rem; flex-wrap: wrap; }
    .tl-tag { background: #efefef; color: var(--dark); border-radius: 999px; padding: .2rem .75rem; font-size: .78rem; font-weight: 600; white-space: nowrap; }
    .tl-tag.green { background: #efefef; color: var(--dark); }
    .tl-missions { list-style: none; margin-top: .75rem; }
    .tl-missions li { position: relative; padding-left: 1.1rem; color: var(--mid); font-size: .9rem; margin-bottom: .4rem; line-height: 1.6; }
    .tl-missions li::before { content: '→'; position: absolute; left: 0; color: var(--muted); font-size: .85rem; }
    .tl-competences { margin-top: 1.25rem; border-top: 1px solid var(--border); padding-top: 1rem; }
    .tl-competences-title { font-size: .75rem; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); margin-bottom: .6rem; display: flex; align-items: center; gap: .4rem; }
    .tl-competences-title::before { content: ''; display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: var(--dark); }
    .comp-pills { display: flex; flex-wrap: wrap; gap: .45rem; }
    .comp-pill { background: #f0f0f0; color: var(--dark); border: 1px solid #ddd; border-radius: 8px; padding: .25rem .7rem; font-size: .78rem; font-weight: 500; }

    /* ── Formations ── */
    #formations { background: var(--light); }
    .formations-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 1.5rem; }
    .formation-card { background: white; border-radius: var(--radius); padding: 1.75rem; border: 1px solid var(--border); box-shadow: 0 2px 12px rgba(0,0,0,.04); position: relative; overflow: hidden; transition: box-shadow .2s; }
    .formation-card:hover { box-shadow: 0 6px 24px rgba(0,0,0,.1); }
    .formation-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: var(--dark); }
    .formation-year { font-size: .8rem; font-weight: 700; color: var(--muted); letter-spacing: .05em; margin-bottom: .5rem; }
    .formation-degree { font-weight: 800; font-size: 1rem; color: var(--dark); margin-bottom: .25rem; }
    .formation-school { color: var(--muted); font-size: .88rem; }
    .formation-note { display: inline-block; margin-top: .75rem; background: #ececec; color: var(--dark); border-radius: 999px; padding: .2rem .75rem; font-size: .78rem; font-weight: 600; }

    /* ── Skills ── */
    #competences { background: white; }
    .skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem; }
    .skill-group { background: var(--light); border-radius: var(--radius); padding: 1.5rem; border: 1px solid var(--border); }
    .skill-group-header { display: flex; align-items: center; gap: .6rem; margin-bottom: 1.25rem; }
    .skill-group-icon { width: 36px; height: 36px; border-radius: 8px; background: var(--dark); display: flex; align-items: center; justify-content: center; }
    .skill-group-icon svg { color: white; width: 18px; height: 18px; }
    .skill-group h3 { font-weight: 700; font-size: .95rem; color: var(--dark); }
    .skill-pill-list { display: flex; flex-wrap: wrap; gap: .5rem; }
    .skill-pill { background: white; border: 1px solid var(--border); border-radius: 999px; padding: .3rem .85rem; font-size: .82rem; color: var(--mid); font-weight: 500; }

    /* Languages */
    .lang-bar-wrap { margin-bottom: .85rem; }
    .lang-label { display: flex; justify-content: space-between; font-size: .88rem; margin-bottom: .4rem; }
    .lang-label span:first-child { font-weight: 600; color: var(--dark); }
    .lang-label span:last-child { color: var(--muted); }
    .lang-bar { height: 8px; background: var(--border); border-radius: 999px; overflow: hidden; }
    .lang-fill { height: 100%; border-radius: 999px; background: var(--dark); }

    /* ── Intérêts ── */
    #interets { background: var(--light); }
    .interests-grid { display: flex; flex-wrap: wrap; gap: 1rem; }
    .interest-card { background: white; border-radius: var(--radius); padding: 1.25rem 1.5rem; border: 1px solid var(--border); display: flex; align-items: center; gap: .75rem; font-weight: 600; color: var(--mid); font-size: .95rem; }
    .interest-emoji { font-size: 1.5rem; }

    /* ── Mosaïque dessins ── */
    .mosaic-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: .75rem; }
    @media (max-width: 700px) { .mosaic-grid { grid-template-columns: repeat(2, 1fr); } }
    .mosaic-cell { border-radius: 10px; overflow: hidden; aspect-ratio: 1; background: var(--border); }
    .mosaic-img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform .35s ease, filter .35s ease; }
    .mosaic-cell:hover .mosaic-img { transform: scale(1.06); filter: brightness(1.05); }

    /* ── Contact (halftone clair sur fond sombre) ── */
    #contact {
      background: #111;
      text-align: center;
      position: relative; overflow: hidden;
    }
    #contact::before {
      content: '';
      position: absolute; inset: 0; z-index: 0; pointer-events: none;
      background-image: radial-gradient(circle, rgba(255,255,255,.22) 1px, transparent 1px);
      background-size: 16px 16px;
      mask-image: radial-gradient(ellipse at 90% 10%, rgba(0,0,0,.8) 0%, rgba(0,0,0,.3) 38%, rgba(0,0,0,0) 65%);
      -webkit-mask-image: radial-gradient(ellipse at 90% 10%, rgba(0,0,0,.8) 0%, rgba(0,0,0,.3) 38%, rgba(0,0,0,0) 65%);
    }
    #contact .container { position: relative; z-index: 1; }
    #contact h2 { color: white; }
    #contact .section-subtitle { color: #888; margin: 0 auto 2rem; }
    .contact-cta-grid { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
    .cta-btn { display: inline-flex; align-items: center; gap: .6rem; padding: .85rem 1.75rem; border-radius: 999px; font-weight: 600; font-size: .95rem; text-decoration: none; transition: transform .2s, opacity .2s; }
    .cta-btn.primary { background: white; color: #111; }
    .cta-btn.secondary { background: transparent; color: white; border: 1px solid rgba(255,255,255,.35); }
    .cta-btn.linkedin { background: transparent; color: white; border: 1px solid rgba(255,255,255,.35); }
    .cta-btn:hover { transform: translateY(-2px); opacity: .85; }

    /* ── Footer (halftone) ── */
    footer {
      background: #111; color: #555;
      text-align: center; padding: 1.5rem 2rem; font-size: .85rem;
      position: relative; overflow: hidden; border-top: 1px solid #222;
    }
    footer::before {
      content: '';
      position: absolute; inset: 0; z-index: 0; pointer-events: none;
      background-image: radial-gradient(circle, rgba(255,255,255,.18) 1px, transparent 1px);
      background-size: 12px 12px;
      mask-image: linear-gradient(to right, rgba(0,0,0,.7) 0%, rgba(0,0,0,0) 60%);
      -webkit-mask-image: linear-gradient(to right, rgba(0,0,0,.7) 0%, rgba(0,0,0,0) 60%);
    }
    footer p { position: relative; z-index: 1; }

    /* Scroll reveal */
    .reveal { opacity: 0; transform: translateY(24px); transition: opacity .6s ease, transform .6s ease; }
    .reveal.visible { opacity: 1; transform: none; }
  </style>"""

html = re.sub(r'<style>.*?</style>', new_style, html, flags=re.DOTALL)
print("CSS remplacé")

# ── 3. Emojis sur les comp-pills ─────────────────────────────────────────────
# D'abord les pills sans classe extra (marketing → 🎯)
html = re.sub(r'<span class="comp-pill">([^<]+)</span>', r'<span class="comp-pill">🎯 \1</span>', html)
# Puis les autres (et on normalise la classe)
html = re.sub(r'<span class="comp-pill vente">([^<]+)</span>',  r'<span class="comp-pill">🤝 \1</span>', html)
html = re.sub(r'<span class="comp-pill comm">([^<]+)</span>',   r'<span class="comp-pill">💬 \1</span>', html)
html = re.sub(r'<span class="comp-pill client">([^<]+)</span>', r'<span class="comp-pill">⭐ \1</span>', html)
html = re.sub(r'<span class="comp-pill outils">([^<]+)</span>', r'<span class="comp-pill">🛠️ \1</span>', html)
print("Emojis ajoutés aux pills")

# ── 4. Section label Contact (inline style) ───────────────────────────────────
html = html.replace(
    'style="background:rgba(255,255,255,.1);color:#93c5fd;"',
    'style="background:rgba(255,255,255,.1);color:rgba(255,255,255,.85);"'
)

# ── 5. Restaurer les images base64 ───────────────────────────────────────────
for i, img in enumerate(imgs):
    html = html.replace(f'__B64_{i}__', img, 1)
print(f"Images restaurées")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Terminé — taille: {len(html)//1024} KB")
