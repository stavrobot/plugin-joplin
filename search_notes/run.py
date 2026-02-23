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
    query = params["query"]

    config = load_config()
    base_url = config.get("joplin_url", "http://localhost:41184")
    token = config["joplin_token"]

    response = requests.get(
        f"{base_url}/search",
        params={
            "query": query,
            "token": token,
            "fields": "id,title,parent_id",
            "type": "note",
        },
    )
    response.raise_for_status()
    data = response.json()

    notes = [
        {"id": item["id"], "title": item["title"], "parent_id": item["parent_id"]}
        for item in data.get("items", [])
    ]
    json.dump({"notes": notes}, sys.stdout, cls=DateTimeEncoder)


main()
