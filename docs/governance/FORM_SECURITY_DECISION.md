# Expert Form Security Decision — MVP v0.1

**Decision date:** 2026-09-11  
**Scope:** Public expert-profile intake on the VYSRO website.

## Decision

The public MVP may collect expert profile information through a Netlify-compatible form, but **CV upload remains disabled** in the ordinary public form until VYSRO configures and approves a secure file-transfer route appropriate for personally identifiable information (PII).

## Basis

Current Netlify Forms documentation indicates that standard form uploads:

- support one file per file field;
- have an **8 MB** maximum request size;
- have a file-upload timeout;
- can be reviewed/downloaded by authorised site administrators through Netlify form-submission tooling;
- require additional care where uploads contain PII, and Netlify specifically points users toward additional security controls for sensitive file handling.

A CV commonly contains PII such as contact details, employment history, education, identifiers and other personal information. For this reason, basic file upload is not enabled merely because the platform technically supports it.

## MVP implementation

The expert form may collect:

- name and contact details;
- country and professional title;
- discipline and expertise;
- experience, regions, sectors and languages;
- LinkedIn/professional profile;
- availability;
- explicit consent for expert-profile administration and potential opportunity matching.

The page must state that:

1. expert registration does not guarantee an assignment;
2. submitted profile information is not published through the GitHub repository;
3. CVs will be requested through an approved secure channel when needed;
4. personal information is not sold;
5. data/privacy requests can be made through the VYSRO contact route.

## Release condition for CV uploads

CV upload may be activated only after VYSRO selects, configures and verifies a secure PII-capable file-handling route, including access control, administrator permissions, retention/deletion controls and a privacy notice consistent with actual operation.
