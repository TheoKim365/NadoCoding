import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"}

res = requests.get(url, headers=headers)
res.raise_for_status()                             
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)