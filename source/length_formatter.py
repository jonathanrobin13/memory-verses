from openpyxl import load_workbook, Workbook
from files import file

# Load the original workbook
# old_wb = load_workbook(r"C:\Users\robin\memory-verse\data\ESV Verses.xlsx")
# old_ws = old_wb["Verses"]

esv_verses_xlsx = file("ESV_Verses.xlsx", True)
old_ws = esv_verses_xlsx["Verses"]

# Create a new workbook
verses_sorted_xlsx = file("verses_sorted.xlsx", True)
new_ws = verses_sorted_xlsx["Sorted Verses"]


rows = []

# Skip the blank first row
for row in old_ws.iter_rows(min_row=2, values_only=True):

    reference = row[1]   # Column B
    verse = row[2]       # Column C

    # Count every character
    length = len(verse) if verse else 0

    rows.append((length, reference, verse))

# Sort by verse length
rows.sort(key=lambda x: x[0])

# Write the sorted data
for i, (_, reference, verse) in enumerate(rows, start=2):
    new_ws.cell(row=i, column=1).value = i - 1
    new_ws.cell(row=i, column=2).value = reference
    new_ws.cell(row=i, column=3).value = verse

# Save the new workbook
verses_sorted_xlsx.save(file("verses_sorted.xlsx", False))
