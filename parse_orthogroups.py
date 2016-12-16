import openpyxl

wb = load_workbook('orthomcl_results_rearranged.xlsx')
sheet = wb.get_sheet_by_name('All_strains')
