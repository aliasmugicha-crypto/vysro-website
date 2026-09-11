from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    'index.html','who-we-are.html','operational-systems.html','standards-research.html',
    'experts.html','insights.html','contact.html','engineering-office.html'
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
    required = ['Home','Who We Are','Operational Systems','Standards &amp; Research','Expert Network','Insights','Contact']
    for page in PAGES:
        html = read(page)
        for label in required:
            assert label in html, f'{label} missing in {page}'


def test_homepage_contains_governing_identity_and_ctas():
    html = read('index.html')
    assert 'Operational • Intelligence • Systems' in html
    assert 'Turning Operational Knowledge into Intelligent Systems.' in html
    assert 'The operation comes before the software.' in html
    assert all(term in html for term in ['Process','Evidence','Control','Intelligence','Value'])
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
    assert 'overflow-x: hidden' not in css
    assert '.menu-button' in css
    assert '.metric' in css
    assert '.card' in css
    assert '.dashboard-demo' in css


def test_js_is_progressive_mobile_menu_only():
    js = read('assets/js/main.js')
    assert '[data-menu-button]' in js
    assert 'aria-expanded' in js
    assert 'classList.add("hidden")' not in js


def test_internal_html_links_resolve():
    for page in PAGES:
        html = read(page)
        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith(('http://','https://','mailto:','#')):
                continue
            target = href.split('#',1)[0]
            if target:
                assert (ROOT / target).exists(), f'{page} -> missing {target}'
