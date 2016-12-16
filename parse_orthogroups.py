import openpyxl

wb = openpyxl.load_workbook('orthomcl_results_rearranged.xlsx')
sheet = wb.get_sheet_by_name('All_strains')

for row in sheet.iter_rows(min_row=2, min_col=2, max_col=12, max_row=19952):
    for cell in row:
        test = str((cell).value)
        search = "t1"
        print test.count(search)
