import openpyxl as xl

from files import file

from API_System.api_handler import import_json
import requests

from tqdm import tqdm

import time


excel_format_xlsx = file("Excel_Format.xlsx", True)
ws = excel_format_xlsx["Verses"]

esv_verses_xlsx = file("ESV_Verses.xlsx", True)
ws_new = esv_verses_xlsx["Verses"]


url, headers, params = import_json()


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
