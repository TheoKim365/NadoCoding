# Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성하시오

# 1. 그림판 실행 (단축키 : win + r, 입력값 : mspaint) 및 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
#  - 입력 글자 : "참 잘했어요"

# 3. 5초 대기 후 그림판 종료
#  이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

##============[답안 작성]=================================================================
import pyautogui
import sys

pyautogui.hotkey('win', 'r')  # 단축기 : win + r 입력 
pyautogui.write('mspaint')
pyautogui.press('enter')

# 그림판 나타날 때까지 2초 대기 
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle('제목 없음 - 그림판')[0]

if window.isMaximized == False:
    window.maximize()
# maximize_btn = pyautogui.locateOnScreen('maximize_btn.png')
# pyautogui.click(maximize_btn)

# 693,141 243,243,243 #F3F3F3
# locateonscreen 함수에서 image file은 project folder에 존재해야 함. 

# win + shift + s => capture 
btn_text = pyautogui.locateOnScreen('btn_text.png') #, region=(650, 100, 650 + 200, 100 + 200))
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print('찾기 실퍠')
    sys.exit()

# 흰 영역 클릭 
# pyautogui.click(800, 600, duration=0.5)

# 특정 위치에서 상대좌표 이용하여 위치 지정함 
btn_brush = pyautogui.locateOnScreen("btn_brush.png")  
pyautogui.click(btn_brush.left - 400, btn_brush.top + 600)

# 한글을 입력하기 위해 ...
import pyperclip  # 문장을 clipboard에 넣는 역할 

def my_write(text):
    pyperclip.copy(text)  # text를 클립보드에 저장 
    pyautogui.hotkey('ctrl', 'v')

my_write('참 잘했어요') 
pyautogui.sleep(2)

window.close()

pyautogui.sleep(1)    # 기다림...
btn_nosave = pyautogui.locateOnScreen('btn_nosave.png', confidence=0.8) #, region=(650, 100, 650 + 200, 100 + 200))
pyautogui.click(btn_nosave)

sys.exit()


## ===============  나도 코딩 해답  ==============================================================================
import sys
import pyautogui
import pyperclip

pyautogui.hotkey("win", "r") # 단축키 : win + r 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터 키 입력

# 그림판 나타날 때까지 2초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1개만 뜨워져 있다고 가정
#if window.isMaximized == False:
#    window.maximize() # 최대화

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png", confidence=0.8)
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
#pyautogui.click(200, 200, duration=0.5)

btn_brush = pyautogui.locateOnScreen("btn_brush.png")  
pyautogui.click(btn_brush.left - 200, btn_brush.top + 200)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n") # 저장하지 않음
