from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.maximize_window()  # 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

browser.switch_to.frame('iframeResult')

# elem = browser.find_element(by=By.XPATH, value='//*[@id="vehicle1"]')
elem = browser.find_element(By.ID, 'vehicle1')

time.sleep(5)   # 이 시간동안 check_box를 check하면...

if elem.is_selected() == False:
    print('선택 안되어 있으므로 선택')
    elem.click()
else:
    print('선택되어 있으므로 아무 것도 안함')

time.sleep(5)
browser.quit()