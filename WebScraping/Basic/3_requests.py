import requests

# res = requests.get("http://naver.com")
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()                                # 위와 짝을 이루어 사용함 

'''
print('응답코드 : ', res.status_code) # 200 이면 정상 

if res.status_code == requests.codes.ok:
    print('정상입니다')
else:
    print('문제가 생겼습니다. [에러코드', res.status_code, ']')

res.raise_for_status()   # 문제가 있으면 바로 끝낸다.
print('웹 스크래핑을 진행합니다.') 
'''

# print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)