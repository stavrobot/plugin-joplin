#!/usr/bin/env -S uv run
# /// script
# dependencies = ["joppy"]
# ///

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from helpers import get_client


def main() -> None:
    params = json.load(sys.stdin)
    note_id = params["note_id"]

    api = get_client()
    note = api.get_note(
        id_=note_id,
        fields="id,title,body,parent_id,is_todo,todo_completed,created_time,updated_time",
    )

    json.dump(
        {
            "note": {
                "id": note.id,
                "title": note.title,
                "body": note.body,
                "parent_id": note.parent_id,
                "is_todo": note.is_todo,
                "todo_completed": note.todo_completed,
                "created_time": note.created_time,
                "updated_time": note.updated_time,
            }
        },
        sys.stdout,
    )


main()
