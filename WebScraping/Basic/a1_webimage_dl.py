import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

max_cnt = 20
keyword = '셔틀 버스'
url = f'https://www.pexels.com/ko-kr/search/{keyword}/'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

photo_items = browser.find_elements(By.CLASS_NAME, 'BreakpointGrid_item__erUQQ')
# photo_items = browser.find_elements(By.XPATH, '//*[@id="-"]/div[1]/div[1]/div[2]/div[1]/article')
# print(photo_items)

img_urls = [x.get_attribute('href') for x in photo_items]
print(img_urls)

# idx = 1
# for img_url in img_urls:
#     browser.get(img_url)

#     res = requests.get(img_url)
#     if res.ok:
#         file_name = f'{keyword}_{idx}.jpeg'
#         with open(file_name, 'wb') as f:
#             f.write(res.content)
#         print(f'({idx}) {file_name}')   # (2) wallpaper_2.jpeg
#         idx += 1
#     if idx > max_cnt:
#         break
# browser.quit()


# spacing_noMargin__Q_PsJ MediaCard_image__ljFAl