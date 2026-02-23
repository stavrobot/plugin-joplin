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
    notebook_id = params["notebook_id"]

    api = get_client()
    notes_raw = api.get_all_notes(notebook_id=notebook_id, fields="id,title,parent_id")

    notes = [
        {"id": note.id, "title": note.title, "parent_id": note.parent_id}
        for note in notes_raw
    ]
    json.dump({"notes": notes}, sys.stdout, cls=DateTimeEncoder)


main()
