from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))  # 튜플 형태

## 변수 정의 
day_s = 27
month_s = 0    # 이번달 0, 다음달 1, 그 다음달 2
day_e = 30
month_e = 2    

# <Error message 해제> USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection:
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.maximize_window()
url = 'https://flight.naver.com/'
browser.get(url)

begin_date = browser.find_element(By.XPATH, '//button[text() =  "가는 날"]')
begin_date.click()

# time.sleep(1)   # 1초 대기
wait_until(f'//b[text()="{day_s}"]')   # 나올 때까지 30초 대기
browser.find_elements(By.XPATH, f'//b[text()="{day_s}"]')[month_s].click()

wait_until(f'//b[text()="{day_e}"]')   # 나올 때까지 30초 대기
browser.find_elements(By.XPATH, f'//b[text()="{day_e}"]')[month_e].click()

wait_until('//b[text()="도착"]')   # 나올 때까지 30초 대기
arrival = browser.find_element(By.XPATH, '//b[text()="도착"]')
arrival.click()

wait_until('//button[text()="국내"]')   # 나올 때까지 30초 대기
domestic = browser.find_element(By.XPATH, '//button[text()="국내"]')
domestic.click()

# //*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]

wait_until('//i[contains(text(), "제주국제공항")]')   # 나올 때까지 30초 대기
jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()

wait_until('//span[contains(text(), "항공권 검색")]')   # 나올 때까지 30초 대기
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

input('종료하려면 Enter키를 입력하세요')
browser.quit()