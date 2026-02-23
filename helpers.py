# /// script
# dependencies = ["joppy"]
# ///

import json
from pathlib import Path

from joppy.client_api import ClientApi


def load_config() -> dict:
    config_path = Path(__file__).resolve().parent / "config.json"
    return json.loads(config_path.read_text())


def get_client() -> ClientApi:
    config = load_config()
    return ClientApi(
        token=config["joplin_token"],
        url=config.get("joplin_url", "http://localhost:41184"),
    )
