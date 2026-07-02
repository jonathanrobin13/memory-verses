import openpyxl
import requests
from dotenv import load_dotenv
import os

load_dotenv()

ESV_API_KEY = os.getenv("ESV_API_KEY")

url = "https://api.esv.org/v3/passage/text/"

headers = {
    "Authorization": f"Token {ESV_API_KEY}"
}

params = {
    "q": "Genesis 1:1;John 3:16",
    "include-passage-references": False,
    "include-verse-numbers": False,
    "include-first-verse-numbers": False,
    "include-footnotes": False,
    "include-footnote-body": False,
    "include-headings": False,
    "include-short-copyright": False,



}

response = requests.get(
    url,
    headers=headers,
    params=params
)

data = response.json()

for verse in data["passages"]:
    print(verse.strip())
