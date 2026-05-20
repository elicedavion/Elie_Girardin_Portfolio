import re, base64, os

path = "/sessions/elegant-youthful-wright/mnt/outputs/eportfolio_elie_girardin.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# ── Préserver les images existantes ─────────────────────────────────
imgs = re.findall(r'data:image/jpeg;base64,[A-Za-z0-9+/=]{200,}', html)
for i, img in enumerate(imgs):
    html = html.replace(img, f'__B64_{i}__', 1)

# ── Charger les images projets en base64 ────────────────────────────
def b64(p):
    with open(p,"rb") as f: return base64.b64encode(f.read()).decode()

I_MKT  = b64("/sessions/elegant-youthful-wright/mnt/outputs/proj_marketing.jpg")
I_COM  = b64("/sessions/elegant-youthful-wright/mnt/outputs/proj_comm.jpg")
I_VTE  = b64("/sessions/elegant-youthful-wright/mnt/outputs/proj_vente.jpg")

# ── SVG pills (identiques au reste du portfolio) ────────────────────
def psv(d):
    return (f'<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" style="flex-shrink:0;opacity:.6;vertical-align:middle">'
            f'<path stroke-linecap="round" stroke-linejoin="round" d="{d}"/></svg>')

PM  = psv("M10.34 15.84c-.688-.06-1.386-.09-2.09-.09H7.5a4.5 4.5 0 110-9h.75c.704 0 1.402-.03 2.09-.09m0 9.18c.253.962.584 1.892.985 2.783.247.55.06 1.21-.463 1.511l-.657.38c-.551.318-1.26.117-1.527-.461a20.845 20.845 0 01-1.44-4.282m3.102.069a18.03 18.03 0 01-.59-4.59c0-1.586.205-3.124.59-4.59m0 9.18a23.848 23.848 0 018.835 2.535M10.34 6.66a23.847 23.847 0 008.835-2.535")
PC  = psv("M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 01.865-.501 48.172 48.172 0 003.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z")
PV  = psv("M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 00-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 00-16.536-1.84M7.5 14.25L5.106 5.272M6 20.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm12.75 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0z")
PRC = psv("M15.182 15.182a4.5 4.5 0 01-6.364 0M21 12a9 9 0 11-18 0 9 9 0 0118 0zM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75z")

def pill(svg, label):
    return f'<span class="comp-pill">{svg} {label}</span>'

# ── Données des projets ──────────────────────────────────────────────
projects = [
  { "id":"mkt", "title":"SAE Marketing S1",
    "accroche":"Étude de marché avant de lancer le produit innovant DuoBrush.",
    "desc":("Ce projet est une étude de marché réalisée en vue du lancement du Duo Brush, un pinceau à fond de teint innovant intégrant une recharge rechargeable et un mécanisme anti-fuite, conçu avec des matériaux écologiques. La problématique centrale : comment positionner efficacement ce produit sur le marché des cosmétiques en répondant aux nouvelles attentes des consommateurs, tout en valorisant son engagement environnemental ?\n\nL'étude, menée selon les méthodes Pull &amp; Push, couvre une analyse complète du marché cosmétique : structure concurrentielle, analyse des concurrents directs (Max Sauer, Bachca) et indirects (L'Oréal, Sephora), comportements et motivations des consommateurs, ainsi qu'une analyse PESTEL de l'environnement. Elle aboutit à un diagnostic SWOT et à des choix stratégiques de segmentation, ciblage et positionnement autour de deux mots clés : «&nbsp;pratique et durable&nbsp;»."),
    "link":"https://drive.google.com/file/d/1mFpHuVtXQF4nQaP77OnIMPFtM5UkteW9/view?usp=drive_link",
    "cats":"mkt vte",
    "pills_card":[pill(PM,"Étude de marché"), pill(PM,"Analyse concurrentielle"), pill(PM,"SWOT &amp; PESTEL")],
    "pills_modal":[pill(PM,"Étude de marché"), pill(PM,"Analyse concurrentielle"), pill(PM,"SWOT &amp; PESTEL"),
                   pill(PM,"Segmentation / Ciblage / Positionnement"), pill(PV,"Comportements d'achat"), pill(PV,"Motivations consommateurs")],
    "img": I_MKT },
  { "id":"com", "title":"SAE Communication S1",
    "accroche":"Création d'une affiche pour promouvoir une marque d'hygiène et son produit innovant.",
    "desc":("Ce projet consiste en la création d'une affiche publicitaire pour un fond de teint moyen de gamme, à destination d'un public féminin large. L'objectif de la campagne est double : développer la notoriété du produit et construire une image de marque positive auprès de la cible.\n\nLes choix graphiques ont été pensés pour allier accessibilité et désirabilité. Une palette de couleurs sobre et chic, directement tirée des teintes du produit, assure cohérence visuelle et mise en valeur de la gamme. La typographie CopperPlate confère un caractère premium au nom de la marque, tandis que la police Hiragino Sans garantit la lisibilité du slogan. Le packshot met le produit au premier plan sur un fond de teintes variées, illustrant l'inclusivité de la marque.\n\nL'ensemble de ces choix vise à créer un sentiment de luxe accessible, rendant le produit désirable aux yeux du consommateur."),
    "link":"https://drive.google.com/file/d/1pejeLDLinRp4Fj6V4duGzhkIXrNH30Gx/view?usp=sharing",
    "cats":"com",
    "pills_card":[pill(PC,"Création d'affiche"), pill(PC,"Identité visuelle"), pill(PC,"Direction artistique")],
    "pills_modal":[pill(PC,"Création d'affiche"), pill(PC,"Identité visuelle"), pill(PC,"Direction artistique"),
                   pill(PC,"Choix typographiques"), pill(PC,"Cohérence visuelle")],
    "img": I_COM },
  { "id":"vte", "title":"SAE Vente S2",
    "accroche":"Vente de Madeleines Jeannette pour financer une action caritative pour l'hôpital de Caen.",
    "desc":("Ce projet est une opération de vente caritative menée au profit du service pédiatrique du CHU de Caen, en partenariat avec la Biscuiterie Jeannette. Notre équipe de six étudiants a conçu et piloté une campagne de vente complète de A à Z : prospection en porte-à-porte, phoning, vente auprès des pairs et présence sur Instagram, avec une tombola pour dynamiser l'opération.\n\nLe projet couvre l'intégralité du cycle de vente : élaboration d'un argumentaire et d'un script d'appel, anticipation des objections, création des supports (flyer, bon de commande, tableur de suivi), organisation des livraisons et analyse des résultats via des KPIs. Au total, 303,35 € ont été collectés pour 29 ventes, avec un taux de transformation global de 23,4%."),
    "link":"https://drive.google.com/file/d/1gPtnknUOb8uMm2Ebsl0sG2iejT7K5207/view?usp=sharing",
    "cats":"vte com mkt cli",
    "pills_card":[pill(PV,"Prospection multicanale"), pill(PV,"Argumentaire de vente"), pill(PV,"Suivi KPIs")],
    "pills_modal":[pill(PV,"Prospection multicanale"), pill(PV,"Argumentaire de vente"),
                   pill(PV,"Gestion des objections"), pill(PV,"Suivi KPIs"),
                   pill(PC,"Flyer &amp; affiche"), pill(PC,"Animation Instagram"),
                   pill(PM,"Plan d'action structuré"), pill(PRC,"Suivi des commandes")],
    "img": I_VTE },
]

# ── Génération des cartes ────────────────────────────────────────────
def card(p):
    pills = "\n            ".join(p["pills_card"])
    return f"""
      <div class="proj-card" data-categories="{p['cats']}" onclick="openModal('{p['id']}')">
        <div class="proj-img-wrap">
          <img src="data:image/jpeg;base64,{p['img']}" alt="{p['title']}">
        </div>
        <div class="proj-body">
          <h3 class="proj-title">{p['title']}</h3>
          <p class="proj-accroche">{p['accroche']}</p>
          <div class="comp-pills">
            {pills}
          </div>
        </div>
      </div>"""

# ── Génération des modales ───────────────────────────────────────────
def modal(p):
    pills = "\n            ".join(p["pills_modal"])
    desc_html = p["desc"].replace("\n\n","</p><p class=\"modal-para\">")
    return f"""
<div id="modal-{p['id']}" class="modal-overlay" onclick="closeModalOverlay(event,'{p['id']}')">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal('{p['id']}')" aria-label="Fermer">&#x2715;</button>
    <img src="data:image/jpeg;base64,{p['img']}" class="modal-img" alt="{p['title']}">
    <div class="modal-content">
      <h3 class="modal-title">{p['title']}</h3>
      <p class="modal-para">{desc_html}</p>
      <div class="comp-pills" style="margin:1.25rem 0;">
        {pills}
      </div>
      <a href="{p['link']}" target="_blank" rel="noopener" class="modal-link-btn">
        Voir le projet
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"/></svg>
      </a>
    </div>
  </div>
</div>"""

# ── CSS projets ──────────────────────────────────────────────────────
proj_css = """
    /* ── Projets ── */
    #projets { background: var(--light); }
    .proj-filters { display: flex; gap: .5rem; flex-wrap: wrap; margin-bottom: 2.5rem; }
    .filter-btn {
      background: white; color: var(--mid); border: 1px solid var(--border);
      border-radius: 999px; padding: .35rem .95rem; font-size: .82rem; font-weight: 600;
      cursor: pointer; transition: all .2s; display: inline-flex; align-items: center; gap: .35rem;
      font-family: inherit;
    }
    .filter-btn svg { width: 12px; height: 12px; }
    .filter-btn.active, .filter-btn:hover { background: var(--dark); color: white; border-color: var(--dark); }
    .proj-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
    @media (max-width: 960px) { .proj-grid { grid-template-columns: repeat(2,1fr); } }
    @media (max-width: 600px)  { .proj-grid { grid-template-columns: 1fr; } }
    .proj-card {
      background: white; border: 1px solid var(--border); border-radius: var(--radius);
      overflow: hidden; cursor: pointer; transition: box-shadow .25s, transform .25s;
    }
    .proj-card:hover { box-shadow: 0 10px 32px rgba(0,0,0,.13); transform: translateY(-4px); }
    .proj-img-wrap { aspect-ratio: 4/3; overflow: hidden; background: var(--border); }
    .proj-img-wrap img { width:100%; height:100%; object-fit:cover; display:block; transition: transform .35s; }
    .proj-card:hover .proj-img-wrap img { transform: scale(1.05); }
    .proj-body { padding: 1.25rem; }
    .proj-title { font-weight: 700; font-size: .98rem; color: var(--dark); margin-bottom: .4rem; }
    .proj-accroche { font-size: .86rem; color: var(--muted); line-height: 1.55; margin-bottom: .9rem; }
    /* Modal */
    .modal-overlay {
      display: none; position: fixed; inset: 0; z-index: 999;
      background: rgba(0,0,0,.65); backdrop-filter: blur(5px);
      align-items: center; justify-content: center; padding: 1.5rem;
    }
    .modal-overlay.open { display: flex; }
    .modal-box {
      background: white; border-radius: 16px; max-width: 620px; width: 100%;
      max-height: 90vh; overflow-y: auto; position: relative;
      box-shadow: 0 28px 60px rgba(0,0,0,.35); animation: modalIn .25s ease;
    }
    @keyframes modalIn { from{opacity:0;transform:scale(.96) translateY(12px)} to{opacity:1;transform:none} }
    .modal-close {
      position: absolute; top: .85rem; right: .85rem;
      background: white; border: 1px solid var(--border); border-radius: 50%;
      width: 32px; height: 32px; font-size: 1rem; cursor: pointer; color: var(--dark);
      display: flex; align-items: center; justify-content: center; z-index: 2;
      transition: background .2s;
    }
    .modal-close:hover { background: var(--light); }
    .modal-img { width: 100%; aspect-ratio: 4/3; object-fit: cover; display: block; }
    .modal-content { padding: 1.5rem 1.75rem 1.75rem; }
    .modal-title { font-weight: 800; font-size: 1.25rem; color: var(--dark); margin-bottom: 1rem; }
    .modal-para { font-size: .91rem; color: var(--mid); line-height: 1.8; margin-bottom: .75rem; }
    .modal-link-btn {
      display: inline-flex; align-items: center; gap: .5rem;
      background: var(--dark); color: white; text-decoration: none;
      padding: .75rem 1.5rem; border-radius: 999px;
      font-weight: 600; font-size: .9rem; transition: background .2s;
    }
    .modal-link-btn:hover { background: #333; }"""

# ── Section HTML ─────────────────────────────────────────────────────
def fsv(d):  # filtre SVG
    return (f'<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
            f'<path stroke-linecap="round" stroke-linejoin="round" d="{d}"/></svg>')

FSV_M  = fsv("M10.34 15.84c-.688-.06-1.386-.09-2.09-.09H7.5a4.5 4.5 0 110-9h.75c.704 0 1.402-.03 2.09-.09m0 9.18c.253.962.584 1.892.985 2.783.247.55.06 1.21-.463 1.511l-.657.38c-.551.318-1.26.117-1.527-.461a20.845 20.845 0 01-1.44-4.282m3.102.069a18.03 18.03 0 01-.59-4.59c0-1.586.205-3.124.59-4.59m0 9.18a23.848 23.848 0 018.835 2.535M10.34 6.66a23.847 23.847 0 008.835-2.535")
FSV_C  = fsv("M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 01.865-.501 48.172 48.172 0 003.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z")
FSV_V  = fsv("M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 00-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 00-16.536-1.84M7.5 14.25L5.106 5.272M6 20.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm12.75 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0z")
FSV_RC = fsv("M15.182 15.182a4.5 4.5 0 01-6.364 0M21 12a9 9 0 11-18 0 9 9 0 0118 0zM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75z")

cards_html  = "\n".join(card(p) for p in projects)
modals_html = "\n".join(modal(p) for p in projects)

proj_section = f"""
<!-- ── Projets ── -->
<section id="projets">
  <div class="container reveal">
    <span class="section-label">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.75V12A2.25 2.25 0 014.5 9.75h15A2.25 2.25 0 0121.75 12v.75m-8.69-6.44l-2.12-2.12a1.5 1.5 0 00-1.061-.44H4.5A2.25 2.25 0 002.25 6v12a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9a2.25 2.25 0 00-2.25-2.25h-5.379a1.5 1.5 0 01-1.06-.44z"/></svg>
      Travaux académiques
    </span>
    <h2>Projets réalisés</h2>
    <p class="section-subtitle">Travaux menés au cours du BUT TC — cliquez sur un projet pour en savoir plus.</p>

    <div class="proj-filters">
      <button class="filter-btn active" data-filter="all" onclick="filterProjects('all')">Tous</button>
      <button class="filter-btn" data-filter="mkt"  onclick="filterProjects('mkt')">{FSV_M} Marketing</button>
      <button class="filter-btn" data-filter="com"  onclick="filterProjects('com')">{FSV_C} Communication</button>
      <button class="filter-btn" data-filter="vte"  onclick="filterProjects('vte')">{FSV_V} Vente</button>
      <button class="filter-btn" data-filter="cli"  onclick="filterProjects('cli')">{FSV_RC} Relation Client</button>
    </div>

    <div class="proj-grid">
      {cards_html}
    </div>
  </div>
</section>

{modals_html}
"""

# ── JS ────────────────────────────────────────────────────────────────
proj_js = """
  // ── Projets : filtre & modales ──
  function filterProjects(cat) {
    document.querySelectorAll('.proj-card').forEach(c => {
      c.style.display = (cat === 'all' || c.dataset.categories.includes(cat)) ? '' : 'none';
    });
    document.querySelectorAll('.filter-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.filter === cat);
    });
  }
  function openModal(id) {
    document.getElementById('modal-' + id).classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeModal(id) {
    document.getElementById('modal-' + id).classList.remove('open');
    document.body.style.overflow = '';
  }
  function closeModalOverlay(e, id) {
    if (e.target === e.currentTarget) closeModal(id);
  }
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay.open').forEach(m => {
        m.classList.remove('open');
        document.body.style.overflow = '';
      });
    }
  });"""

# ── Injection dans le HTML ────────────────────────────────────────────
# 1. CSS avant le scroll reveal
html = html.replace(
    "    /* Scroll reveal */",
    proj_css + "\n    /* Scroll reveal */"
)

# 2. Section projets avant la section compétences
html = html.replace(
    "\n<!-- ── Compétences ── -->",
    proj_section + "\n<!-- ── Compétences ── -->"
)

# 3. JS avant </script>
html = html.replace("</script>", proj_js + "\n</script>")

# 4. Nav : ajouter lien Projets entre Formations et Compétences
html = html.replace(
    '<li><a href="#formations">Formations</a></li>\n    <li><a href="#competences">Compétences</a></li>',
    '<li><a href="#formations">Formations</a></li>\n    <li><a href="#projets">Projets</a></li>\n    <li><a href="#competences">Compétences</a></li>'
)

# ── Restaurer les images ──────────────────────────────────────────────
for i, img in enumerate(imgs):
    html = html.replace(f'__B64_{i}__', img, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Terminé — {len(html)//1024} KB")
