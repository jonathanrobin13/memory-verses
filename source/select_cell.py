from files import file


def select_cells(input_filename, output_filename):

    input_file = file(input_filename, True)
    sheet = input_file.active

    output_file = file(output_filename, True)
    new_sheet = output_file.active

    new_sheet.delete_rows(2, new_sheet.max_row)

    print("Type all the references  that you want. Split each reference by a comma.")
    print("For example, Proverbs 3:16,Genesis 1:1,John 3:16")
    references = input()

    verses_to_get = references.split(",")

    open_row = 2

    for reference in verses_to_get:
        while True:
            found = False

            for row in sheet.iter_rows(min_row=2):
                if reference in row[1].value:
                    verse = row[2].value
                    new_sheet.cell(open_row, 3).value = verse
                    found = True
                    break

            if found:
                break
            else:
                reference = input(
                    f"{reference} not found, please type it again\n")

        new_sheet.cell(open_row, 2).value = reference
        new_sheet.cell(open_row, 1).value = open_row - 1

        open_row += 1

    output_file.save(file(output_filename, False))


if __name__ == "__main__":
    print("select_cell.py")
    input_file = input("Name of input file : ")
    output_file = input("name of output file: ")
    select_cells(input_file, output_file)
