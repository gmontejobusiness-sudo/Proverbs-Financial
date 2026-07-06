#!/usr/bin/env python3
import re, os, shutil

ROOT = "/home/user/Proverbs-Financial"
# onepage.html is the source of truth (full long-form content).
src = open(os.path.join(ROOT, "onepage.html")).read()

# --- Extract reusable bits ---
font_link = re.search(r'(<link href="https://fonts\.googleapis\.com[^>]*>)', src).group(1)
favicon   = re.search(r'(<link rel="icon"[^>]*>)', src).group(1)
header_src = re.search(r'<header.*?</header>', src, re.S).group(0)
footer_src = re.search(r'<footer.*?</footer>', src, re.S).group(0)
main_inner = re.search(r'<main>(.*?)</main>', src, re.S).group(1)
sections = re.findall(r'<section\b.*?</section>', main_inner, re.S)

def classify(block):
    for key, ident in [
        ('hero','class="hero"'), ('trust','class="section trust"'),
        ('chapters','id="chapters"'), ('approach','id="help"'),
        ('philosophy','id="philosophy"'), ('pillars','class="section pillars"'),
        ('advisors','id="advisors"'), ('resources','id="resources"'),
        ('truly','id="truly"'), ('faq','id="faq"'),
        ('referral','class="section referral"'), ('contact','id="contact"')]:
        if ident in block:
            return key
    return None
sec = {}
for b in sections:
    k = classify(b)
    if k: sec[k] = b

# --- Link rewriting: anchors -> page URLs (for the multi-page version) ---
LINKMAP = [
    ('#chapter-build','two-chapters.html#chapter-build'),
    ('#chapter-retire','two-chapters.html#chapter-retire'),
    ('#chapters','two-chapters.html'),
    ('#help','how-we-help.html'),
    ('#philosophy','philosophy.html'),
    ('#advisors','team.html'),
    ('#resources','resources.html'),
    ('#truly','truly-wealthy-life.html'),
    ('#faq','how-we-help.html#faq'),
    ('#contact','contact.html'),
    ('#top','index.html'),
]
def relink(html):
    for k,v in LINKMAP:
        html = html.replace('href="%s"' % k, 'href="%s"' % v)
    return html

def promote_h1(html):
    # promote the first section/philosophy/truly title from h2 to h1 for SEO
    return re.sub(r'<h2 (class="(?:section-title|philosophy-title|truly-title)"[^>]*)>(.*?)</h2>',
                  r'<h1 \1>\2</h1>', html, count=1, flags=re.S)

# --- Nav / header / footer ---
NAV = [
    ('index.html','Home'),
    ('two-chapters.html','The Two Chapters'),
    ('how-we-help.html','How We Help'),
    ('philosophy.html','Our Philosophy'),
    ('team.html','Your Team'),
    ('resources.html','Resources'),
    ('truly-wealthy-life.html','Truly Wealthy Life'),
]
def header(active):
    items = []
    for href,label in NAV:
        cls = ' class="active"' if href==active else ''
        items.append('          <li><a href="%s"%s>%s</a></li>' % (href,cls,label))
    items.append('          <li><a href="contact.html" class="nav-cta">Schedule a Conversation</a></li>')
    ul = '<ul class="nav-menu" id="nav-menu">\n' + '\n'.join(items) + '\n        </ul>'
    h = re.sub(r'<ul class="nav-menu".*?</ul>', ul, header_src, flags=re.S)
    h = h.replace('href="#top"', 'href="index.html"')
    return h
footer_html = relink(footer_src)

# --- Home-only teaser blocks ---
two_chapters_teaser = '''<section class="section chapters">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">Who we serve</p>
          <h2 class="section-title">One firm,<br /><em>two chapters of life.</em></h2>
          <p class="section-sub">Wealth has two great chapters &mdash; building it, and one day living on it. We walk closely with the people we serve through both.</p>
        </div>
        <div class="chapter-grid">
          <a class="chapter teaser-card" href="two-chapters.html#chapter-build">
            <span class="chapter-index">Chapter One &middot; Building Wealth</span>
            <h3>Building wealth with intention</h3>
            <p>For high-earning professionals and business owners structuring growing wealth &mdash; from RSUs to a business that holds most of your net worth.</p>
            <span class="teaser-link">Explore this chapter &rsaquo;</span>
          </a>
          <a class="chapter chapter-alt teaser-card" href="two-chapters.html#chapter-retire">
            <span class="chapter-index">Chapter Two &middot; The Five-Year Horizon</span>
            <h3>Living the wealth you built</h3>
            <p>For those within five years of retirement &mdash; turning a lifetime of saving into dependable, tax-aware income.</p>
            <span class="teaser-link">Explore this chapter &rsaquo;</span>
          </a>
        </div>
      </div>
    </section>'''

truly_teaser = '''<section class="section truly">
      <div class="wrap">
        <div class="truly-head">
          <p class="eyebrow light">Our movement</p>
          <h2 class="truly-title">Live a <em>Truly Wealthy Life.</em></h2>
          <p class="truly-lead">True wealth is measured by more than your net worth &mdash; it's the freedom to spend your time, energy, and resources on what matters most.</p>
        </div>
        <div class="truly-invite" style="margin-top:2.4rem">
          <a href="truly-wealthy-life.html" class="btn btn-gold">Explore the movement</a>
        </div>
      </div>
    </section>'''

cta_band = '''<section class="section">
      <div class="wrap" style="text-align:center">
        <div class="section-head" style="margin-bottom:1.4rem">
          <p class="eyebrow">Schedule a conversation</p>
          <h2 class="section-title">Let's talk about<br /><em>your wealthy life.</em></h2>
        </div>
        <p style="color:var(--ink-soft);max-width:34rem;margin:0 auto 1.9rem">Whether you're building or five years from retirement, the first step is simply a conversation &mdash; unhurried, and with no obligation.</p>
        <a href="contact.html" class="btn btn-solid">Schedule a conversation</a>
      </div>
    </section>'''

# --- Compose page mains ---
home_main = '\n'.join([relink(sec['hero']), sec['trust'], two_chapters_teaser, truly_teaser, relink(sec['referral']), cta_band])

def page_main(*keys):
    return '\n'.join(promote_h1(relink(sec[k])) if i==0 else relink(sec[k]) for i,k in enumerate(keys))

PAGES = {
    'index.html':              (home_main, "Proverbs Wealth — Financial planning for a truly wealthy life", "Proverbs Wealth is a relationship-driven financial planning firm helping successful individuals and families align their finances with a truly wealthy life.", None),
    'two-chapters.html':       (page_main('chapters'), "The Two Chapters — Proverbs Wealth", "Two chapters of a wealthy life: building it, and one day living on it.", 'two-chapters.html'),
    'how-we-help.html':        (page_main('approach','faq'), "How We Help — Proverbs Wealth", "Thoughtful, relationship-driven financial planning — the best strategy is the one you can live with.", 'how-we-help.html'),
    'philosophy.html':         (page_main('philosophy','pillars'), "Our Philosophy — Proverbs Wealth", "We believe money is one piece of a truly wealthy life.", 'philosophy.html'),
    'team.html':               (page_main('advisors'), "Your Team — Proverbs Wealth", "A real person, for the long run — meet the advisors of Proverbs Wealth.", 'team.html'),
    'resources.html':          (page_main('resources'), "Resources — Proverbs Wealth", "Plain-language guides on the questions we hear most.", 'resources.html'),
    'truly-wealthy-life.html': (promote_h1(relink(sec['truly'])), "Truly Wealthy Life — Proverbs Wealth", "Live a truly wealthy life. Our movement to align finances with what matters most.", 'truly-wealthy-life.html'),
    'contact.html':            (page_main('contact'), "Schedule a Conversation — Proverbs Wealth", "Start a conversation with Proverbs Wealth — unhurried, and with no obligation.", 'contact.html'),
}

HEAD = '''  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta property="og:title" content="Proverbs Wealth" />
  <meta property="og:description" content="Align your finances to a truly wealthy life." />
  <meta property="og:type" content="website" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  {font}
  <link rel="stylesheet" href="styles.css" />
  {favicon}'''

for fname,(main_html,title,desc,active) in PAGES.items():
    html = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n'
            + HEAD.format(title=title, desc=desc, font=font_link, favicon=favicon)
            + '\n</head>\n<body>\n'
            + header(active if active else 'index.html')
            + '\n\n  <main>\n    ' + main_html + '\n  </main>\n\n'
            + footer_html + '\n\n  <script src="script.js"></script>\n</body>\n</html>\n')
    open(os.path.join(ROOT, fname), "w").write(html)
    print("wrote", fname, len(html), "bytes")

print("done; onepage.html preserved")
