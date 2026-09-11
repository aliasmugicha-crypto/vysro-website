# VYSRO Website MVP v0.1

Mobile-first public business website for VYSRO — Operational • Intelligence • Systems.

## Purpose

The site positions VYSRO as an operational-intelligence and technical-systems consultancy for technical organisations, especially SMEs in manufacturing, production, construction, concrete/materials and engineering.

## Deployment

- Production branch: `main`
- Working/review branch: `design/vysro-mvp-v0.1`
- Netlify publish directory: repository root
- Publish directory: repository root
- No build command is required for v0.1.
- The site is static HTML5 + CSS3 + minimal vanilla JavaScript.

## Content and data rules

- No confidential data belongs in this public repository.
- Operational client names, private screenshots and private documents are excluded unless specifically approved for public release.
- Public dashboard examples use synthetic `Demonstration data` unless a source is public and approved.
- Quantitative claims are governed by `docs/business/CLAIMS_REGISTER.md`.
- Expert profile submissions are handled by Netlify-compatible form processing rather than source-code storage.
- CV upload is intentionally disabled in the ordinary public form because CVs contain personal information; an approved secure file-transfer route must be configured before CV collection is activated.

## Controlled sources

- Institutional identity: `docs/business/WHO_WE_ARE.md`
- Public claims: `docs/business/CLAIMS_REGISTER.md`
- Public content rules: `docs/governance/PUBLIC_CONTENT_RULES.md`
- Expert form security decision: `docs/governance/FORM_SECURITY_DECISION.md`
- Design specification: `docs/superpowers/specs/2026-09-11-vysro-website-mvp-v0.1-design.md`
- Implementation plan: `docs/superpowers/plans/2026-09-11-vysro-website-mvp-v0.1.md`

## Production gate

Do not merge the release candidate into `main` until the mobile Netlify preview has been reviewed and approved.
