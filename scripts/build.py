#!/usr/bin/env python3
import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "resume.json"
TEMPLATE_DIR = ROOT / "templates"
ASSETS_DIR = ROOT / "assets"
DIST_DIR = ROOT / "dist"


def build() -> None:
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    template = env.get_template("resume.html.j2")
    html = template.render(**data)

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    (DIST_DIR / "index.html").write_text(html, encoding="utf-8")
    shutil.copytree(ASSETS_DIR, DIST_DIR / "assets")

    print(f"Built {DIST_DIR / 'index.html'}")


if __name__ == "__main__":
    build()
