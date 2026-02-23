#!/usr/bin/env -S uv run
# /// script
# dependencies = ["joppy"]
# ///

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from helpers import get_client, DateTimeEncoder

# Joplin internal links use the ":/" prefix before the note ID.
INTERNAL_LINK_PATTERN = re.compile(r"\[(?:[^\]]*)\]\(:\/([a-f0-9]+)\)")
# Standard markdown links that are not Joplin internal links.
EXTERNAL_LINK_PATTERN = re.compile(r"\[(?:[^\]]*)\]\(((?!:\/)[^)]+)\)")


def main() -> None:
    params = json.load(sys.stdin)
    note_id = params["note_id"]

    api = get_client()
    note = api.get_note(id_=note_id, fields="body")

    body = note.body or ""
    internal_links = INTERNAL_LINK_PATTERN.findall(body)
    external_links = EXTERNAL_LINK_PATTERN.findall(body)

    json.dump(
        {"internal_links": internal_links, "external_links": external_links},
        sys.stdout,
        cls=DateTimeEncoder,
    )


main()
