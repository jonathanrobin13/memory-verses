from files import file

from api_handler import import_json
import requests

from tqdm import tqdm

import time


def esv_trans(input_file, output_file):

    input_file = file(input_file, True)
    ws = input_file.active

    output_file = file(output_file, True)
    ws_new = output_file.active

    url, headers, params = import_json()

    session = requests.Session()

    for row in tqdm(range(2, ws.max_row+1)):
        reference_cell = ws.cell(row, 2)
        reference = reference_cell.value

        ws_new.cell(row, 2).value = reference

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
            print(reference)
            print(verse)
            print(row)
            time.sleep(60)

    session.close()

    output_file.save(file(output_file, False))


if __name__ == "__main__":
    print("esv_trans.py")
    input_file = input("Name of input file : ")
    output_file = input("name of output file: ")
    esv_trans(input_file, output_file)
