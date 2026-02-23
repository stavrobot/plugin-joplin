# /// script
# dependencies = ["joppy"]
# ///

import json
from datetime import datetime
from pathlib import Path

from joppy.client_api import ClientApi


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj: object) -> object:
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def load_config() -> dict:
    config_path = Path(__file__).resolve().parent / "config.json"
    return json.loads(config_path.read_text())


def get_client() -> ClientApi:
    config = load_config()
    return ClientApi(
        token=config["joplin_token"],
        url=config.get("joplin_url", "http://localhost:41184"),
    )
