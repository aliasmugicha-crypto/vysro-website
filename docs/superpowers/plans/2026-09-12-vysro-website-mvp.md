# VYSRO Website MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a deployable multi-page VYSRO corporate website in the GitHub repository for direct Netlify hosting.

**Architecture:** Dependency-free static HTML/CSS/JavaScript served directly from the repository root. Shared brand, navigation and interaction assets live under `assets/`; each page is independently addressable and uses the same controlled copy and visual system.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Node.js built-in test runner, Netlify static hosting.

**Spec:** `docs/superpowers/specs/2026-09-12-vysro-website-mvp-design.md`

## Global Constraints
- Descriptor: `Operational • Intelligence • Systems`.
- Tagline: `Turning Operational Knowledge into Intelligent Systems.`
- Brand colors: `#0D2240`, `#1FA84A`, `#FF6A00`.
- No TEMACO or other client/company names.
- Ready-Mix must be included as a visible system showcase.
- Describe prototypes and implementation architectures without unsupported deployment claims.
- No framework, package manager or build command.
- Netlify publishes repository root `.` from branch `main`.

---

### Task 1: Acceptance tests
**Files:** Create `tests/site.test.mjs`.
- [ ] Write tests for required files, controlled brand copy, prohibited names, navigation targets and Netlify publish configuration.
- [ ] Run tests before site files exist and confirm failure for missing production files.

### Task 2: Global brand and interaction layer
**Files:** Create `assets/vysro-logo.svg`, `assets/styles.css`, `assets/app.js`.
- [ ] Preserve the approved primary logo in a web-safe asset.
- [ ] Implement shared responsive layout, typography, navigation, cards, dashboard visuals, buttons and footer.
- [ ] Implement mobile navigation and current-year footer behavior.

### Task 3: Homepage
**Files:** Create `index.html`.
- [ ] Implement hero, positioning, VYSRO doctrine, services preview, systems showcase, SME/technical-business section, standards logic and CTA.
- [ ] Include Ready-Mix dashboard-style KPI visualization.

### Task 4: Systems page
**Files:** Create `systems.html`.
- [ ] Present seven controlled system architectures with clear prototype/implementation-language boundaries.
- [ ] Expand Ready-Mix architecture with evidence, QA/QC, production, dispatch and management-review modules.

### Task 5: Corporate service pages
**Files:** Create `services.html`, `industries.html`, `standards.html`, `about.html`.
- [ ] Implement approved service lines.
- [ ] Position SME, manufacturing, production, construction, ready-mix and institutional use cases.
- [ ] Explain standards-to-systems and evidence governance.
- [ ] Present founder/company credibility without unverified claims.

### Task 6: Deployment configuration and verification
**Files:** Create `netlify.toml`; update `README.md`.
- [ ] Configure root publishing and security headers.
- [ ] Run the complete Node test suite until green.
- [ ] Inspect responsive static output locally and verify all links/files.
- [ ] Commit/push the verified set to `main` so Netlify can deploy it.
