import openpyxl as xl

from files import file

from dotenv import load_dotenv
import os
import requests

from tqdm import tqdm

import time


excel_format_xlsx = file("Excel_Format.xlsx", True)
ws = excel_format_xlsx["Verses"]

esv_verses_xlsx = file("ESV_Verses.xlsx", True)
ws_new = esv_verses_xlsx["Verses"]


load_dotenv()

ESV_API_KEY = os.getenv("ESV_API_KEY")

url = "https://api.esv.org/v3/passage/text/"

headers = {
    "Authorization": f"Token {ESV_API_KEY}"
}

params = {
    "include-passage-references": False,  # make false
    "include-verse-numbers": False,
    "include-first-verse-numbers": False,
    "include-footnotes": False,
    "include-footnote-body": False,
    "include-headings": False,
    "include-short-copyright": False,
    "indent-poetry": False,
    "include-selahs": False
}


references = []

session = requests.Session()

for row in tqdm(range(2, 302)):
    reference_cell = ws.cell(row, 2)
    reference = reference_cell.value

    params["q"] = reference

    response = session.get(
        url,
        headers=headers,
        params=params
    )

    verse = response.json()

    verse_cell = ws_new.cell(row, 3)

    try:
        verse_cell.value = verse['passages'][0].strip()
    except KeyError:
        print(verse)
        print(row)
        time.sleep(60)

session.close()


esv_verses_xlsx.save(file("ESV_Verses.xlsx", False))


#     for index in range(0, len(references)):
#         if index == 0:
#             params["q"] = references[index]
#             continue

#         params["q"] = params["q"] + ";" + references[index]
