from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active

# ws.delete_rows(8)
# ws.delete_rows(8, 3) # 8번째 줄부터 3줄의 데이터 삭제

# ws.delete_cols(2) # 2번째 열 삭제
ws.delete_cols(2) # 2번째 열 삭제
ws.delete_cols(2, 2) # 2번째 열부터 2열 삭제


# wb.save('sample_delete_rows.xlsx')
wb.save('sample_delete_cols.xlsx')