import pyautogui
# file_menu = pyautogui.locateOnScreen('file_menu.png')

# # ctrl (win) alt space 버튼 순서
# # (win) + shift + s    #------> screen capture 가능 화면으로 전환 
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen('trash_icon.png')
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen('screenshot.png')
# print(screen)

# 같은 이미지가 두개 이상 있을 경우
# for i in pyautogui.locateAllOnScreen('checkbox.png'):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen('checkbox.png')
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen('trash_icon.png')
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen('trash_icon.png', grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정 
# trash_icon = pyautogui.locateOnScreen('trash_icon.png', region=(x, y, width, height))
# trash_icon = pyautogui.locateOnScreen('trash_icon.png', region=(2447, 1045, 2875 - 2447, 1165 - 1045))
# pyautogui.moveTo(trash_icon)
# pyautogui.mouseInfo()
## 2447,1045 30,30,30 #1E1E1E
## 2875,1165 30,30,30 #1E1E1E

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen('run_btn.png', confidence=0.5)  # 신뢰도 50% 
# pyautogui.moveTo(run_btn)

# 4. 자동화 대상이 바로 보여지지 않는 경우
## 1)계속 기다리기 
# file_menu_notepad = pyautogui.locateOnScreen('file_menu_notepad.png')
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print('발견 실패')

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen('file_menu_notepad.png')
#     print('발견 실퍠')
# pyautogui.click(file_menu_notepad)

## 2) 일정 시간동안 기다리기 (Timeout)
import time
import sys

# timeout = 10 # 대기 시간 
# start = time.time()  # 시작 시각을 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen('file_menu_notepad.png')
#     end = time.time()  # 종료 시각 결정 
#     if end - start > timeout : # 지정한 대기시간을 초과하면 
#         print('시간 종료')
#         sys.exit()

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f'[Timeout {timeout}s] Target not found ({img_file}). Terminate program.')
        sys.exit()

# pyautogui.click(file_menu_notepad)

my_click('file_menu_notepad.png', 10)