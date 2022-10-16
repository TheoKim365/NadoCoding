# Project) 나도 코딩에서 구독자 분들을 대상으로 파이썬 특강을 진행합니다.
# 참여 신청은 이메일을 통해 가능하며 메일 수신 시간 기준으로 선착순 3명이 선정됩니다.
# 아래 조건에 해당하는 메일을 자동으로 조회하여 선정되신 분들께는 선정 안내 메일을, 
# 아쉽게 선정되지 못한 분들께는 대기 번호 안내 메일을 자동으로 발신하고, 
# 선정된 3명의 명단을 엑셀 파일로 저장하는 자동화 프로그램을 작성하시오. 

# [신청 메일 양식]
# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
#    (예) 나도코딩/1234

'''
##================ 나의 해결책 =========================

import smtplib
from account import *
from email.message import EmailMessage   # 이 파일에서 keypoint 
import random
import sys

msg = EmailMessage()
msg["Subject"] = "파이썬 특강 신청합니다."  # 제목
msg['From'] = EMAIL_ADDRESS          # 보내는 사람 
msg['To'] = 'wizuever@gmail.com'     # 받는 사람 

phone_no = random.randint(1000, 9999)
msg.set_content(f'테오/ {phone_no}')  # 본문 

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

##================== end of my solution =============================
'''

import smtplib
from random import *
from account import *
from email.message import EmailMessage

nicknames = ["유재석", "박명수", "정형돈", "노홍철", "조세호"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "wizuever@gmail.com"

        #content = nickname + "/" + str(randint(1000, 9999))
        content = "/".join([nickname, str(randint(1000, 9999))])
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 wizu 지메일 계정으로 메일 발송 완료")