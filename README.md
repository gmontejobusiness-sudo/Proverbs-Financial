# Proverbs Wealth

The marketing website for **Proverbs Wealth** — a financial planning firm.
(The repository name remains `Proverbs-Financial`; the brand is Proverbs Wealth.)

> Align your finances to a *truly wealthy life.*

A fast, self-contained **static site**: no build step, no framework. Editorial,
mostly-white design inspired by a sophisticated, unhurried aesthetic.

## Brand system

- **Palette (three families):** pure white canvas with a whisper of cool
  green-grey, deep forest green anchor, antique gold accent. Defined as CSS
  variables at the top of `styles.css`.
- **Type ("two voices, one mind"):** [Hanken Grotesk](https://fonts.google.com/specimen/Hanken+Grotesk)
  (a modern grotesque) for all roman text — headlines, body, and labels —
  paired with [Cormorant Garamond](https://fonts.google.com/specimen/Cormorant+Garamond)
  *italics* for the emphasized words and quotes. Loaded via Google Fonts.
- **Mark:** the sapling — recreated as inline SVG, so it scales crisply and needs no asset file.

## Positioning

The site is built around the two great chapters of wealth:

1. **Building wealth with intention** — executives with RSUs / equity comp and
   business owners building wealth outside the business.
2. **The five-year horizon** — people within five years of retirement, turning
   a lifetime of saving into a confident, tax-aware income.

…and the philosophy that money is one piece of a *truly wealthy life*
(relationships, finances, health, purpose). Personalized service, built to scale.

## Structure

| File | Purpose |
|------|---------|
| `index.html` | All content and sections. |
| `styles.css` | Design system, layout, responsive rules. |
| `script.js`  | Mobile nav, footer year, contact-form validation. |

## Run locally

```bash
python3 -m http.server 8000
# visit http://localhost:8000
```

## Customize

- **Colors / fonts** — edit the CSS variables at the top of `styles.css`.
- **Copy** — edit directly in `index.html`.
- **Contact form** — currently shows a client-side confirmation only. To collect
  real submissions, wire the success block in `script.js` to a form service
  (Formspree, Netlify Forms) or your own endpoint.

## Deploy

Static, so it runs anywhere:

- **GitHub Pages** — Settings → Pages → serve from the branch root.
- **Netlify / Vercel / Cloudflare Pages** — point at the repo, no build command.

## Note

Contact details (email, phone, hours) and regulatory language are placeholders —
replace with the firm's real, compliant information before going live.


## Site structure

Two ways to view the same content:

**Multi-page site (primary).** Real pages, best for hosting, SEO, and sharing:

| Page | File |
|------|------|
| Home | `index.html` |
| The Two Chapters | `two-chapters.html` |
| How We Help | `how-we-help.html` |
| Our Philosophy | `philosophy.html` |
| Your Team | `team.html` |
| Resources | `resources.html` |
| Truly Wealthy Life | `truly-wealthy-life.html` |
| Schedule a Conversation | `contact.html` |

All pages share `styles.css` and `script.js`. Cross-page links only work when the
files are served together (any static host, or opened from the same folder).

**Long-form single page.** The whole story on one scroll: `onepage.html`
(also available fully self-contained for easy sharing).

> Rebuild the pages after editing content with `build_pages.py`,
> or edit the page files directly.
