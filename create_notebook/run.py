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
    if "parent_id" in params:
        kwargs["parent_id"] = params["parent_id"]

    notebook_id = api.add_notebook(**kwargs)
    json.dump({"notebook_id": notebook_id}, sys.stdout, cls=DateTimeEncoder)


main()
