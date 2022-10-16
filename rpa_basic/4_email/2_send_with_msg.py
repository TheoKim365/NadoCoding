import smtplib
from account import *
from email.message import EmailMessage   # 이 파일에서 keypoint 

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"  # 제목
msg['From'] = EMAIL_ADDRESS          # 보내는 사람 
msg['To'] = 'wizuever@gmail.com'     # 받는 사람 

# 여러 명에게 메일을 보낼 때
# msg['To'] = 'wizuever@gmail.com', 'wizuever@msn.com'
# to_list = ['wizuever@gmail.com', 'wizuever@msn.com']
# msg['To'] = ','.join(to_list)  # join 문법 : ,를 이용하여 to_list의 리스트를 조인함 

# 참조
msg['Cc'] = 'wizuever@gmail.com'

# 비밀참조
msg['Bcc'] = 'wizuever@msn.com'

msg.set_content('테트트 본문입니다.')  # 본문 

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
