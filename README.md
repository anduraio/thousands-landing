# 1500 Landing Pages

1500 standalone, self-contained landing pages for fictional products across **375 sectors**
(4 products each), rendered in **15 rotating visual themes**.

Every brand, product, person and statistic here is invented — these are demo
templates, not real companies.

## Browse

Open `index.html` — a filterable gallery of all 1500 pages:

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

- `index.html` — filterable gallery of all 1500 pages
- `<sector-slug>/<brand>.html` × 1500 — one landing page per product (nav, hero with fake
  product UI, logo strip, features, how-it-works, stats band, pricing, testimonials, FAQ,
  CTA, footer), filed under one directory per sector — `fintech/`, `ai-and-automation/`, … —
  four pages each, so the repository browses by sector instead of one flat list
- `generate.py` — theme engine, page builder, gallery builder and this README
- `data.py` — the original sector banks and brand list, plus the expander that
  merges the packs below into `SECTORS` / `BRANDS`
- `data2.py` … `data5.py` — 25 full sectors each, with their own features,
  stats, plans, testimonials and FAQs
- `data6.py` … `data10.py` — 50 "lite" sectors each: name, audience, unique
  features and brands, borrowing the rest of their copy from an archetype
- `archetypes.py` — the 12 copy archetypes the lite sectors borrow from

## Regenerate

```bash
python3 generate.py
```

Rewrites every page, `index.html` and this README. Edit the `data*.py` banks to
change copy or add brands; edit `THEMES` in `generate.py` for styling.

## License

MIT — see [LICENSE](LICENSE).
