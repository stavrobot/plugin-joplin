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
    json.load(sys.stdin)  # no parameters expected

    api = get_client()
    tags_raw = api.get_all_tags()

    tags = [{"id": tag.id, "title": tag.title} for tag in tags_raw]
    json.dump({"tags": tags}, sys.stdout)


main()
