#!/usr/bin/env -S uv run
# /// script
# dependencies = ["joppy", "requests"]
# ///

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from helpers import load_config, DateTimeEncoder

import requests


def main() -> None:
    params = json.load(sys.stdin)
    note_id = params["note_id"]

    config = load_config()
    base_url = config.get("joplin_url", "http://localhost:41184")
    token = config["joplin_token"]

    tags = []
    page = 1
    while True:
        response = requests.get(
            f"{base_url}/notes/{note_id}/tags",
            params={
                "token": token,
                "fields": "id,title",
                "page": page,
            },
        )
        response.raise_for_status()
        data = response.json()

        for item in data.get("items", []):
            tags.append({"id": item["id"], "title": item["title"]})

        if not data.get("has_more", False):
            break
        page += 1

    json.dump({"tags": tags}, sys.stdout, cls=DateTimeEncoder)


main()
