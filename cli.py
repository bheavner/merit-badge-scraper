#!/usr/bin/env python3
import argparse
import json
from scraper.scrape import scrape_all
from scraper.export import export_csv, export_tsv, export_markdown

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="Merit Badge Scraper Toolkit")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # scrape
    p = sub.add_parser("scrape")
    p.add_argument("-o", "--out", default="badges.json")
    p.add_argument("--delay", type=float, default=1.0)
    p.add_argument("--limit", type=int)
    p.add_argument("--no-cache", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true")

    # csv
    p = sub.add_parser("csv")
    p.add_argument("json")
    p.add_argument("out")

    # tsv
    p = sub.add_parser("tsv")
    p.add_argument("json")
    p.add_argument("out")

    # markdown
    p = sub.add_parser("md")
    p.add_argument("json")
    p.add_argument("out")

    args = parser.parse_args()

    if args.cmd == "scrape":
        data = scrape_all(
            use_cache=not args.no_cache,
            delay=args.delay,
            limit=args.limit,
            verbose=args.verbose,
        )
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Saved {len(data)} badges → {args.out}")
        return

    if args.cmd == "csv":
        export_csv(load_json(args.json), args.out)
        print(f"Exported CSV → {args.out}")
        return

    if args.cmd == "tsv":
        export_tsv(load_json(args.json), args.out)
        print(f"Exported TSV → {args.out}")
        return

    if args.cmd == "md":
        export_markdown(load_json(args.json), args.out)
        print(f"Exported Markdown → {args.out}")
        return

if __name__ == "__main__":
    main()

