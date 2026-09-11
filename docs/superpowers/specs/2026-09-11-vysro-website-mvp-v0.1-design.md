# VYSRO Website MVP v0.1 — Design Specification

**Status:** Approved design baseline pending final written-spec review  
**Date:** 2026-09-11  
**Repository:** `aliasmugicha-crypto/vysro-website`  
**Deployment target:** Netlify  
**Primary device:** Mobile/Android first, responsive desktop second

## 1. Purpose

Build the first deployable public VYSRO website as a serious business front door, not as an AI-product demo. The MVP must help a first-time visitor understand who VYSRO is, see credible evidence of technical capability, explore selected systems and research, and take one of two high-value actions: **Join Our Expert Pool** or **Contact VYSRO**.

The website must separate VYSRO's stable institutional identity from the specific products, systems and offers currently being developed.

## 2. Design philosophy

The visual and information architecture should combine the strongest qualities observed in three approved benchmark directions:

- **Genesis Analytics:** clear institutional identity, Africa-rooted positioning, disciplined presentation of complex multidisciplinary work.
- **iTad:** evidence-led storytelling, measurable outcomes, research/learning orientation, clear conversion from evidence to action.
- **CSIR South Africa:** depth of technical capability across engineering, research, systems and applied innovation without reducing the institution to one service line.

The site must not imitate or reproduce proprietary layouts or copy. These references are design benchmarks only.

## 3. Institutional identity

The homepage must answer **“Who is VYSRO?” before “What are we selling right now?”**

Working institutional positioning:

> VYSRO works at the intersection of standards, engineering, research and operational systems — turning technical knowledge and evidence into practical, controlled solutions for industry and society.

This wording is a working content baseline and remains editable during copy review.

### Institutional capability pillars

1. **Standards & Quality Infrastructure**
   - standards development and technical review
   - standards research and evidence generation
   - implementation support
   - ISO / management-system readiness
   - conformity and certification-readiness support
   - stakeholder consultation and standards-data systems

2. **Engineering & Technical Assurance**
   - civil and infrastructure engineering
   - concrete and materials engineering
   - QA/QC and technical controls
   - engineering documentation and project controls
   - future Engineering Office capability

3. **Research & Industrial Innovation**
   - fly ash / pozzolan / low-carbon materials research
   - concrete mix design and laboratory programmes
   - materials characterisation
   - research-to-industrialisation pathways

4. **Operational & Evidence Systems**
   - production-control systems
   - Ready-Mix and concrete operations systems
   - precast production systems
   - ISO-readiness systems
   - Kobo/ODK field-data systems
   - monitoring, evaluation and learning systems
   - dashboards, evidence controls and traceability

5. **Expert Network** is a cross-cutting business capability, not a fifth technical silo. It connects specialists to assignments, research, engineering and standards work.

## 4. Public MVP information architecture

### Primary navigation

- Home
- Who We Are
- Systems & Solutions
- Standards & Research
- Expert Network
- Insights
- Contact

A future **Engineering Office** route may exist as an “under development” page but must not distract from the v0.1 conversion priorities.

### Primary conversion action

**Join Our Expert Pool** must be the dominant recurring CTA in the header, homepage, relevant content sections and footer.

### Secondary conversion action

**Contact VYSRO** for projects, research, partnerships and consulting enquiries.

## 5. Homepage structure

The homepage should tell a coherent story in this order:

1. **Hero / institutional identity**
   - clear VYSRO statement
   - short explanatory copy
   - CTA: Explore Systems & Solutions
   - CTA: Join Our Expert Pool
   - use the real approved VYSRO logo exactly as supplied; do not redesign or substitute it

2. **Evidence / numbers strip**
   Use only claims that can be evidenced. Initial candidate metrics:
   - **1,122** registrations in the SizAfrica pilot
   - **9** pilot districts
   - **215+** standards supported/developed/reviewed through team experience — wording must make clear whether this is institutional or personnel experience
   - no “countries impacted,” CO₂ reduction, economic value or other extrapolated numbers until separately researched and evidenced

3. **Who we are / capability architecture**
   Present the four institutional pillars as a coherent operating model, not a miscellaneous services catalogue.

4. **Featured systems**
   Use product/system demonstrations rather than named operational clients:
   - Ready-Mix / Concrete Operations System
   - Precast Production System
   - ISO Readiness System
   - Field Data & MEL System
   - Standards / Evidence Intelligence concept

5. **Selected public evidence / case work**
   - SizAfrica / anthropometric standards work, where public naming and attribution are appropriate
   - standards and research evidence
   - materials/pozzolan research programme, framed without confidential client disclosure

6. **Expert Network conversion section**
   Explain why experts should join, how matching works, and what kinds of assignments may be available.

7. **Insights / publications**
   Technical notes, research, standards commentary and future publications.

8. **Contact / partnership CTA**

## 6. Systems & Solutions page

Public systems must be described as VYSRO capabilities and demonstrators, not as client disclosures.

### Initial solution set

#### Ready-Mix / Concrete Operations System
Public demonstration modules:
- order and production status
- batching / production control
- dispatch and delivery
- plant and mixer utilisation
- material consumption
- QA/QC status
- nonconformity tracking
- operational alerts
- management KPI dashboard

#### Precast Production System
Public demonstration modules:
- production planning
- mould / casting cycle tracking
- curing / release controls
- inspection and NCR tracking
- inventory and delivery status

#### ISO Readiness System
Public demonstration modules:
- process register
- SOP status
- evidence completeness
- action tracker
- internal audit readiness
- nonconformities
- readiness score/dashboard

#### Field Data & MEL System
Public demonstration modules:
- Kobo/ODK collection
- submission monitoring
- validation
- data-quality alerts
- geographic coverage
- progress/indicator dashboards
- reporting and learning

#### Standards / Evidence Intelligence
Future-facing concept showing how controlled standards, regulations and technical evidence may be organised, compared and retrieved. Do not present unbuilt AI functionality as an operational product.

### Demonstration data rule

Dashboard screenshots/prototypes must use clearly labelled synthetic/demo data unless the underlying information is already public and approved. No confidential client data may appear on the public site.

## 7. Standards & Research page

SizAfrica is a flagship evidence case study, not the definition of the standards practice.

The standards practice should explain the broader lifecycle:

**Evidence → Technical Analysis → Standard / Requirement → Implementation → Conformity / Assurance**

Content may include:
- standards development and review
- standards implementation support
- standards research and evidence generation
- stakeholder consultation
- ISO readiness
- conformity/certification-readiness support
- standards and regulatory intelligence
- anthropometric research / SizAfrica case study
- materials and low-carbon concrete research

## 8. Expert Network page

This is a primary business funnel.

### Visitor proposition

The page should answer:
- Why join VYSRO's expert network?
- Who should register?
- What kinds of assignments may experts be matched to?
- How does matching work?
- What information is collected and why?
- How is personal information handled?

### Initial expert intake fields

- full name
- email
- phone / country
- professional title
- discipline / expertise categories
- years of experience
- countries/regions of experience
- sector experience
- languages
- LinkedIn / professional profile
- availability
- CV upload
- consent to retain/process information for opportunity matching

CVs and personal records must **never be stored in the public GitHub repository**.

For v0.1, the expert intake will use **Netlify Forms with a CV file-upload field**, subject to verification of Netlify's current upload/security limits during implementation. Form submissions must remain outside the public repository, and submission notifications must be configured to a designated VYSRO inbox. The public form must include explicit consent/privacy wording before submission.

## 9. Privacy, confidentiality and claims governance

- Do not publicly name operational clients or companies unless the user explicitly approves that specific disclosure.
- Do not use private client logos, screenshots, operational data or project documents.
- Public named case studies must have a defensible public basis and approved attribution.
- Every quantitative claim must be traceable to a source/evidence register before launch.
- Distinguish VYSRO institutional achievements from founder/team prior professional experience.
- Clearly label synthetic dashboard data as demonstration data.
- Do not present future KOSH/VERA/AI functions as completed capabilities.
- Personal expert information must be collected outside the public source-code repository and handled under an explicit consent/privacy model.

## 10. Visual direction

- preserve the actual VYSRO logo and brand assets exactly
- mobile-first Android experience
- clean, technically credible, African/international consulting aesthetic
- strong typography and white space
- number-led evidence sections
- dashboards, maps, diagrams, charts and technical interfaces as core visual assets
- selective real project/research photography where available and authorised
- AI-generated contextual imagery may be used only where appropriate and must not imply a fabricated real project, client or field event
- avoid dependence on autoplay video or large media assets for the core experience
- fast loading on mobile connections

## 11. Initial file/page scope

Target production structure for v0.1:

```text
/
├── index.html
├── who-we-are.html
├── systems-solutions.html
├── standards-research.html
├── experts.html
├── insights.html
├── contact.html
├── engineering-office.html        # under development / future capability
├── assets/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   ├── images/
│   └── logo/
├── docs/
│   ├── business/
│   ├── website/
│   ├── governance/
│   └── superpowers/
├── prototypes/
└── netlify.toml
```

Exact implementation structure may be refined in the implementation plan, but v0.1 must remain a lightweight static deployment suitable for GitHub + Netlify.

## 12. Technology baseline

For MVP v0.1:

- static HTML5
- CSS3
- minimal vanilla JavaScript
- no frontend framework unless a concrete requirement emerges
- Netlify deployment from GitHub
- Netlify Forms for expert intake
- no production KOSH/VERA backend in this release
- no authentication/account system in this release
- no confidential database in GitHub

This keeps the first release fast, understandable, inexpensive and easy to maintain from Android/GitHub while leaving room for future application modules.

## 13. Definition of MVP success

A first-time visitor on an Android phone should be able to:

1. understand what VYSRO is within the first screen/first short scroll;
2. see credible quantitative and project evidence without inflated claims;
3. understand that standards, engineering, research and systems belong to one coherent institution;
4. view concrete demonstrations of VYSRO systems without client confidentiality breaches;
5. register / join the expert pool through a clear path including CV submission and consent;
6. contact VYSRO for consulting/research/partnership work;
7. navigate and read the site comfortably on a mobile connection;
8. distinguish existing work from capabilities under development.

## 14. Explicitly out of scope for v0.1

- production KOSH/VERA implementation
- vector database / RAG / LLM application
- client portals
- authenticated expert accounts
- automated opportunity matching
- tender/bid automation
- payment systems
- full Engineering Office application
- private operational dashboards
- autonomous decision systems

These may become later modules once the public business front door and expert-intake funnel are operating.