from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE = "https://www.scouting.org"

def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()

def parse_badge_index(html):
    """Return dict: {name → URL} from the A–Z page."""
    soup = BeautifulSoup(html, "html.parser")
    badges = {}

    for a in soup.select("a"):
        href = a.get("href")
        if not href:
            continue
        if href.startswith("/skills/merit-badges/") and not href.endswith("all/"):
            name = a.get_text(strip=True)
            badges[name] = urljoin(BASE, href)

    return badges

def parse_requirements(html):
    """Extract ordered-list requirements."""
    soup = BeautifulSoup(html, "html.parser")
    reqs = []

    for ol in soup.find_all("ol"):
        for li in ol.find_all("li", recursive=False):
            txt = clean_text(li.get_text(" ", strip=True))
            if txt:
                reqs.append(txt)

    # fallback
    if not reqs:
        for p in soup.find_all("p"):
            txt = clean_text(p.get_text(" ", strip=True))
            if txt and len(txt) < 2000:
                reqs.append(txt)

    return reqs

