# chrome://version = 103.0.5060.114 (공식 빌드) (64비트)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

## USB error meassage를 처리하기 위해 일부 (options) 수정 반영함 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
# browser = webdriver.Chrome(executable_path=r"C:\Users\wizue\PythonWorks\NadoCoding\chromedriver.exe", 
#                             options=options)

## 1.네이버로 이동
browser.get("https://naver.com")
# browser.get("https://daum.net")

## 2.로그인 버튼 클릭  
elem = browser.find_element(by=By.CLASS_NAME, value='link_login')
elem.click()

## 3.id, pw 입력
# browser.find_element(By.ID, "id").send_keys("naver_id")
# browser.find_element(By.ID, "pw").send_keys("naver_pw")
input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
        '.format(id="test_id", pw="test_pw")
time.sleep(random.uniform(1,3))   # 자동화탐지를 우회하기 위한 delay
browser.execute_script(input_js)
time.sleep(random.uniform(1,3))   # 자동화탐지를 우회하기 위한 delay

## 4.로그인 버튼 클릭
browser.find_element(By.ID, 'log.login').click()

time.sleep(3)

## 5.id를 새로 입력 
# browser.find_element(By.ID, "id").send_keys("my_id")
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

## 6.html 정보 출력
print(browser.page_source)

## 7.브라우져 종료
# browser.close()  # 현재 탭만 종료 
browser.quit()  # 전체 브라우져 종료 

# elem = browser.find_element(by=By.NAME, value='q')
# elem.send_keys('나도코딩')
# elem = browser.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
# elem.send_keys(Keys.ENTER)