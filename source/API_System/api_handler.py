from dotenv import load_dotenv
import os
import json
from pathlib import Path


def import_json():

    api_settings = Path(__file__).parent / "api_settings.json"

    with open(api_settings, "r") as file:
        config = json.load(file)

    url = config["url"]
    params = config["verse-parameters"]

    load_dotenv()

    ESV_API_KEY = os.getenv("ESV_API_KEY")

    headers = config["headers"]
    headers["Authorization"] = f"Token {ESV_API_KEY}"

    return url, headers, params
