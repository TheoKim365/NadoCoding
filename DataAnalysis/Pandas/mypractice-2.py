import xlwings as xw
import pandas as pd
import sys 

dir = 'D:\d.도서목록 (Document Control Log)'
f_name = 'PMIS 성과물 관리대장-20220914'     # xlsx 형식 파일 

wb = xw.book(f'{dir}\{f_name}.xlsx')
ws = wb.sheets[0]
df = ws['a4'].expand().options(pd.DataFrame).value
wb.app.quit()



