import requests
import re
import sys
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"}

for i in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)

    res = requests.get(url, headers= headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-prodect")})
    for item in items:
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"}) # 제품명
        if ad_badge:
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()  # 제품명
        if "Apple" in name:
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()  # 가격
        rate = item.find("em", attrs={"class":"rating"})  # 평점 
        if rate:
            rate = rate.get_text()
        else:
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})  # 평점 수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]  # 예: (26)
        else:
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        if float(rate) >= 4.5 and int(rate_cnt) >= 50: 
            print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt})개")
            print("바로가기: {}".format("https://www.coupang.com" + link))
            print("-" * 100)    # 줄긋기

            
