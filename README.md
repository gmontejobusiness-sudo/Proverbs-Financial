# Proverbs Financial

A clean, responsive marketing website for **Proverbs Financial**, an
independent, fiduciary financial-planning and wealth-management firm.

Built as a fast, self-contained **static site** — no build step, no
dependencies. Just open `index.html` or host the folder anywhere.

## Structure

| File | Purpose |
|------|---------|
| `index.html` | All page content and sections (hero, services, process, about, why-us, contact, footer). |
| `styles.css` | Styling, layout, and responsive rules. Brand colors defined as CSS variables at the top. |
| `script.js`  | Mobile nav toggle, footer year, and contact-form validation. |

## Run locally

Just open the file:

```bash
open index.html        # macOS
```

Or serve it (recommended, so relative paths behave):

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Customize

- **Brand colors** — edit the `--navy`, `--gold`, etc. variables at the top of `styles.css`.
- **Content** — edit the text directly in `index.html`.
- **Contact form** — currently shows a client-side confirmation only. To collect
  real submissions, wire the form to a service (e.g. Formspree, Netlify Forms) or
  your own endpoint in the submit handler in `script.js`.

## Deploy

This is a static site, so it works on any static host:

- **GitHub Pages** — enable Pages for this repo (Settings → Pages), serving from the branch root.
- **Netlify / Vercel / Cloudflare Pages** — point at the repo; no build command needed.

## Disclaimer

Content is placeholder/sample copy. Replace contact details, statistics, and
regulatory language with your firm's real, compliant information before going live.
