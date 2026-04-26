# SPINE Report Generator

Automated PDF report generation system for the **SPINE** healing and coaching framework by **That Deeper Feeling**.

> *Growing the spine that was never allowed to form.*

The SPINE framework helps adults recovering from high-demand religious systems reclaim five internal territories:

- **S** — Sovereignty: "This interior is mine."
- **P** — Power: "I act from my own center."
- **I** — Identity: "I am someone I'm discovering and creating."
- **N** — Nourishment: "My desires and needs sustain me."
- **E** — Embodiment: "I live here, in this body."

## Setup

```bash
pip install -r requirements.txt
```

### Optional: Custom Fonts

For branded typography, download and place these fonts in `assets/fonts/`:

- **EB Garamond** (headings): `EBGaramond-Regular.ttf`, `EBGaramond-Bold.ttf`, `EBGaramond-Italic.ttf`
- **Lato** (body): `Lato-Regular.ttf`, `Lato-Bold.ttf`, `Lato-Italic.ttf`
- **Roboto Mono** (data): `RobotoMono-Regular.ttf`

The system falls back to Helvetica/Courier if custom fonts are not found.

## Usage

### Generate All Four Sample Reports

```bash
python run_all.py
```

### Generate One Report

```bash
python generate_report.py --client sarah
python generate_report.py --client marcus
python generate_report.py --client elena
python generate_report.py --client diane
```

### Generate Charts Only

```bash
python chart_generator.py sarah
```

## Output

Reports are saved to the `reports/` folder:

```
reports/
  sarah_spine_report.pdf
  marcus_spine_report.pdf
  elena_spine_report.pdf
  diane_spine_report.pdf
  sarah_charts/
  marcus_charts/
  elena_charts/
  diane_charts/
```

## Adding a New Client

1. Add a client data dictionary to `clients_data.py` following the existing template
2. Add corresponding narrative entries in `narrative_generator.py` under `NARRATIVES`
3. Run: `python generate_report.py --client [name]`

## Adding the Spine Illustration

Place your spine image file in `assets/images/` named `spine_illustration.png`. Rerun generation — it will be placed automatically on the cover page.

## Report Structure

Each report is 6 pages:

1. **Cover** — Client name, dates, tagline, spine illustration placeholder
2. **Map Overview** — Meta spider chart (5 axes) + domain summary table
3. **Reading Your Shape** — Personalized narrative, central tension quote, anchor acknowledgment
4. **Domain Detail** — Per-domain cards with sub-dimension scores and category assignments
5. **Priority Stack** — Ordered priorities with 8-week timeline
6. **Practice Prescription** — Up to 3 active practices with personalized "why this for you" text

## File Structure

```
spine-report-generator/
  assets/
    fonts/          # Custom fonts (optional)
    images/         # Spine illustration goes here
  reports/          # Generated PDFs output here
  generate_report.py
  clients_data.py
  chart_generator.py
  narrative_generator.py
  run_all.py
  requirements.txt
  README.md
```
