# [선정 안내 메일]
# 제목 : 파이썬 특강 안내 [선정]
# 본문 : xx님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 1번)


## ================== Start of my Solution ========================
import sys
from account import *
from email.message import EmailMessage   # 이 파일에서 keypoint 
import random

application_list = []  # 지원자 리스트

with 

## ================= End of my Solution =======================   
sys.exit()

from account import *
from imap_tools import MailBox

applicant_list = [] # 지원자 리스트

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)'): # 2020년 11월 7일 이후로 온 메일 조회
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번 : {} 닉네임 : {} 전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

# for applicant in applicant_list:
#     print(applicant)
