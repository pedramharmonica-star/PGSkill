#!/usr/bin/env python3
"""For each RFP requirement, list the best evidence candidates from the knowledge base.

Usage: python3 candidates.py requirements.csv out.json [--top 5]
requirements.csv needs columns: id, requirement (other columns are kept).
Output: JSON list of {id, requirement, ..., candidates:[{score, source, article, text}]}.
Candidates are hints only - the status decision is made by reading the full sources.
"""
import csv, json, os, sys

KB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                  "payamgostar-knowledge", "scripts")
sys.path.insert(0, os.path.abspath(KB))
import find  # noqa: E402

def main():
    src, out = sys.argv[1], sys.argv[2]
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 5
    rows = list(csv.DictReader(open(src, encoding="utf-8-sig")))
    res = []
    for r in rows:
        hits = find.search(r.get("requirement", ""), top)
        r["candidates"] = [{"score": round(s, 2), "source": f, "article": a, "text": t[:500]} for s, f, a, t in hits]
        res.append(r)
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(res)} requirements -> {out}")

if __name__ == "__main__":
    main()
