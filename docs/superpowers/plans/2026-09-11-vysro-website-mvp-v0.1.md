# VYSRO Website MVP v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and deploy a mobile-first VYSRO public website that positions VYSRO as an operational-intelligence and technical-systems consultancy for technical SMEs, demonstrates selected systems and evidence, recruits experts, and is deployable from GitHub to Netlify.

**Architecture:** A lightweight static multi-page site built with semantic HTML5, one shared responsive CSS file and minimal vanilla JavaScript. Public pages contain only approved or synthetic/demo content. Expert submissions use Netlify-compatible form handling and never store CVs or personal information in the public repository.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, GitHub, Netlify, Netlify Forms.

**Spec:** `docs/superpowers/specs/2026-09-11-vysro-website-mvp-v0.1-design.md`

## Global Constraints

- Primary design target: Android/mobile first; responsive desktop second.
- Preserve the real VYSRO logo exactly as supplied; do not recreate or reinterpret the logo.
- Core identity: `Operational • Intelligence • Systems`.
- Tagline: `Turning Operational Knowledge into Intelligent Systems.`
- Governing philosophy: `The operation comes before the software.`
- Public operating logic: `Process → Evidence → Control → Intelligence → Value`.
- Primary business audience includes technical SMEs in manufacturing, production, construction, concrete/materials and engineering.
- Primary CTAs: `Improve Your Operations` and `Join Our Expert Pool`.
- Do not publicly name operational clients unless explicitly approved.
- Use synthetic/demo data for public dashboard demonstrations unless data is public and approved.
- Do not store CVs or personal expert data in GitHub.
- Do not present future KOSH/VERA/AI capabilities as completed products.
- No React, Next.js or other frontend framework in v0.1.
- No confidential database, client portal or authentication in v0.1.
- Avoid autoplay video and large media dependencies.

---

## Planned Production Files

```text
/
├── index.html                     # mobile-first landing page and business front door
├── who-we-are.html                # identity, philosophy, capability model
├── operational-systems.html       # SME systems and dashboard demonstrations
├── standards-research.html        # standards, SizAfrica and materials research
├── experts.html                   # expert-network value proposition + Netlify intake
├── insights.html                  # initial publication/technical-note surface
├── contact.html                   # business enquiry surface
├── engineering-office.html        # clearly labelled future/under-development capability
├── assets/
│   ├── css/
│   │   └── styles.css             # complete shared design system and responsive layout
│   ├── js/
│   │   └── main.js                # mobile navigation and small progressive enhancements only
│   ├── images/                    # approved or synthetic public visual assets
│   └── logo/                      # real VYSRO logo asset only
├── docs/
│   ├── business/
│   │   ├── WHO_WE_ARE.md          # controlled institutional copy source
│   │   └── CLAIMS_REGISTER.md     # quantitative/public-claim governance
│   ├── website/
│   │   └── CONTENT_REGISTER.md    # page/section/content-status register
│   └── governance/
│       └── PUBLIC_CONTENT_RULES.md# client/privacy/demo-data rules
├── netlify.toml                   # static deployment configuration
└── README.md                      # repository/deployment notes
```

---

### Task 1: Create the public-site shell and controlled content registers

**Files:**
- Create: `index.html`
- Create: `who-we-are.html`
- Create: `operational-systems.html`
- Create: `standards-research.html`
- Create: `experts.html`
- Create: `insights.html`
- Create: `contact.html`
- Create: `engineering-office.html`
- Create: `assets/css/styles.css`
- Create: `assets/js/main.js`
- Create: `docs/business/WHO_WE_ARE.md`
- Create: `docs/business/CLAIMS_REGISTER.md`
- Create: `docs/website/CONTENT_REGISTER.md`
- Create: `docs/governance/PUBLIC_CONTENT_RULES.md`

**Interfaces:**
- Consumes: approved design specification.
- Produces: stable page filenames and content-governance documents used by all later tasks.

- [ ] **Step 1: Create each HTML page with the same semantic shell**

Each page must contain:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#ffffff">
  <link rel="stylesheet" href="assets/css/styles.css">
  <script defer src="assets/js/main.js"></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header"></header>
  <main id="main"></main>
  <footer class="site-footer"></footer>
</body>
</html>
```

For pages inside the repository root, all CSS/JS links use the paths above.

- [ ] **Step 2: Add the controlled institutional source file**

`docs/business/WHO_WE_ARE.md` must record:

```markdown
# VYSRO — Controlled Institutional Identity

## Descriptor
Operational • Intelligence • Systems

## Tagline
Turning Operational Knowledge into Intelligent Systems.

## Governing principle
The operation comes before the software.

## Operating logic
Process → Evidence → Control → Intelligence → Value

## Market position
VYSRO helps technical organisations—especially SMEs in manufacturing, production and construction—turn operational knowledge into practical, evidence-driven systems that improve efficiency, quality, compliance, traceability and management visibility.

## Supporting capabilities
- Operational Efficiency & Technical Systems
- Standards & Quality Infrastructure
- Engineering & Technical Assurance
- Research & Industrial Innovation
- Expert Network
```

- [ ] **Step 3: Add the initial claims register**

`docs/business/CLAIMS_REGISTER.md` must contain:

```markdown
# Public Claims Register

| Claim | Status | Public wording rule |
| --- | --- | --- |
| 1,122 registrations in SizAfrica pilot | approved candidate | Attribute specifically to SizAfrica pilot |
| 9 pilot districts | approved candidate | Attribute specifically to SizAfrica pilot |
| 215+ standards supported/developed/reviewed | controlled | Must distinguish professional/team experience from VYSRO institutional achievement |
| Countries potentially impacted by anthropometric work | blocked | Do not publish until separately evidenced |
| CO2 reduction / economic impact | blocked | Do not publish until separately evidenced |
```

- [ ] **Step 4: Add public content rules**

`docs/governance/PUBLIC_CONTENT_RULES.md` must state:

```markdown
# Public Content Rules

1. No operational client names unless specifically approved.
2. No confidential client logos, screenshots, records or documents.
3. Synthetic dashboard data must be labelled `Demonstration data`.
4. Existing work and under-development capabilities must be visibly distinguishable.
5. AI-generated imagery must not imply a fabricated real project or client engagement.
6. CVs and expert personal data must never enter this repository.
7. Public quantitative claims must be listed in `docs/business/CLAIMS_REGISTER.md` before publication.
```

- [ ] **Step 5: Add the page-content register**

`docs/website/CONTENT_REGISTER.md` must track the initial sections:

```markdown
# Website Content Register

| Page | Required sections | Status |
| --- | --- | --- |
| Home | hero; SME problem; methodology; evidence numbers; environments; systems; public evidence; experts; insights; contact | planned |
| Who We Are | identity; philosophy; capabilities; operating logic | planned |
| Operational Systems | SME cockpit; ready-mix; precast; ISO readiness; field/MEL; evidence intelligence | planned |
| Standards & Research | standards lifecycle; SizAfrica; materials research | planned |
| Expert Network | proposition; who joins; process; intake form; privacy | planned |
| Insights | technical notes/publications starter surface | planned |
| Contact | business enquiry form/contact route | planned |
| Engineering Office | under-development notice and scope | planned |
```

- [ ] **Step 6: Verify the shell manually**

Check that every page contains exactly one `<main id="main">`, includes the viewport meta tag, and references the shared CSS and JS without broken paths.

- [ ] **Step 7: Commit**

Commit message:

```text
feat: scaffold VYSRO website MVP
```

---

### Task 2: Build the mobile-first design system and navigation

**Files:**
- Modify: `assets/css/styles.css`
- Modify: `assets/js/main.js`
- Modify: all root HTML pages

**Interfaces:**
- Consumes: stable page filenames from Task 1.
- Produces: shared navigation, footer, design tokens and mobile responsive primitives used by every page.

- [ ] **Step 1: Define CSS design tokens**

Create `:root` variables for spacing, typography, borders, shadows, radii and brand colours. Until the exact logo palette is extracted from the approved logo asset, use neutral semantic token names (`--brand-primary`, `--brand-dark`, `--surface`, `--text`) rather than hard-coding a fabricated brand identity in page markup.

- [ ] **Step 2: Implement mobile-first layout primitives**

Required classes:

```text
.container
.section
.section--compact
.eyebrow
.display
.lead
.grid
.card
.metric
.button
.button--primary
.button--secondary
.tag
.notice
.dashboard-demo
```

Base layout must work at 360px width without horizontal scrolling.

- [ ] **Step 3: Add consistent header navigation to every page**

Navigation labels:

```text
Home
Who We Are
Operational Systems
Standards & Research
Expert Network
Insights
Contact
```

Include two CTA links where space allows:

```text
Improve Your Operations
Join Our Expert Pool
```

On mobile, use one accessible menu button with `aria-expanded` and a collapsible nav panel.

- [ ] **Step 4: Implement the menu script**

`assets/js/main.js` must only handle progressive enhancements such as the mobile menu. It must not be required for the core content to be readable.

Expected logic:

```js
const menuButton = document.querySelector('[data-menu-button]');
const menu = document.querySelector('[data-menu]');

if (menuButton && menu) {
  menuButton.addEventListener('click', () => {
    const expanded = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!expanded));
    menu.hidden = expanded;
  });
}
```

- [ ] **Step 5: Add a shared footer pattern to every page**

Footer must include:

- VYSRO descriptor;
- quick navigation;
- `Improve Your Operations`;
- `Join Our Expert Pool`;
- privacy/confidentiality note where relevant;
- copyright line generated as static 2026 text in v0.1.

- [ ] **Step 6: Manual responsive test**

Test widths:

```text
360px
412px
768px
1024px
1440px
```

Expected: no horizontal scrolling, usable menu, readable text, CTA buttons remain tappable.

- [ ] **Step 7: Commit**

Commit message:

```text
feat: add mobile-first VYSRO design system
```

---

### Task 3: Build the homepage as the primary business conversion surface

**Files:**
- Modify: `index.html`
- Modify: `assets/css/styles.css`
- Modify: `docs/website/CONTENT_REGISTER.md`

**Interfaces:**
- Consumes: shared navigation/design system.
- Produces: homepage section patterns reused on internal pages.

- [ ] **Step 1: Build the hero**

Required content:

```text
Operational • Intelligence • Systems
Turning Operational Knowledge into Intelligent Systems.
VYSRO helps technical organisations—especially SMEs in manufacturing, production and construction—improve operational efficiency, quality, compliance, traceability and management visibility through practical, evidence-driven systems.
```

Primary CTA links to `contact.html#operations` with label `Improve Your Operations`.

Secondary CTA links to `experts.html` with label `Join Our Expert Pool`.

The hero must reserve an explicit logo slot that uses the real VYSRO logo asset once retrieved; do not create a substitute mark.

- [ ] **Step 2: Build the SME problem section**

Show the operational fragmentation pattern:

```text
Spreadsheets
Paper records
WhatsApp
Production logs
Quality records
Standards
Management reports
```

Lead with the idea that the business often already has knowledge; VYSRO structures and connects it.

- [ ] **Step 3: Build the methodology section**

Use five cards or steps:

```text
Process
Evidence
Control
Intelligence
Value
```

Include the line `The operation comes before the software.`

- [ ] **Step 4: Build the evidence-number strip**

Only include:

```text
1,122 — SizAfrica pilot registrations
9 — pilot districts
215+ — standards supported/developed/reviewed through relevant professional experience
```

Add careful wording beneath the 215+ metric so it is not represented as a VYSRO corporate achievement unless subsequently validated.

- [ ] **Step 5: Build operating-environment cards**

Cards:

```text
Manufacturing
Production
Construction
Concrete & Materials
Engineering
Standards & Quality
Field Operations
```

- [ ] **Step 6: Build featured-system cards**

Cards:

```text
SME Operational Cockpit
Ready-Mix / Concrete Operations
Precast Production
ISO Readiness
Field Data & MEL
Standards / Evidence Intelligence
```

Each card links to an anchor in `operational-systems.html` except the standards-intelligence concept, which may link to `standards-research.html`.

- [ ] **Step 7: Build the selected-evidence section**

Feature SizAfrica as a public case study and materials/pozzolan research as a research programme. Do not include unapproved client names.

- [ ] **Step 8: Build the Expert Network CTA**

The section must explain that VYSRO is building a multidisciplinary pool of technical experts and link to `experts.html`.

- [ ] **Step 9: Build a compact insights preview and contact CTA**

Use three placeholder-safe insight cards that are clearly labelled `Coming soon` unless real publications are approved before implementation.

- [ ] **Step 10: Update content register and commit**

Commit message:

```text
feat: build VYSRO mobile-first homepage
```

---

### Task 4: Build the Operational Systems page with public dashboard demonstrators

**Files:**
- Modify: `operational-systems.html`
- Modify: `assets/css/styles.css`
- Modify: `docs/website/CONTENT_REGISTER.md`

**Interfaces:**
- Consumes: shared card/dashboard styles.
- Produces: reusable visual demo components that can be linked from the homepage.

- [ ] **Step 1: Lead with the business problem, not software**

Opening copy must explain that VYSRO first maps how work is performed and then applies fit-for-purpose tools.

- [ ] **Step 2: Add `#sme-cockpit`**

Include a demo dashboard with synthetic values for:

```text
Open actions
Quality issues
Today's output
Evidence completion
On-time tasks
Management alerts
```

Display a visible `Demonstration data` label.

- [ ] **Step 3: Add `#ready-mix`**

Demo modules:

```text
Today's production
Orders
On-time dispatch
Plant utilisation
Open NCRs
Material status
QA/QC status
```

Use synthetic values only.

- [ ] **Step 4: Add `#precast`**

Demo modules:

```text
Planned units
Cast today
Curing
Awaiting inspection
Released
NCRs
```

- [ ] **Step 5: Add `#iso-readiness`**

Demo modules:

```text
Processes mapped
SOP approval
Evidence completeness
Open actions
Internal audit readiness
NCR status
```

- [ ] **Step 6: Add `#field-mel`**

Demo modules:

```text
Submissions
Validated
Pending review
Data-quality alerts
Coverage
Indicators on track
```

- [ ] **Step 7: Add the future evidence-intelligence concept**

Label the section `Under development` and describe controlled organisation/retrieval of standards and technical evidence without claiming production AI functionality.

- [ ] **Step 8: Add CTA**

`Discuss Your Operations` links to `contact.html#operations`.

- [ ] **Step 9: Manual mobile QA and commit**

Commit message:

```text
feat: add operational systems demonstrators
```

---

### Task 5: Build Standards & Research and the SizAfrica case study

**Files:**
- Modify: `standards-research.html`
- Modify: `assets/css/styles.css`
- Modify: `docs/website/CONTENT_REGISTER.md`

**Interfaces:**
- Consumes: evidence-number and step/timeline patterns.
- Produces: public standards/research authority page.

- [ ] **Step 1: Build the standards lifecycle**

Use:

```text
Requirement → Operational Obligation → Process → Evidence → Verification → Decision → Improvement
```

Explain that standards become valuable when translated into operating controls and evidence.

- [ ] **Step 2: Build standards capability cards**

Include:

```text
Standards development & review
Implementation support
ISO readiness
Conformity/certification readiness
Research & evidence generation
Stakeholder/technical committee support
Standards & regulatory intelligence
```

- [ ] **Step 3: Build the SizAfrica public case-study section**

Required structure:

```text
Problem
Intervention
Method
Scale
Broader lesson
```

Use `1,122` and `9` only in accordance with the claims register.

- [ ] **Step 4: Build materials-research section**

Present fly ash, volcanic pozzolan and low-carbon concrete as research/industrial-innovation areas. Clearly label ongoing or developing work and avoid confidential partner/client attribution.

- [ ] **Step 5: Add CTA and commit**

CTA: `Discuss a Standards or Research Assignment` → `contact.html#technical-enquiry`.

Commit message:

```text
feat: add standards and research page
```

---

### Task 6: Build the Expert Network page and Netlify-compatible intake

**Files:**
- Modify: `experts.html`
- Modify: `assets/css/styles.css`
- Create: `privacy.html`
- Modify: all shared navigation/footer references to include privacy in footer only
- Modify: `docs/website/CONTENT_REGISTER.md`

**Interfaces:**
- Consumes: Netlify static form handling.
- Produces: expert intake form with CV upload route and explicit consent.

- [ ] **Step 1: Build the expert-network value proposition**

Sections:

```text
Why join
Who should join
How matching works
What information we collect
What happens after registration
Privacy and consent
```

- [ ] **Step 2: Build the Netlify-compatible form**

Use:

```html
<form name="expert-pool" method="POST" data-netlify="true" enctype="multipart/form-data">
  <input type="hidden" name="form-name" value="expert-pool">
</form>
```

Fields:

```text
full-name
email
phone
country
professional-title
discipline
expertise
years-experience
regions
sectors
languages
linkedin
availability
cv
consent
```

`cv` must be `type="file"` and the form must visibly state that submissions are not stored in the public GitHub repository.

- [ ] **Step 3: Add explicit consent**

Required checkbox wording direction:

```text
I consent to VYSRO retaining and processing the information I submit for expert-profile administration and potential opportunity matching, subject to the VYSRO privacy notice.
```

The checkbox must be required.

- [ ] **Step 4: Add privacy page**

`privacy.html` must state in plain language:

- purpose of expert-data collection;
- categories of data collected;
- opportunity-matching purpose;
- that submission does not guarantee assignment;
- that CV/personal data are not published through GitHub;
- contact route for data/privacy requests;
- no sale of expert information.

Do not invent a retention period until VYSRO adopts one.

- [ ] **Step 5: Verify current Netlify form/file-upload limits before production release**

If current platform limits make CV upload unsuitable, the implementation must disable the file field and replace it with an approved secure upload path before launch rather than publishing an insecure workaround.

- [ ] **Step 6: Commit**

Commit message:

```text
feat: add expert network intake
```

---

### Task 7: Build Who We Are, Insights, Contact and Engineering Office pages

**Files:**
- Modify: `who-we-are.html`
- Modify: `insights.html`
- Modify: `contact.html`
- Modify: `engineering-office.html`
- Modify: `assets/css/styles.css`
- Modify: `docs/website/CONTENT_REGISTER.md`

**Interfaces:**
- Consumes: approved institutional copy and shared forms/components.
- Produces: complete navigable public MVP.

- [ ] **Step 1: Build Who We Are**

Sections:

```text
Operational • Intelligence • Systems
The operation comes before the software
Process → Evidence → Control → Intelligence → Value
Operational Efficiency & Technical Systems
Standards & Quality Infrastructure
Engineering & Technical Assurance
Research & Industrial Innovation
Expert Network
```

- [ ] **Step 2: Build Insights**

If no publication is approved for public release, use a high-quality `Insights are being prepared` state with categories:

```text
Operational Efficiency
Standards & Quality
Engineering & Materials
Research
Data & Evidence Systems
```

Do not fabricate article titles presented as published work.

- [ ] **Step 3: Build Contact**

Provide two routes:

```text
Improve Your Operations
Technical / Research / Standards Enquiry
```

A simple Netlify contact form may collect name, organisation, email, country, enquiry type and message. No sensitive operational documents are requested in v0.1.

- [ ] **Step 4: Build Engineering Office as under development**

Explicitly label it `Under development` and list intended scope without implying a fully launched service.

- [ ] **Step 5: Commit**

Commit message:

```text
feat: complete VYSRO MVP content pages
```

---

### Task 8: Add the real VYSRO logo and approved visual assets

**Files:**
- Create/modify: `assets/logo/*`
- Create/modify: `assets/images/*`
- Modify: HTML pages referencing visuals
- Modify: `assets/css/styles.css`

**Interfaces:**
- Consumes: real approved VYSRO logo from the user's existing source asset.
- Produces: final brand-consistent public presentation.

- [ ] **Step 1: Retrieve the actual VYSRO logo asset from the user's available files/source**

Do not redraw it with AI and do not substitute the temporary mockup logo.

- [ ] **Step 2: Store a web-appropriate copy in `assets/logo/`**

Preserve aspect ratio and original brand treatment. If conversion is necessary, keep the source untouched and create only a web derivative.

- [ ] **Step 3: Use approved real/synthetic visuals**

Priority order:

```text
Dashboards
Diagrams
Charts
Maps
Approved project/research photos
Clearly contextual AI-generated imagery
```

- [ ] **Step 4: Optimise media for mobile**

Avoid unnecessarily large source files and reserve image dimensions to minimise layout shift.

- [ ] **Step 5: Commit**

Commit message:

```text
feat: add VYSRO brand and visual assets
```

---

### Task 9: Configure Netlify deployment

**Files:**
- Create: `netlify.toml`
- Modify: `README.md`

**Interfaces:**
- Consumes: complete static site.
- Produces: repository configuration deployable by Netlify from GitHub.

- [ ] **Step 1: Create `netlify.toml`**

For a root static site:

```toml
[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    X-Frame-Options = "SAMEORIGIN"
```

Do not add a build command unless Netlify requires one.

- [ ] **Step 2: Update README**

README must explain:

```text
Repository purpose
Approved branch workflow
Production branch: main
Netlify publish directory: repository root
No build command for v0.1
No confidential data in repository
Expert form handled outside source-code storage
```

- [ ] **Step 3: Verify internal links**

Check every navigation, CTA, anchor and CSS/JS asset reference.

- [ ] **Step 4: Commit**

Commit message:

```text
chore: configure Netlify deployment
```

---

### Task 10: Accessibility, mobile performance and content-governance verification

**Files:**
- Modify: any public page failing checks
- Modify: `assets/css/styles.css`
- Modify: `assets/js/main.js`
- Modify: `docs/website/CONTENT_REGISTER.md`

**Interfaces:**
- Consumes: completed site.
- Produces: release candidate suitable for Netlify preview and review.

- [ ] **Step 1: Accessibility pass**

Verify:

```text
One h1 per page
Logical heading order
Keyboard-operable navigation
Visible focus states
Meaningful link/button labels
Form labels tied to controls
Required fields indicated
Alt text for informative images
Decorative images use empty alt text
No colour-only status indicators
```

- [ ] **Step 2: Mobile pass**

At 360px and 412px:

```text
No horizontal scroll
No clipped dashboard cards
Navigation is usable one-handed
Tap targets are comfortably sized
Text does not require zoom
Forms fit the viewport
```

- [ ] **Step 3: Content-governance pass**

Search the site for:

```text
unapproved client names
unapproved logos
unqualified impact claims
confidential data
claims not listed in CLAIMS_REGISTER.md
AI/KOSH/VERA claims written as completed functionality
```

Any finding blocks release until corrected.

- [ ] **Step 4: Performance pass**

Confirm:

```text
No autoplay video
Minimal JavaScript
No framework bundles
Images compressed appropriately
No unnecessary external font dependency if system fonts meet the design requirement
```

- [ ] **Step 5: Update content register**

Set completed public pages to `release candidate` only after passing the checks above.

- [ ] **Step 6: Commit**

Commit message:

```text
test: verify VYSRO MVP release candidate
```

---

### Task 11: Open a pull request for CEO review before production merge

**Files:**
- No new production files unless review fixes are required.

**Interfaces:**
- Consumes: release-candidate branch.
- Produces: reviewable pull request into `main`.

- [ ] **Step 1: Compare branch with `main`**

Review all changed files and confirm the PR contains only the approved website MVP work.

- [ ] **Step 2: Open the pull request**

Title:

```text
VYSRO Website MVP v0.1
```

Body must summarise:

```text
Business positioning
Mobile-first implementation
Operational systems demonstrators
Standards/research content
Expert-pool intake
Privacy/confidentiality controls
Netlify deployment configuration
Known under-development areas
```

- [ ] **Step 3: Do not merge until the user has reviewed the deployed/preview experience**

The PR is the production gate.

---

## Release Definition

MVP v0.1 is release-ready only when:

1. A visitor at 360–412px width immediately understands VYSRO as an operational-intelligence and technical-systems consultancy.
2. Technical SMEs in manufacturing, production and construction are visibly served.
3. `The operation comes before the software` and `Process → Evidence → Control → Intelligence → Value` are reflected in the actual homepage story.
4. The site contains no unapproved client disclosures.
5. Public dashboards use synthetic/demo data unless otherwise approved.
6. Expert CVs/personal data are not committed to GitHub.
7. The real VYSRO logo is used rather than the earlier mockup mark.
8. Expert registration and business-contact routes are usable.
9. Netlify can serve the repository as a static site.
10. The final production merge occurs only after user review of the release candidate.