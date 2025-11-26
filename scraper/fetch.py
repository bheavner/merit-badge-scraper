import os
import hashlib
import time
import json
import requests

CACHE_DIR = ".cache"
os.makedirs(CACHE_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MeritBadgeScraper/1.0)"
}

def _cache_path(url):
    h = hashlib.md5(url.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{h}.json")

def fetch(url, use_cache=True, delay=1.0):
    """Fetch URL with optional caching."""
    path = _cache_path(url)

    if use_cache and os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            obj = json.load(f)
        return obj["html"]

    time.sleep(delay)
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    html = resp.text

    with open(path, "w", encoding="utf-8") as f:
        json.dump({"url": url, "html": html}, f)

    return html

