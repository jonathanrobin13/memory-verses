from pathlib import Path
from openpyxl import load_workbook


def file(fileName, returnWorkbook):
    project_folder = Path(__file__).parent.parent

    file_path = project_folder / "data" / fileName

    if returnWorkbook:
        wb = load_workbook(file_path)
        return wb
    else:
        return file_path
