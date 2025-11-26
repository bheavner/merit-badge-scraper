import csv

def export_csv(badges, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Badge", "Requirement #", "Requirement Text", "URL"])
        for badge, info in badges.items():
            for i, req in enumerate(info["requirements"], start=1):
                w.writerow([badge, i, req, info["url"]])

def export_tsv(badges, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["Badge", "Requirement #", "Requirement Text", "URL"])
        for badge, info in badges.items():
            for i, req in enumerate(info["requirements"], start=1):
                w.writerow([badge, i, req, info["url"]])

def export_markdown(badges, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Merit Badge Requirements\n\n")
        for badge, info in sorted(badges.items()):
            f.write(f"## {badge}\n")
            f.write(f"*Source:* {info['url']}\n\n")
            for i, req in enumerate(info["requirements"], start=1):
                f.write(f"{i}. {req}\n")
            f.write("\n")

