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
    json.load(sys.stdin)  # no parameters expected

    api = get_client()
    notebooks_raw = api.get_all_notebooks()

    notebooks = [
        {"id": notebook.id, "title": notebook.title, "parent_id": notebook.parent_id}
        for notebook in notebooks_raw
    ]
    json.dump({"notebooks": notebooks}, sys.stdout, cls=DateTimeEncoder)


main()
