#!/usr/bin/env python3
"""Builds the matthewnothdurft.com preview pages. Run: python3 build.py"""
from pathlib import Path

NAV = [("index.html", "Home"), ("about.html", "About"), ("ventures.html", "Ventures"), ("contact.html", "Contact")]

# (url, name, domain, logo). MJN Realty logo is mock-up option 1 (preview only, not approved).
FOOTER_SITES = [
    ("https://mjnrealty.com", "MJN Realty", "mjnrealty.com", "img/logos/mjnrealty.svg"),
    ("https://41hayes.com", "The Hayes House", "41hayes.com", "img/logos/41hayes.svg"),
    ("https://adirondackcraftworks.com", "Adirondack Craftworks", "adirondackcraftworks.com", "img/logos/adirondackcraftworks.png"),
    ("https://droneestates.com", "Drone Estates", "droneestates.com", "img/logos/droneestates.svg"),
]

def page(fname, title, desc, body):
    script = '<script src="js/contact.js" defer></script>\n' if fname == "contact.html" else ""
    nav = "".join(
        f'<a href="{h}"{" class=\"on\" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV
    )
    sites = "".join(
        f'<li><a href="{u}" rel="noopener"><img class="site-logo" src="{l}" alt="" width="40" height="40"><span class="site-text">{n}<span>{d}</span></span></a></li>' for u, n, d, l in FOOTER_SITES
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=4">
</head>
<body>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="index.html"><span class="mono">MN</span><span class="name">Matthew Nothdurft</span></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap foot">
    <div class="foot-id">
      <p class="foot-name">Matthew Nothdurft</p>
      <p class="foot-place">Adirondack region of New York</p>
    </div>
    <div class="foot-sites">
      <p class="eyebrow light">My other sites</p>
      <ul>{sites}</ul>
    </div>
  </div>
  <div class="wrap foot-base"><span>matthewnothdurft.com</span></div>
</footer>
{script}</body>
</html>
"""

PORTRAIT = """<img class="portrait-photo" src="img/matthew-nothdurft.jpg?v=2" alt="Matthew Nothdurft" width="671" height="894">"""

HOME = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">Lake George &middot; Schroon Lake &middot; the Adirondacks</p>
      <h1>Matthew Nothdurft</h1>
      <p class="lede">Licensed real estate broker and founder of MJN Realty, working in the Adirondack region of New York.</p>
      <p>I focus on seasonal and rental properties and property management around Lake George and Schroon Lake. Away from real estate, I fly DJI drones and make handmade pieces in wood, metal, and other materials through Adirondack Craftworks.</p>
      <div class="actions">
        <a class="btn" href="ventures.html">See what I'm working on</a>
        <a class="btn ghost" href="contact.html">Get in touch</a>
      </div>
    </div>
    <div class="hero-photo">{PORTRAIT}</div>
  </div>
</section>

<section class="band">
  <img src="img/hero-lake.jpg" alt="Adirondack lake with forested hills under a blue sky" loading="lazy">
</section>

<section class="wrap section">
  <div class="section-head">
    <p class="eyebrow">What I do</p>
    <h2>Three things, one region</h2>
  </div>
  <div class="pillars">
    <div class="pillar">
      <span class="num">01</span>
      <h3>Real estate</h3>
      <p>Seasonal and rental properties and property management through MJN Realty.</p>
    </div>
    <div class="pillar">
      <span class="num">02</span>
      <h3>Aerial photography</h3>
      <p>DJI drones, 4K photo and video.</p>
    </div>
    <div class="pillar">
      <span class="num">03</span>
      <h3>Craftwork</h3>
      <p>Handmade pieces in wood, metal, and other materials through Adirondack Craftworks.</p>
    </div>
  </div>
</section>

<section class="wrap section tight">
  <div class="section-head row">
    <div>
      <p class="eyebrow">Ventures</p>
      <h2>Where to find my work</h2>
    </div>
    <a class="text-link" href="ventures.html">All ventures &rarr;</a>
  </div>
  <div class="cards">
    <a class="card" href="https://mjnrealty.com" rel="noopener">
      <img src="img/fall-road.jpg" alt="Fall foliage over a country road" loading="lazy">
      <div class="card-body"><h3>MJN Realty</h3><p>Seasonal and rental properties and property management.</p><span class="go">mjnrealty.com &rarr;</span></div>
    </a>
    <a class="card" href="https://41hayes.com" rel="noopener">
      <img src="img/lake-path.jpg" alt="Wooded path in the Adirondacks" loading="lazy">
      <div class="card-body"><h3>The Hayes House</h3><p>A seasonal rental in Schroon Lake, NY.</p><span class="go">41hayes.com &rarr;</span></div>
    </a>
    <a class="card" href="https://adirondackcraftworks.com" rel="noopener">
      <div class="card-logo"><img src="img/acw-logo.png" alt="Adirondack Craftworks logo" loading="lazy"></div>
      <div class="card-body"><h3>Adirondack Craftworks</h3><p>Handmade pieces in wood, metal, and other materials.</p><span class="go">adirondackcraftworks.com &rarr;</span></div>
    </a>
    <a class="card" href="https://droneestates.com" rel="noopener">
      <img src="img/drone-valley.jpg" alt="Aerial view over wooded Adirondack hills" loading="lazy">
      <div class="card-body"><h3>Drone Estates</h3><p>Drone photos and aerial views, 4K photo and video.</p><span class="go">droneestates.com &rarr;</span></div>
    </a>
  </div>
</section>
"""

ABOUT = f"""
<section class="wrap page-head">
  <p class="eyebrow">About</p>
  <h1>About me</h1>
</section>
<section class="wrap about-grid">
  <div>{PORTRAIT}</div>
  <div class="about-copy">
    <p class="lede">I'm Matthew Nothdurft, a licensed real estate broker and the founder of MJN Realty, based in the Adirondack region of New York.</p>
    <p class="bio">I grew up on the shores of Schroon Lake, kindergarten through twelfth grade, with the mountains for a backyard and the lake for a playground. College took me just down the road to Queensbury, and work carried me farther, to other towns and other lives. But this lake has a way of calling you home. Now I&rsquo;m back, swimming and boating the same clear water and still finding something new around every bend.</p>
    <h2 class="h3">At a glance</h2>
    <ul class="facts">
      <li><span>Work</span>Licensed real estate broker, founder of MJN Realty</li>
      <li><span>Focus</span>Seasonal and rental properties, property management</li>
      <li><span>Area</span>Lake George and Schroon Lake, Adirondack region of New York</li>
      <li><span>In the air</span>DJI drones, 4K photo and video</li>
      <li><span>In the shop</span>Handmade pieces in wood, metal, and other materials through Adirondack Craftworks</li>
    </ul>
  </div>
</section>
<section class="band short">
  <img src="img/fall-road.jpg" alt="Fall foliage over a country road" loading="lazy">
</section>
"""

VENTURES = """
<section class="wrap page-head">
  <p class="eyebrow">Ventures</p>
  <h1>What I'm working on</h1>
  <p class="lede narrow">Real estate, a seasonal home, craftwork, and aerial photography, all rooted in the Adirondacks.</p>
</section>
<section class="wrap ventures">
  <article class="venture">
    <img src="img/fall-road.jpg" alt="Fall foliage over a country road" loading="lazy">
    <div class="v-body">
      <p class="eyebrow">Real estate</p>
      <h2>MJN Realty</h2>
      <p>My brokerage. MJN Realty specializes in seasonal and rental properties and property management in the Adirondack region.</p>
      <a class="btn" href="https://mjnrealty.com" rel="noopener">Visit mjnrealty.com</a>
    </div>
  </article>
  <article class="venture flip">
    <img src="img/lake-path.jpg" alt="Wooded path in the Adirondacks" loading="lazy">
    <div class="v-body">
      <p class="eyebrow">Seasonal stay</p>
      <h2>The Hayes House</h2>
      <p>A seasonal rental in Schroon Lake, NY.</p>
      <a class="btn" href="https://41hayes.com" rel="noopener">Visit 41hayes.com</a>
    </div>
  </article>
  <article class="venture">
    <div class="logo-art"><img src="img/acw-logo.png" alt="Adirondack Craftworks logo" loading="lazy"></div>
    <div class="v-body">
      <p class="eyebrow">Craftwork</p>
      <h2>Adirondack Craftworks</h2>
      <p>Handmade pieces from Adirondack Craftworks, in wood, metal, and whatever else the piece calls for.</p>
      <a class="btn" href="https://adirondackcraftworks.com" rel="noopener">Visit adirondackcraftworks.com</a>
    </div>
  </article>
  <article class="venture flip">
    <img src="img/drone-valley.jpg" alt="Aerial view over wooded Adirondack hills" loading="lazy">
    <div class="v-body">
      <p class="eyebrow">Aerial photography</p>
      <h2>Drone Estates</h2>
      <p>Drone photos and aerial views for homeowners, events, and real estate, flown on DJI drones in 4K photo and video.</p>
      <a class="btn" href="https://droneestates.com" rel="noopener">Visit droneestates.com</a>
    </div>
  </article>
</section>
"""

CONTACT = """
<section class="wrap page-head">
  <p class="eyebrow">Contact</p>
  <h1>Get in touch</h1>
  <p class="lede narrow">For real estate questions, seasonal rentals, or anything else.</p>
</section>
<section class="wrap contact-grid">
  <div class="contact-details">
    <p class="form-intro">Have a project or question? Send a note and I'll get back to you within a day or two.</p>
    <form id="contact-form" class="contact-form" accept-charset="UTF-8">
      <input type="hidden" name="_subject" value="matthewnothdurft.com contact form">
      <div class="hp" aria-hidden="true"><label for="f-gotcha">Leave this field empty</label><input id="f-gotcha" type="text" name="_gotcha" tabindex="-1" autocomplete="off"></div>
      <div class="f-row">
        <div class="f-field"><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name"></div>
        <div class="f-field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      </div>
      <div class="f-field"><label for="f-message">Message</label><textarea id="f-message" name="message" rows="5"></textarea></div>
      <button class="btn" type="submit">Send</button>
      <p id="contact-form-note" class="form-note" role="status" hidden></p>
    </form>
    <ul class="facts">
      <li><span>Phone</span><a href="tel:+15188329174">518-832-9174</a></li>
      <li><span>Area</span>Adirondack region of New York</li>
    </ul>
  </div>
  <div class="contact-side">
    <h2 class="h3">Looking for MJN Realty?</h2>
    <p>Rentals, property management, and real estate questions are best started on the MJN Realty site.</p>
    <a class="btn" href="https://mjnrealty.com" rel="noopener">Go to mjnrealty.com</a>
  </div>
</section>
"""

PAGES = [
    ("index.html", "Matthew Nothdurft", "Matthew Nothdurft, licensed real estate broker and founder of MJN Realty in the Adirondack region of New York.", HOME),
    ("about.html", "About | Matthew Nothdurft", "About Matthew Nothdurft.", ABOUT),
    ("ventures.html", "Ventures | Matthew Nothdurft", "MJN Realty, The Hayes House, Adirondack Craftworks, and Drone Estates.", VENTURES),
    ("contact.html", "Contact | Matthew Nothdurft", "Contact Matthew Nothdurft.", CONTACT),
]

if __name__ == "__main__":
    root = Path(__file__).parent
    for fname, title, desc, body in PAGES:
        html = page(fname, title, desc, body)
        assert "\u2014" not in html and "\u2013" not in html, f"dash in {fname}"
        (root / fname).write_text(html)
        print("wrote", fname)
