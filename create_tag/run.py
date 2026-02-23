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
    title = params["title"]

    api = get_client()
    tag_id = api.add_tag(title=title)
    json.dump({"tag_id": tag_id}, sys.stdout, cls=DateTimeEncoder)


main()
