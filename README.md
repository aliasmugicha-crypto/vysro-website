# VYSRO Website

Official static MVP website for **VYSRO — Operational • Intelligence • Systems**.

**Primary tagline:** Turning Operational Knowledge into Intelligent Systems.

## Deployment

This repository is designed for direct Netlify deployment with no build step.

- Branch: `main`
- Base directory: leave blank
- Build command: leave blank
- Publish directory: `.`

`netlify.toml` contains the same publish configuration.

## Structure

- `index.html` — corporate homepage
- `systems.html` — operational system architectures and dashboard concepts
- `services.html` — service lines
- `industries.html` — SME and technical-sector use cases
- `standards.html` — standards, QA/QC and evidence assurance
- `about.html` — company and founder positioning
- `assets/` — shared brand, styles and JavaScript
- `tests/` — static acceptance checks
- `docs/superpowers/` — controlled design and implementation plan

## Verification

Run:

```bash
node --test tests/site.test.mjs
```
