# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repo contains two projects for **That Deeper Feeling** (Conscious Intimacy Coaching by Kimberly Bryant):

1. **`website/`** — Next.js 16 marketing website (TypeScript, Tailwind CSS v4, React 19)
2. **`spine-report-generator/`** — Python PDF report generator for the SPINE coaching framework

## Commands

### Website (`website/` directory)

```bash
cd website
npm install        # install dependencies
npm run dev        # dev server at http://localhost:3000
npm run build      # production build
npm run start      # serve production build
npm run lint       # run eslint
```

### SPINE Report Generator (`spine-report-generator/` directory)

```bash
pip install -r requirements.txt
python run_all.py                        # generate all sample reports
python generate_report.py --client sarah # generate single report
python chart_generator.py sarah          # generate charts only
```

## Website Architecture

- **Framework:** Next.js 16 App Router (all routes under `website/app/`)
- **Styling:** Tailwind CSS v4 with CSS custom properties in `website/app/globals.css` using `@theme inline` for Tailwind integration
- **Fonts:** Playfair Display (headings) + Poppins (body), loaded via Google Fonts in `layout.tsx`
- **Layout:** `layout.tsx` wraps all pages with `<Navigation />` and `<Footer />`
- **Components:** `website/components/ui/` (Button, Logo, Accordion) and `website/components/layout/` (Navigation, Footer)
- **API Routes:** `website/app/api/` — checkout (Stripe), curiosity-call, webhook, suites-available
- **Dependencies:** Stripe for payments, Resend for email

### Brand Colors (CSS variables in globals.css)

| Variable | Hex | Role |
|---|---|---|
| `--primary-burgundy` | `#8B3A47` | Main brand, headings |
| `--primary-wine` | `#6B2D3A` | Deeper accents |
| `--accent-terracotta` | `#E8A399` | CTAs, highlights |
| `--neutral-cream` | `#F5F1E8` | Secondary backgrounds |
| `--neutral-soft-white` | `#FDFCF9` | Primary background |

### Brand Voice

- Invitational, not prescriptive ("explore" vs "you must")
- Embodied language ("return to your body", "come home to yourself")
- Professional boundaries clear ("coaching, not therapy")
- Grounded, not performative — "sacred" without being lofty

## SPINE Report Generator Architecture

- `clients_data.py` — Client assessment data dictionaries
- `narrative_generator.py` — `NARRATIVES` dict with per-client personalized text
- `chart_generator.py` — Matplotlib spider/radar charts per domain
- `generate_report.py` — Main PDF generation (ReportLab), 6-page reports
- `style_system.py` — Typography and color constants for PDF styling
- To add a new client: add data in `clients_data.py`, narratives in `narrative_generator.py`, then run `generate_report.py --client [name]`

## Key Conventions

- Use `@/components/...` import alias for website components (configured in tsconfig)
- Pages follow Next.js App Router convention: `app/<route>/page.tsx`
- Button component has three variants: `primary`, `secondary`, `accent`
- Use CSS custom properties (e.g., `var(--primary-burgundy)`) or Tailwind theme colors (e.g., `bg-primary-burgundy`) — both work
- Static assets go in `website/public/`
- Deployed on Vercel with auto-deploy from GitHub
