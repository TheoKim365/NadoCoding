## get 방식 
# https://www.coupang.com/np/search?
# q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&
# component=&eventCategory=SRP&trcid=&traid=&
# sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&
# filterType=&listSize=36&filter=&isPriceRange=false&
# brand=&offerCondition=&rating=0&page=5&rocketAll=false&
# searchIndexingToken=1=6&backgroundColor=

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=9&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"}

res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-prodect")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"}) # 제품명
    if ad_badge:
        print("  <광고 상품 제외합니다>")
        continue

    # 애풀 제품 제외
    name = item.find("div", attrs={"class":"name"}).get_text()  # 제품명
    if "Apple" in name:
        print("  <Apple 상품 제외합니다>")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()  # 가격

    # 평점 4.5 이상, 리뷰 50개 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})  # 평점 
    if rate:
        rate = rate.get_text()
    else:
        print("  <평점 없는 상품 제외합니다>")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})  # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()  # 예: (26)
        rate_cnt = rate_cnt[1:-1]
        # print("리뷰 수", rate_cnt)
    else:
        print("  <평점 수 없는 상품 제외합니다>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 50: 
        print(name, price, rate, rate_cnt)