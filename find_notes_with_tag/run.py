#!/usr/bin/env -S uv run
# /// script
# dependencies = ["joppy", "requests"]
# ///

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from helpers import load_config

import requests


def main() -> None:
    params = json.load(sys.stdin)
    tag_id = params["tag_id"]

    config = load_config()
    base_url = config.get("joplin_url", "http://localhost:41184")
    token = config["joplin_token"]

    notes = []
    page = 1
    while True:
        response = requests.get(
            f"{base_url}/tags/{tag_id}/notes",
            params={
                "token": token,
                "fields": "id,title,parent_id",
                "page": page,
            },
        )
        response.raise_for_status()
        data = response.json()

        for item in data.get("items", []):
            notes.append(
                {"id": item["id"], "title": item["title"], "parent_id": item["parent_id"]}
            )

        if not data.get("has_more", False):
            break
        page += 1

    json.dump({"notes": notes}, sys.stdout)


main()
