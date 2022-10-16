from pprint import pp
import pyautogui

# pyautogui.sleep(3)  # 3초 대기
# print(pyautogui.position())

# pyautogui.click(110, 21, duration=1)  # 1초 동안 좌표로 이동 후 마우스 클릭

# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200, 500)
# pyautogui.mouseDown()  # 마우스 누른 상태 
# pyautogui.moveTo(500, 700)
# pyautogui.mouseUp()  # 마우스 뗀 상태 

pyautogui.sleep(3)  # 3초 대기
# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(1844, 703)
# pyautogui.drag(100, 0)   # 현재 위치 기준으로 x 100만큼 이동
# pyautogui.drag(100, 0, duration=0.25)   # 너무 빠른 동작으로 drag 수행이 안될 때는 duration을 지정
# pyautogui.dragTo(1944, 703, duration=0.5)  # 절대 좌표 기준으로 x, y로 드래그

pyautogui.scroll(-800)  # 양수이면 위 방향으로, 음수이면 아래 방향으로 스크롤. (PC 마다 다를 수 있음)
