import pyautogui

# fw = pyautogui.getActiveWindow()  # 현재 활성화된 창 (VSCode)
# print(fw.title) # 창의 제목정보 
# print(fw.size)  # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

# for w in pyautogui.getWindowsWithTitle('제목 없음'):
#     print(w) # 모든 윈도우 가져오기

w = pyautogui.getAllWindows()
for i in w:
    print(len(w))
    print(i.title)

# print(w.title)

# w = pyautogui.getWindowsWithTitle('제목 없음')[0]
# print(w)
# if w.

w.close()  # pyautogui의 roadmap에 언급됨 
