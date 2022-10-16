from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.maximize_window()  # 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

elem = browser.find_element(by=By.XPATH, value='//*[@id="html"]')

# 선택이 안되어 있으면 선택하기
if elem.is_selected() == False:   # 라디오 버튼이 선택되어 있지 않으면 
    print('선택되어 있지 않으면 선택하기')
    elem.click()
else:  # 라이오 버튼이 선택되어 있으면 
    print('선택되어 있으므로 아무 것도 않함')

time.sleep(5)

# 선택이 안되어 있으면 선택하기
if elem.is_selected() == False:   # 라디오 버튼이 선택되어 있지 않으면 
    print('선택되어 있지 않으면 선택하기')
    elem.click()
else:  # 라이오 버튼이 선택되어 있으면 
    print('선택되어 있으므로 아무 것도 않함')

browser.quit()