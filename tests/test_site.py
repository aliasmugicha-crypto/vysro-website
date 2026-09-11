from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    'index.html','who-we-are.html','operational-systems.html','standards-research.html',
    'experts.html','insights.html','contact.html','engineering-office.html','privacy.html'
]


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


def test_all_pages_exist_and_have_accessible_shell():
    for page in PAGES:
        p = ROOT / page
        assert p.exists(), f'missing {page}'
        html = p.read_text(encoding='utf-8')
        assert html.lower().count('<main id="main"') == 1, page
        assert 'name="viewport"' in html, page
        assert 'assets/css/styles.css' in html, page
        assert 'assets/js/main.js' in html, page
        assert 'Skip to content' in html, page
        assert 'data-menu-button' in html, page
        assert 'data-menu' in html, page


def test_shared_navigation_contains_approved_routes():
    required = [
        'Home','Who We Are','Operational Systems','Standards &amp; Research',
        'Expert Network','Insights','Contact'
    ]
    for page in PAGES:
        html = read(page)
        for label in required:
            assert label in html, f'{label} missing in {page}'


def test_homepage_contains_governing_identity_and_ctas():
    html = read('index.html')
    assert 'Operational • Intelligence • Systems' in html
    assert 'Turning Operational Knowledge into Intelligent Systems.' in html
    assert 'The operation comes before the software.' in html
    assert 'Process' in html and 'Evidence' in html and 'Control' in html and 'Intelligence' in html and 'Value' in html
    assert 'Improve Your Operations' in html
    assert 'Join Our Expert Pool' in html
    assert '1,122' in html and '9' in html and '215+' in html
    assert 'SME Operational Cockpit' in html
    assert 'Ready-Mix / Concrete Operations' in html
    assert 'SizAfrica' in html


def test_governance_documents_exist_and_block_unverified_claims():
    claims = read('docs/business/CLAIMS_REGISTER.md')
    rules = read('docs/governance/PUBLIC_CONTENT_RULES.md')
    identity = read('docs/business/WHO_WE_ARE.md')
    register = read('docs/website/CONTENT_REGISTER.md')
    assert 'Countries potentially impacted by anthropometric work | blocked' in claims
    assert 'CVs and expert personal data must never enter this repository' in rules
    assert 'Operational • Intelligence • Systems' in identity
    assert '| Home |' in register


def test_mobile_css_has_no_fixed_page_width_and_has_breakpoint():
    css = read('assets/css/styles.css')
    assert 'max-width:' in css
    assert '@media' in css
    assert 'overflow-x: hidden' not in css, 'do not hide layout bugs with overflow-x:hidden'
    assert '.menu-button' in css
    assert '.metric' in css
    assert '.card' in css


def test_js_is_progressive_mobile_menu_only():
    js = read('assets/js/main.js')
    assert "[data-menu-button]" in js
    assert "aria-expanded" in js
    assert 'classList.add("hidden")' not in js


def test_internal_html_links_resolve():
    import re
    for page in PAGES:
        html = read(page)
        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith(('http://','https://','mailto:','#')):
                continue
            target = href.split('#',1)[0]
            if target:
                assert (ROOT / target).exists(), f'{page} -> missing {target}'

def test_operational_systems_contains_all_demo_dashboards_and_labels():
    html = read('operational-systems.html')
    required_sections = ['sme-cockpit','ready-mix','precast','iso-readiness','field-mel','evidence-intelligence']
    for section in required_sections:
        assert f'id="{section}"' in html
    for label in [
        'Open actions','Quality issues',"Today’s output",'Evidence completion','On-time tasks','Management alerts',
        "Today’s production",'Orders','On-time dispatch','Plant utilisation','Open NCRs','Material status','QA/QC status',
        'Planned units','Cast today','Curing','Awaiting inspection','Released',
        'Processes mapped','SOP approval','Internal audit readiness','NCR status',
        'Submissions','Validated','Pending review','Data-quality alerts','Coverage','Indicators on track'
    ]:
        assert label in html, f'missing dashboard label: {label}'
    assert html.count('Demonstration data') >= 5
    assert 'Under development' in html
    assert 'Discuss Your Operations' in html

def test_standards_research_has_lifecycle_capabilities_case_and_cta():
    html = read('standards-research.html')
    for term in ['Requirement','Operational obligation','Process','Evidence','Verification','Decision','Improvement']:
        assert term in html
    for term in ['Standards development &amp; review','Implementation support','ISO readiness','Conformity / certification readiness','Research &amp; evidence generation','Stakeholder / technical committee support','Standards &amp; regulatory intelligence']:
        assert term in html, term
    for heading in ['Problem','Intervention','Method','Scale','Broader lesson']:
        assert f'<h3>{heading}</h3>' in html
    assert '1,122' in html and '9' in html
    assert 'fly ash' in html.lower() and 'volcanic pozzolan' in html.lower() and 'low-carbon concrete' in html.lower()
    assert 'Discuss a Standards or Research Assignment' in html
    assert 'contact.html#technical-enquiry' in html


def test_expert_intake_is_netlify_compatible_and_pii_safe():
    html = read('experts.html')
    assert 'name="expert-pool"' in html
    assert 'method="POST"' in html
    assert 'data-netlify="true"' in html
    assert 'netlify-honeypot="bot-field"' in html
    for field in ['full-name','email','phone','country','professional-title','discipline','expertise','years-experience','regions','sectors','languages','linkedin','availability','consent']:
        assert f'name="{field}"' in html, field
    assert 'type="file"' not in html, 'PII CV upload must remain disabled until secure file handling is configured'
    assert 'CV' in html and 'secure' in html.lower()
    assert 'privacy.html' in html
    assert 'name="consent"' in html and 'required' in html


def test_privacy_page_covers_expert_data_basics_without_fake_retention_period():
    html = read('privacy.html')
    for term in ['expert-profile administration','opportunity matching','does not guarantee an assignment','not published through GitHub','data or privacy requests','do not sell']:
        assert term.lower() in html.lower(), term
    assert '12 months' not in html and '24 months' not in html

def test_who_we_are_contains_full_institutional_model():
    html = read('who-we-are.html')
    for term in ['Operational • Intelligence • Systems','The operation comes before the software.','Process','Evidence','Control','Intelligence','Value','Operational Efficiency &amp; Technical Systems','Standards &amp; Quality Infrastructure','Engineering &amp; Technical Assurance','Research &amp; Industrial Innovation','Expert Network']:
        assert term in html, term


def test_insights_uses_categories_not_fake_published_articles():
    html = read('insights.html')
    for term in ['Operational Efficiency','Standards &amp; Quality','Engineering &amp; Materials','Research','Data &amp; Evidence Systems']:
        assert term in html, term
    assert 'Insights are being prepared' in html


def test_contact_has_two_routes_and_netlify_form_without_file_uploads():
    html = read('contact.html')
    assert 'id="operations"' in html
    assert 'id="technical-enquiry"' in html
    assert 'name="business-enquiry"' in html
    assert 'data-netlify="true"' in html
    for field in ['name','organisation','email','country','enquiry-type','message']:
        assert f'name="{field}"' in html
    assert 'type="file"' not in html
    assert 'Improve Your Operations' in html
    assert 'Technical / Research / Standards Enquiry' in html


def test_engineering_office_is_explicitly_under_development():
    html = read('engineering-office.html')
    assert 'Under development' in html
    for term in ['Technical assurance','Project controls','QA/QC','Concrete &amp; materials','Standards &amp; compliance']:
        assert term in html


def test_locked_brand_asset_and_controlled_palette_are_used():
    logo = ROOT / 'assets/logo/vysro-logo.webp'
    assert logo.exists() and logo.stat().st_size > 1000
    css = read('assets/css/styles.css')
    for value in ['#0B2F5B','#062447','#5BC500','#FF6A00','#1A1A1A','#5F6B7A']:
        assert value in css, value
    assert '"Noto Sans"' in css
    for page in PAGES:
        html = read(page)
        assert 'assets/logo/vysro-logo.webp' in html, page
        assert 'logo-placeholder' not in html, page


def test_netlify_static_deployment_and_security_docs_exist():
    config = read('netlify.toml')
    assert 'publish = "."' in config
    assert 'X-Content-Type-Options = "nosniff"' in config
    assert 'Referrer-Policy = "strict-origin-when-cross-origin"' in config
    assert 'X-Frame-Options = "SAMEORIGIN"' in config
    readme = read('README.md')
    for term in ['Production branch: `main`','Publish directory: repository root','No build command','confidential data','expert']:
        assert term.lower() in readme.lower(), term
    security = read('docs/governance/FORM_SECURITY_DECISION.md')
    assert '8 MB' in security
    assert 'PII' in security
    assert 'CV upload remains disabled' in security


def test_release_accessibility_and_content_governance_basics():
    forbidden_client_names = ['TEMACO']
    for page in PAGES:
        html = read(page)
        assert len(re.findall(r'<h1(?:\s[^>]*)?>', html, flags=re.I)) == 1, page
        for name in forbidden_client_names:
            assert name.lower() not in html.lower(), f'unapproved client name {name} in {page}'
        assert '<video' not in html.lower(), page
        assert 'react' not in html.lower() and 'next.js' not in html.lower(), page
    # Forms must not request operational documents or CV files in v0.1.
    assert 'type="file"' not in read('experts.html')
    assert 'type="file"' not in read('contact.html')
