# Quiz) Selenium 을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오

# 1. https://www.w3schools.com 접속 (URL 은 구글에서 w3schools 검색)
# 2. 화면 중간 LEARN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력
#   First Name : 나도
#   Last Name : 코딩
#   Country : Canada
#   Subject : 퀴즈 완료하였습니다.
#   ※ 위 값들은 변수로 미리 저장해두세요
# 6. 5초 대기 후 Submit 버튼 클릭
# 7. 5초 대기 후 브라우저 종료 

## ================ solution =======================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# 변수 정의 
first_name = '나도'
last_name = '코딩'
country = 'Canada'
subject = '퀴즈 완료하였습니다.'
url = 'https://www.w3schools.com'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.maximize_window()

# 1. https://www.w3schools.com 접속 (URL 은 구글에서 w3schools 검색)
browser.get(url)


# 2. 화면 중간 LEARN HTML 클릭
# //*[@id="main"]/div[2]/div/div[1]/a[1]
browser.find_element(By.LINK_TEXT,'Learn HTML').click()

# 3. 상단 메뉴 중 HOW TO 클릭
# //*[@id="topnav"]/div/div[1]/a[10]
browser.find_element(By.LINK_TEXT,'HOW TO').click()

# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# //*[@id="leftmenuinnerinner"]/a[118]
# browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[118]').click()
browser.find_element(By.LINK_TEXT, 'Contact Form').click()  # contact form이 2개 이상 있는 경우 실패 
# 가장 좋은 방법 (텍스트 전체 일치 비교)
browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
# 일부만 일치하는 경우 
# browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()

# 5. 입력란에 아래 값 입력
browser.find_element(By.ID, 'fname').send_keys(first_name)
browser.find_element(By.ID, 'lname').send_keys(last_name)

# < case 2 > : 텍스트 값을 통해서 선택하는 방법 
browser.find_element(By.XPATH, f'//*[@id="country"]/option[text()="{country}"]').click()
# time.sleep(5)
# elem.click()

# //*[@id="main"]/div[3]/textarea
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)
browser.find_element(By.LINK_TEXT, 'Submit')
print('Submit 클릭하였습니다.')

time.sleep(5)
browser.quit()


