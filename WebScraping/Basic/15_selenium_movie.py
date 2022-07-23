from xml.sax.xmlreader import AttributesNSImpl
import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies?hl=ko&gl=kr'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# class = ULeU3b neq64b

# movies = soup.find_all("div", attrs={"class":["ULeU3b neq64b","hP61id"]})
movies = soup.find_all("div", attrs={"class":"VfPpkd-WsjYwc VfPpkd-WsjYwc-OWXEXe-INsAgc KC1dQ Usd1Ac AaN0Dd  MPNOXb"})
print(len(movies))



# listitems = soup.find_all("div", attrs={"class":"YMlj6b"})
# print(len(listitems))

# # with open("movie.html", "w", encoding='utf8') as f:
# #     # f.write(res.text)
# #     f.write(soup.prettify())

# for a_item in listitems:
#     a_item.find("div", attrs={"class":"YMlj6b"})
# print(len(movie_listitems))


# # for movie in movies:
# #     title = movie.find("div", attrs={"class":"hP61id"}).title()
# #     # class = hP61id
# #     print(title)
