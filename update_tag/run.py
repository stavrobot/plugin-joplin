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
    title = params["title"]

    api = get_client()
    api.modify_tag(id_=tag_id, title=title)
    json.dump({"success": True}, sys.stdout, cls=DateTimeEncoder)


main()
