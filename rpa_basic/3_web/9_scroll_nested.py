from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.get('https://www.w3schools.com/html/')
browser.maximize_window()  # 창 최대화

time.sleep(5)

# 특정 영역 스크롤 
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[62]')

# # 방법 1) : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# # 방법 2) : 좌표 정보 이용 
# xy = elem.location_once_scrolled_into_view  # 함수가 아니니까 () 쓰지 마세요. 
# print('type :', type(xy))  # dict
# print('value :', xy)

time.sleep(2)
elem.click()     # 위치로 scroll 하지 않은 상태에서도 xpath가 정확하면 click 가능 

time.sleep(5)
browser.quit()
