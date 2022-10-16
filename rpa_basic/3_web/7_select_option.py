from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.maximize_window()  # 창 최대화

# https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

## < case 1 > 
# # cars에 해당하는 element를 찾고, 드롭다운 내부에 있는 3번째 옵션을 선택 
# //*[@id="cars"]/option[3]
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[3]')
# time.sleep(5)
# elem.click()

## < case 2 > : 텍스트 값을 통해서 선택하는 방법 
# 옵션 중에서 텍스트가 Opel인 항목을 선택 
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Opel"]')
# time.sleep(5)
# elem.click()

## < case 3 > : 텍스트 값이 부분 일치하는 항목 선택하는 방법 
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "pe")]')
time.sleep(5)
elem.click()

time.sleep(5)
browser.quit()
