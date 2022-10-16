'''
<html>
    <body>
        <iframe id = "1">
            <html>
                <body>
                    <div...>
                </body>
    </body>
'''

# //*[@id="html"]

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)


browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

elem = browser.find_element(by=By.XPATH, value='//*[@id="html"]')  # 성공

elem.click()

browser.switch_to.default_content()  # 상위로 빠져 나옴

elem = browser.find_element(by=By.XPATH, value='//*[@id="html"]')  # 실패

elem.click()

time.sleep(5)

browser.quit()