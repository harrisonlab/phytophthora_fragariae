import openpyxl

wb = openpyxl.load_workbook('orthomcl_results_rearranged.xlsx')
sheet = wb.get_sheet_by_name('All_strains')

for i in range(1,1,1):
    l = print(i, sheet.cell(row=i, column=2).value)
    print len(l)
