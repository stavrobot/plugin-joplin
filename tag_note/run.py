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
    tag_id = params["tag_id"]
    note_id = params["note_id"]

    api = get_client()
    api.add_tag_to_note(tag_id=tag_id, note_id=note_id)
    json.dump({"success": True}, sys.stdout, cls=DateTimeEncoder)


main()
