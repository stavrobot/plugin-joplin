#!/usr/bin/env -S uv run
# /// script
# dependencies = ["joppy"]
# ///

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from helpers import get_client, DateTimeEncoder


def main() -> None:
    params = json.load(sys.stdin)

    api = get_client()

    kwargs: dict = {"title": params["title"]}
    if "body" in params:
        kwargs["body"] = params["body"]
    if "notebook_id" in params:
        kwargs["parent_id"] = params["notebook_id"]
    if "is_todo" in params:
        kwargs["is_todo"] = 1 if params["is_todo"] else 0

    note_id = api.add_note(**kwargs)
    json.dump({"note_id": note_id}, sys.stdout, cls=DateTimeEncoder)


main()
