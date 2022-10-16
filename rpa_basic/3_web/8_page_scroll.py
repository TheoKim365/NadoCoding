from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.maximize_window()  # 창 최대화

browser.get('https://shopping.naver.com/home/p/index.naver')

# 검색창을 xpath로 찾기 
elem = browser.find_element(By.XPATH, 
        '//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
elem.send_keys('무선마우스')

time.sleep(1)
elem.send_keys(Keys.ENTER)

# 스크롤
# # 1) 지정한 위치로 스크롤 내리기
# browser.execute_script('windows.scrollTo(0,1080)')  # 모니터 해상도에 따라 다름 
# browser.execute_script('windows.scrollTo(0,2080)')

# # 2) 화면 가장 아래로 스크롤 내리기 
# browser.execute_script('windows.scrollTo(0,document.body.scrollHeight)')

# 3) 동적 페이지에 대해서 마지막까지 스크롤 반복 수행 
interval = 2 # 2초에 한번씩 스크롤 내리기 

# 현재 문서 높이를 가져와서 저장 
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행 
while True:
    # 스크롤 화면 가장 아래로 내림 
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    
    # 페이지 로딩 대기 
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장 
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:  # 직전 높이와 같으면, 높이 변화가 없으면 
        break  # 반복문 탈출 (모든 스크롤 동작 완료)
    
    prev_height = curr_height

# 맨 위로 올리기 
browser.execute_script('window.scrollTo(0,0)')

time.sleep(5)
browser.quit()
