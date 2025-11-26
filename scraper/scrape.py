from .fetch import fetch
from .parse import parse_badge_index, parse_requirements

BADGE_INDEX_URL = "https://www.scouting.org/skills/merit-badges/all/"

def scrape_all(use_cache=True, delay=1.0, limit=None, verbose=False):
    """Scrape all badges and return structured dict."""
    if verbose:
        print("Loading badge index...")

    index_html = fetch(BADGE_INDEX_URL, use_cache=use_cache, delay=delay)
    badges = parse_badge_index(index_html)

    if verbose:
        print(f"Found {len(badges)} badges.")

    if limit:
        badges = dict(list(badges.items())[:limit])

    out = {}
    for badge, url in badges.items():
        if verbose:
            print(f"Scraping {badge}...")

        html = fetch(url, use_cache=use_cache, delay=delay)
        reqs = parse_requirements(html)

        out[badge] = {
            "url": url,
            "requirements": reqs,
        }

    return out

