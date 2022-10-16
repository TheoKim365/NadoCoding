import pyautogui
# 스크린 샷을 찍기
# img = pyautogui.screenshot()
# img.save('screenshot.png')  # 파일로 저장 

# pyautogui.mouseInfo()
# 48,32 67,164,237 #43A4ED

pixel = pyautogui.pixel(48, 32)
print(pixel)

# print(pyautogui.pixelMatchesColor(48, 32, (67, 164, 237)))
# print(pyautogui.pixelMatchesColor(48, 32, pixel))
print(pyautogui.pixelMatchesColor(48, 32, (67, 164, 238)))

