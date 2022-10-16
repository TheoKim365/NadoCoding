import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import lxml
import os
import sys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# browser.maximize_window()

# 1. 페이지 이동 
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url) 

# 2. 조회 항목 초기화 (체크되어 )
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected():  # 체크된 상태라면? 
        checkbox.click()        # 클릭 (체크 해제)

# 3. 조회 항목을 설정 
items_to_select = ['영업이익','자산총계','매출액']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..')  # 부모 element를 찾음 
    label = parent.find_element(By.TAG_NAME, 'label')
    # print(label.text)  # 이름 확인
     
    if label.text in items_to_select:  # 선택 항목
        checkbox.click()  # 체크

# 4. 적용하기 버튼
# //*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]/img
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1, 45):  # 1부터 40미만 페이지 반복
    # 사전 작업 : 페이지 이동 
    browser.get(url + str(idx))

    # 5. 데이터 추출 
    # df = pd.read_html(browser.page_source)
    # print(len(df))   # df의 갯수 => 3 

    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0:  # 더 이상 가져올 데이타가 없으면? 
        break
    
    # 6. 파일 저장
    f_name = 'sise.csv'
    if os.path.exists(f_name):  # 파일이 있다면? 헤더 제외 
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else:
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
    print(f'{idx} 페이지 완료')

browser.quit()  # 브라우저 종료 
