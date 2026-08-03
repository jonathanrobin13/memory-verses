import fitz
from files import file


def excel_formatter(input_pdf_name, output_excel_name):

    # Open excel sheet
    excel_format_xlsx = file(output_excel_name, True)
    ws = excel_format_xlsx.active

    # Open PDF
    doc = fitz.open(file(input_pdf_name, False))

    for page in doc:

        blocks = page.get_text("dict")["blocks"]

        for block in blocks:

            if "lines" not in block:
                continue

            for line in block["lines"]:

                for span in line["spans"]:

                    if "5. Exodus" in span["text"]:

                        open_row += 1

                        ws.cell(open_row, 1).value = "5"
                        ws.cell(open_row, 2).value = "Exodus 34:7"

                    # If the font in bold, then that means it is a verse heading
                    elif span["font"] == "TimesNewRomanPS-BoldMT":

                        # sometimes there are empty spans and headings that don't have verses and there are headings, so skip them
                        if span["text"] == ' ' or "School" in span["text"] or span["text"] == "300 Bible Verses":
                            continue

                        # If the text is bolded, then that means that there was a verse completed

                        # splits verse number and reference
                        verse_heading = span["text"].split(sep=".", maxsplit=1)
                        verse_number = int(verse_heading[0])
                        reference = verse_heading[1]

                        open_row = verse_number + 1

                        # create cell
                        # add + 1 to verse_number so I can put heading for verse #, ref, and verse
                        verse_num_cell = ws.cell(open_row, 1)
                        reference_cell = ws.cell(open_row, 2)

                        # Put in the values
                        verse_num_cell.value = verse_number
                        reference_cell.value = reference

    excel_format_xlsx.save(file(output_excel_name, False))


if __name__ == "__main__":
    print("excelformatter.py")
    input_file = input("Name of input file : ")
    output_file = input("name of output file: ")
    excel_formatter(input_file, output_file)
