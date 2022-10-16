from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# 아래 3줄은 그 아래 Options()로 대체해도 문제 발생치 않음 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.maximize_window()
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print('curr_handel :', curr_handle)  # 현재 윈도우 핸들 정보 

# Try it Yourself 
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle)  # 각 핸들 정보
    browser.switch_to.window(handle)  # 각 핸들로 이동해서 
    print(browser.title)  # 출력해보면 현재 핸들 (브라우저)의 제목 출력 
    print()

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행 

# 그 브라우져 종료 
print('현재 핸들 닫기')
browser.close()

# 이전 핸들로 돌아오기
print('처음 핸들로 돌아오기')
browser.switch_to.window(curr_handle)

print(browser.title)  # HTML input type='radio'

# 브라우저 컨트롤이 가능한지 확인
time.sleep(5)
browser.get('http://daum.net')

time.sleep(5)
browser.quit()