import openpyxl

wb = openpyxl.load_workbook('orthomcl_results_rearranged.xlsx')
sheet = wb.get_sheet_by_name('All_strains')

for row in range(1, sheet.max_row +1):
    Orthogroups = sheet['A' + str(row)]
    A4 = sheet['B' + str(row)]
    Bc1 = sheet['C' + str(row)]
    Bc16 = sheet['D' + str(row)]
    Bc23 = sheet['E' + str(row)]
    Nov27 = sheet['F' + str(row)]
    Nov5 = sheet['G' + str(row)]
    Nov71 = sheet['H' + str(row)]
    Nov77 = sheet['I' + str(row)]
    Nov9 = sheet['J' + str(row)]
    ONT3 = sheet['K' + str(row)]
    SCRP25_v2 = sheet['L' + str(row)]

print(A4)
