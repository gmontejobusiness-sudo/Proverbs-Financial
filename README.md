# Proverbs Financial

The marketing website for **Proverbs Financial** — a boutique financial
planning firm.

> Align your finances to a *truly wealthy life.*

A fast, self-contained **static site**: no build step, no framework. Editorial,
mostly-white design inspired by a sophisticated, unhurried aesthetic.

## Brand system

- **Palette (three families):** pure white canvas with a whisper of cool
  green-grey, deep forest green anchor, antique gold accent. Defined as CSS
  variables at the top of `styles.css`.
- **Type ("two voices, one mind"):** [Hanken Grotesk](https://fonts.google.com/specimen/Hanken+Grotesk)
  (a modern grotesque) for all roman text — headlines, body, and labels —
  paired with [Fraunces](https://fonts.google.com/specimen/Fraunces) *italics*
  for the emphasized words and quotes. Loaded via Google Fonts.
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
