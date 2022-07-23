import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# 네이버 웹툰 전체 목록 가져오기
soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("a", attrs={"class":"title"})

# class 속성이 title인 모든 "a" element를 반환 
for cartoon in cartoons:
    print(cartoon.get_text())


# # ---------------------------------------------------
# # <나의 학습> 모든 title을 sorting 해서 출력
# cartoons_lst = []
# for cartoon in cartoons:
#     # print(cartoon.get_text())
#     cartoons_lst.append(cartoon.get_text())

# cartoons_lst.sort()
# print(cartoons_lst, len(cartoons_lst))