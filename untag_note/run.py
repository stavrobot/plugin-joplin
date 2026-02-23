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
    tag_id = params["tag_id"]
    note_id = params["note_id"]

    config = load_config()
    base_url = config.get("joplin_url", "http://localhost:41184")
    token = config["joplin_token"]

    response = requests.delete(
        f"{base_url}/tags/{tag_id}/notes/{note_id}",
        params={"token": token},
    )
    response.raise_for_status()
    json.dump({"success": True}, sys.stdout, cls=DateTimeEncoder)


main()
