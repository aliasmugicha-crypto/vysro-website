# VYSRO Website MVP Design

**Date:** 2026-09-12  
**Status:** Approved direction captured for implementation

## Purpose
Build the first deployable VYSRO corporate website in `aliasmugicha-crypto/vysro-website` and deploy it through Netlify. The website must present VYSRO as a serious, globally credible, standards-informed operational intelligence and systems consultancy while remaining practical for African technical businesses and SMEs.

## Governing Positioning
- Permanent descriptor: **Operational • Intelligence • Systems**
- Primary tagline: **Turning Operational Knowledge into Intelligent Systems.**
- Corporate positioning: VYSRO is a standards-informed operational intelligence and systems consultancy. It helps organizations convert standards, engineering knowledge, operational processes, inspections, quality controls, contractual requirements and management expectations into intelligent workflows that generate reliable evidence, improve operational control and support better decisions.
- Secondary line: **Better Evidence. Better Control. Better Decisions.**
- Core doctrine: **Operational event → structured evidence → control or escalation → management decision → assigned action → verified result.**

## Audience
1. Small and medium technical enterprises seeking operational efficiency.
2. Manufacturing and production businesses.
3. Construction and engineering organizations.
4. Ready-mix concrete and materials-production operations.
5. Institutions needing standards, QA/QC, evidence, reporting and management systems.
6. Consulting and implementation partners requiring standards-to-systems architecture.

## Scope and Pages
The MVP is a global multi-page corporate website with:
- `/` — Home
- `/systems.html` — Systems and implementation architectures
- `/services.html` — Service lines
- `/industries.html` — Technical sectors and SME use cases
- `/standards.html` — Standards, QA/QC, evidence and assurance approach
- `/about.html` — Company and founder positioning

A contact CTA appears across the site rather than requiring a separate contact page in this first deploy.

## Homepage Information Architecture
1. Branded header using the approved VYSRO logo.
2. Hero: tagline, corporate proposition, and CTAs to Systems and Services.
3. Problem statement: organizations often have standards, procedures and software but still lack operational visibility, evidence quality, process control and decision-ready information.
4. VYSRO method: Process → Evidence → Control → Intelligence, extended through decision, action and verified result.
5. Service-line overview.
6. Systems showcase with dashboard-style interfaces, especially Ready-Mix Operations & QA/QC.
7. Technical business / SME operational-efficiency section.
8. Standards-embedded operating model.
9. CTA/footer.

## Systems Showcase
Show implementation architectures and prototypes without implying unverified commercial deployment. Include:
- Ready-Mix Concrete Operations & QA/QC Cockpit
- Construction Project Monitoring System
- Manufacturing Quality & Production Control
- SME Operational Cockpit
- Standards-to-Systems Architecture
- Field Research & Evidence Governance
- Executive Decision & Management Review

Dashboard mockups must emphasize large readable metrics, status, evidence, control gates and decisions rather than decorative photography.

## Services
- Operational Intelligence Systems
- Standards-Embedded Workflow Design
- Quality, Inspection & Evidence Systems
- Production & Operational Control
- Technical Reporting & Decision Support
- Systems Architecture & Implementation Support

## Brand and Visual Rules
- Use the approved VYSRO primary logo without recoloring, stretching, rotation, effects or descriptor changes.
- Palette: navy `#0D2240`, green `#1FA84A`, orange `#FF6A00`, white and restrained neutrals.
- Visual style: engineering/executive, information-dense but clean, dashboard-led rather than photography-led.
- Responsive first for Android/mobile, then desktop.

## Content Controls
- Do **not** mention TEMACO or any client/company name on the public website.
- Describe outcomes before tools.
- Do not claim VYSRO implements software unless that is the actual scope.
- Use standards as operational logic, not decorative compliance language.
- Separate proven experience from development-stage concepts.
- Do not imply certification authority, unverified predictive performance or unsupported software-development depth.
- Avoid hype such as “revolutionary”, “world-first” or similar unsupported claims.

## Technical Architecture
- Plain semantic HTML5, CSS and small vanilla JavaScript only.
- No framework, package manager or build command for the MVP.
- Shared stylesheet and script in `/assets`.
- Approved logo asset in `/assets/vysro-logo.svg`, preserving the exact supplied logo image.
- `netlify.toml` sets `publish = "."` and basic security headers.
- All navigation uses relative static paths so Netlify serves the repository root directly.

## Netlify Configuration
- Branch to deploy: `main`
- Base directory: blank
- Build command: blank
- Publish directory: `.`

## Acceptance Criteria
- All six pages render from static files with no build step.
- Navigation works across every page and mobile menu works.
- Approved logo and brand colors are used consistently.
- Homepage clearly states the operational-intelligence positioning and SME/technical-business value.
- Ready-Mix and other system architectures are visibly showcased.
- No TEMACO or client/company names appear.
- Prototype/system language does not overstate deployment evidence.
- Automated content/link checks pass.
- Site is suitable for immediate Netlify deployment from `main`.
