from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from typing import Dict, List

BASE = "https://www.scouting.org"

def clean_text(text: str) -> str:
    """Normalize whitespace in text."""
    return re.sub(r"\s+", " ", text).strip()

def parse_badge_index(html: str) -> Dict[str, str]:
    """
    Return dict {badge name -> URL} by extracting all <h2 class="mb-card-title"> headers.
    Each header contains an <a> with the badge page URL.
    """
    soup = BeautifulSoup(html, "html.parser")
    badges: Dict[str, str] = {}

    for h2 in soup.find_all("h2", class_="mb-card-title"):
        a = h2.find("a")
        if not a:
            continue
        name = clean_text(a.get_text())
        href = a.get("href")
        if not href:
            continue
        url = urljoin(BASE, href)
        badges[name] = url

    return badges

from bs4 import BeautifulSoup
from typing import List
import re

def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

from bs4 import BeautifulSoup
from typing import List
import re

def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

from bs4 import BeautifulSoup
from typing import List, Dict
import re

def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def parse_requirements(html: str) -> List[Dict]:
    """
    Parse merit badge requirements handling both inline lists and adjacent lists.
    Returns a list of dicts: {"number": str, "heading": str, "subitems": List[str]}
    """
    soup = BeautifulSoup(html, "html.parser")
    requirements: List[Dict] = []

    main_container = soup.find("div", class_="mb-requirement-container")
    if not main_container:
        return requirements

    items = main_container.find_all("div", class_="mb-requirement-item", recursive=False)
    for item in items:
        parents = item.find_all("div", class_="mb-requirement-parent", recursive=False)
        for parent in parents:
            listnum_span = parent.find("span", class_="mb-requirement-listnumber")
            if not listnum_span or not listnum_span.get_text(strip=True):
                continue
            number = clean_text(listnum_span.get_text())

            # Heading text: remove list number from parent text
            heading_text = clean_text(parent.get_text())
            if heading_text.startswith(number):
                heading_text = heading_text[len(number):].strip()

            # Sub-items
            subitems: List[str] = []

            # 1) Check for ul/ol inside parent
            inner_list = parent.find(["ul", "ol"])
            if inner_list:
                for li in inner_list.find_all("li", recursive=False):
                    li_text = clean_text(li.get_text(" ", strip=True))
                    if li_text:
                        subitems.append(li_text)

            # 2) If no inner list, check **next tag sibling** (skips whitespace)
            if not subitems:
                next_sibling = parent.find_next_sibling()
                while next_sibling and next_sibling.name is None:
                    next_sibling = next_sibling.find_next_sibling()
                if next_sibling and next_sibling.name in ["ul", "ol"]:
                    for li in next_sibling.find_all("li", recursive=False):
                        li_text = clean_text(li.get_text(" ", strip=True))
                        if li_text:
                            subitems.append(li_text)

            requirements.append({
                "number": number,
                "heading": heading_text,
                "subitems": subitems
            })

    return requirements

