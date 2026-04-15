# -*- coding: utf-8 -*-
from pathlib import Path
base = Path(__file__).parent
parts = []
for i in range(1, 21):
    p = base / f"html_chunk_{i:02d}.txt"
    if p.exists():
        parts.append(p.read_text(encoding="utf-8"))
(base / "index.html").write_text("".join(parts), encoding="utf-8")
print("Wrote index.html,", len(parts), "chunks")
