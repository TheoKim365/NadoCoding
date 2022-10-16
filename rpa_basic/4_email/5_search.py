import mailbox
from imap_tools import MailBox
from account import *

# mailbox = MailBox('imap.gmail.com', 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX')
# mailbox.logout()

# logout 필요 없음
with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True):  # 전체 메일 다 가져오기 
    #     print('[{}] {}'.format(msg.from_, msg.subject))
    
    # n = 1
    # for msg in mailbox.fetch('(UNSEEN)'):  # 읽지 않은 메일  
    #     print('<{n}> [{}] {}'.format(n, msg.from_, msg.subject))
    #     n += 1

    # n = 1
    # for msg in mailbox.fetch('(FROM wizuever@gmail.com)'):  # 특정인 보낸 메일 가져오기
    #     print('<{}> [{} {}] {}'.format(n, msg.from_, msg.date, msg.subject))
    #     n += 1

    # n = 1
    # # "(TEXT 'test mail')"   => error 발생 
    # for msg in mailbox.fetch('(TEXT "test mail")'):  # 특정 문구 포함 (제목, 본문)
    #     print('<{}> [{} {}] {}'.format(n, msg.from_, msg.date, msg.subject))
    #     n += 1
    
    # n = 1
    # for msg in mailbox.fetch('(SUBJECT "test mail")'):  # 특정 문구 포함 (제목만)
    #     print('<{}> [{} {}] {}'.format(n, msg.from_, msg.date, msg.subject))
    #     n += 1

    # # 한글 사용시 error
    # n = 1
    # for msg in mailbox.fetch('(SUBJECT "테스트")'):  # 한글 사용시 error
    #     print('<{}> [{} {}] {}'.format(n, msg.from_, msg.date, msg.subject))
    #     n += 1

    # n = 1
    # for msg in mailbox.fetch(limit=5, reverse=True):  # 한글을 포함하는 메일 필터링
    #     if "테스트" in msg.subject:
    #         print('<{}> [{} {}] {}'.format(n, msg.from_, msg.date, msg.subject))
    #         n += 1

    # n = 1
    # for msg in mailbox.fetch('(SENTSINCE 07-Aug-2022)'):  # 특정 날짜 이후 메시지
    #     if "테스트" in msg.subject:
    #         print('<{}> [{} {}] {}'.format(n, msg.from_, msg.date, msg.subject))
    #         n += 1

    # n = 1
    # for msg in mailbox.fetch('(ON 27-Aug-2022)', reverse=True):  # 특정 날짜 이후 메시지
    #     if "테스트" in msg.subject:
    #         print('<{}> [{} {}] {}'.format(n, msg.from_, msg.date, msg.subject))
    #         n += 1
    #     # query 관련해서는 google의 imap tools 로 검색 

    # # 두가지 이상의 조건을 모두 만족하는 메일 (AND 조건)
    # n = 1
    # for msg in mailbox.fetch('(ON 27-Aug-2022 SEEN)', reverse=True, limit=10):  # 특정 날짜 이후 메시지
    #         print('<{}> [{} {}] {}'.format(n, msg.from_, msg.date, msg.subject))
    #         n += 1

    # 2가지 조건 중 하나를 만족하는 메일 (OR 조건)
    n = 1
    for msg in mailbox.fetch('(OR ON 27-Aug-2022 SEEN)', reverse=True, limit=10):  # 특정 날짜 이후 메시지
            print('<{}> [{} {}] {}'.format(n, msg.from_, msg.date, msg.subject))
            n += 1