!pip install openpyxl
import openpyxl
import pandas as pd
import glob

import_file_path = 'Desktop/Mypandas/sample-1.xlsx'
excel_sheet_name = '発注管理表'
export_file_path = 'Desktop/Mypandas/output'

df_order = pd.read_excel(import_file_path, sheet_name = excel_sheet_name)

company_name = df_order['会社名'].unique()
for i in company_name:
    df_order_company = df_order[df_order['会社名'] == i]
    print(df_order_company)

# gitテスト