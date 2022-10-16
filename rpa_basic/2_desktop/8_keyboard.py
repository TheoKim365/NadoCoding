import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]  # 메모장 1개 띄운 상태에서 가져옴.
w.activate()

# pyautogui.write('12345')
# pyautogui.write('NadoCoding', interval=0.25)
# pyautogui.write('나도 코딩')  # 한글 안됨. 

# pyautogui.write(['t','e','s','t','left','left','right','l','a','enter'])
# t e s t를 적고 왼쪽 방향키 2번 오른쪽 방향키 1번, l, a 순서대록 적고 enter 입력 
# <참고> 'automate the boring stuff with python'으로 검색 -> keyboard attribute... 로 찾기 

# 특수 문자
# shift 4 -> $ 
# pyautogui.keyDown('shift')  # shift 키를 누른 상태에서 
# pyautogui.press('4')  # 숫자 4를 입력하고 
# pyautogui.keyUp()

# 조합키 (Hot Key)
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('a')
# pyautogui.keyup('a')   # press('a')
# pyautogui.keyup('ctrl')  # Ctrl + A

# 간편한 조합키
# pyautogui.hotkey('ctrl', 'alt', 'shift', 'a')
# ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 > Shift 떼고 > Alt 떼고 > Ctrl 떼고
# pyautogui.hotkey('ctrl', 'a')

# ##=============================================================================
# import pyperclip  # 문장을 clipboard에 넣는 역할 
# # pyperclip.copy('나도코딩') # '나도코딩' 글자를 클립보드에 저장 
# # pyautogui.hotkey('ctrl', 'v')  # 클립보드에 있는 내용을 붙여넣기 

# def my_write(text):
#     pyperclip.copy(text)
#     pyautogui.hotkey('ctrl', 'v') 

# my_write('나의 메모지')

# 자동화 프로그램 종료 
# win : ctrl + alt + del 
# mac : cmd + shift + option + q 