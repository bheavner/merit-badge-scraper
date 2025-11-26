# Merit Badge Scraper

A Python-based toolkit for scraping and exporting the official **Scouting America merit badge requirements** from:

**https://www.scouting.org/skills/merit-badges/all/**

This project can:

- ✔️ Scrape all merit badge names + requirements  
- ✔️ Cache pages locally for fast updates  
- ✔️ Export to **JSON**, **CSV**, **TSV**, and **Markdown**  
- ✔️ Generate a “Requirements Book” in Markdown format  
- ✔️ Be run periodically to keep your local copy current  
- ✔️ Includes unit tests and modular code structure  

---

## 📂 Project Structure

merit-badge-scraper/
│
├── scraper/
│ ├── init.py
│ ├── fetch.py
│ ├── parse.py
│ ├── export.py
│ └── scrape.py
│
├── tests/
│ ├── test_parse.py
│ └── test_export.py
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore


---

## 🚀 Installation

### 1. Clone repository

git clone https://github.com/YOURNAME/merit-badge-scraper.git

cd merit-badge-scraper


### 2. Install dependencies

pip install -r requirements.txt


---

## 🕹️ Usage

All commands are run through `cli.py`.

### Scrape all merit badges (cached by default)

python cli.py scrape -v


This creates:

badges.json


### Disable cache

python cli.py scrape --no-cache


### Export CSV

python cli.py csv badges.json badges.csv


### Export TSV

python cli.py tsv badges.json badges.tsv


### Export Markdown "book"

python cli.py md badges.json requirements.md


---

## 📦 Caching

All fetched pages are cached in:

.cache/


This makes repeated scrapes very fast and reduces load on Scouting.org.

Delete the folder to refresh everything.

---

## 🧪 Running Tests

pytest


Requires:

pytest


(You can add to requirements.txt if desired.)

---

## ⚙️ Design Notes

- Scraper uses polite delays (`--delay`, default 1.0 seconds)
- All parsing done with BeautifulSoup
- TSV & CSV exports include:  
  - Badge name  
  - Requirement number  
  - Requirement text  
  - Source URL  
- Markdown export produces a clean, readable requirements book

---

## 📜 License

MIT License (you may modify as needed).


