# 500 Landing Pages

500 standalone, self-contained landing pages for fictional products across **125 sectors**
(4 products each), rendered in **15 rotating visual themes**.

## Browse

Open `index.html` — a filterable gallery of all 100 pages:

- **Search** by name, sector or headline
- **Filter** by sector (dropdown or quick pills), theme, and light/dark mode
- **Sort** by sector (grouped), name A→Z / Z→A, theme, or shuffle
- **Grid / list view** toggle
- **Live previews** — hover a card for a scaled live thumbnail; click for a
  full preview modal with desktop/tablet/phone widths, `←`/`→` to browse,
  `Esc` to close, and deep links via `index.html#preview=paystream`
  (also `#view=list`)

Every page works over `file://` with no server and no external assets
(Google Fonts is the only optional network request; pages fall back to
system fonts offline).

## Structure

- `index.html` — filterable gallery of all 500 pages
- `<brand>.html` × 500 — one landing page per product (nav, hero with fake product UI,
  logo strip, features, how-it-works, stats band, pricing, testimonials, FAQ, CTA, footer)
- `data.py` — all copy: sector content banks + 100 brand entries
- `generate.py` — theme engine + page builder

## Regenerate

```bash
python3 generate.py
```

Edit `data.py` to change copy or add brands; edit `THEMES` in `generate.py` for styling.
