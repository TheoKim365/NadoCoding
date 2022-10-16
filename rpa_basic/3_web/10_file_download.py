from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

## 아래 3줄은 그 아래 Options()로 대체해도 문제 발생치 않음 
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# browser = webdriver.Chrome(options=options)

chrome_options = Options()
chrome_options.add_experimental_option('prefs', 
        {'download.default_directory':r'C:\Users\wizue\PythonWorks\NadoCoding'})
browser = webdriver.Chrome(options=chrome_options)

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
browser.maximize_window()  # 창 최대화

browser.switch_to.frame('iframeResult')

# download 링크 클릭
elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()

time.sleep(5)
browser.quit()