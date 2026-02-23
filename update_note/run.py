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
    note_id = params["note_id"]

    api = get_client()

    kwargs: dict = {}
    if "title" in params:
        kwargs["title"] = params["title"]
    if "body" in params:
        kwargs["body"] = params["body"]
    if "is_todo" in params:
        kwargs["is_todo"] = 1 if params["is_todo"] else 0

    api.modify_note(id_=note_id, **kwargs)
    json.dump({"success": True}, sys.stdout, cls=DateTimeEncoder)


main()
