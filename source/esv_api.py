import requests
from dotenv import load_dotenv
import os

load_dotenv()

ESV_API_KEY = os.getenv("ESV_API_KEY")


def sendAPI(references, session):

    url = "https://api.esv.org/v3/passage/text/"

    headers = {
        "Authorization": f"Token {ESV_API_KEY}"
    }

    params = {
        "include-passage-references": False,
        "include-verse-numbers": False,
        "include-first-verse-numbers": False,
        "include-footnotes": False,
        "include-footnote-body": False,
        "include-headings": False,
        "include-short-copyright": False,
    }

    response = session.get(
        url,
        headers=headers,
        params=params
    )

    data = response.json()

    for verse in data["passages"]:
        print(verse.strip())
