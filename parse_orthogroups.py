import openpyxl

wb = openpyxl.load_workbook('orthomcl_results_rearranged.xlsx')
sheet = wb.get_sheet_by_name('All_strains')

for row in range(1, sheet.max_row +1):
    Orthogroups = sheet['A' + str(row)].value
    A4 = sheet['B' + str(row)].value
    Bc1 = sheet['C' + str(row)].value
    Bc16 = sheet['D' + str(row)].value
    Bc23 = sheet['E' + str(row)].value
    Nov27 = sheet['F' + str(row)].value
    Nov5 = sheet['G' + str(row)].value
    Nov71 = sheet['H' + str(row)].value
    Nov77 = sheet['I' + str(row)].value
    Nov9 = sheet['J' + str(row)].value
    ONT3 = sheet['K' + str(row)].value
    SCRP25_v2 = sheet['L' + str(row)].value
