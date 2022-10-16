import time
print(time.strftime('%d-%b-%Y'))  # 현재 날짜를 일-월-연도 

import datetime
dt = datetime.datetime.strptime('2022-8-28', '%Y-%m-%d')
print(type(dt))
print(dt.strftime('%d-%b-%Y'))