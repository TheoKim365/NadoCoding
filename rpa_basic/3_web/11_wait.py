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
browser.get('https://m-flight.naver.com/')
time.sleep(5)

# 가는 날 검색 
# browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
# # ??? 잘 안됨 
# browser.find_elements(By.LINK_TEXT, '28')[0].click()
# browser.find_elements(By.LINK_TEXT, '30')[0].click()

# 제주도 클릭
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[7]/div/div[2]/div/ul/li[1]/button').click()

# 항공권 검색 클릭
browser.find_element(By.LINK_TEXT, '항공권 검색').click()


time.sleep(5)
browser.quit()