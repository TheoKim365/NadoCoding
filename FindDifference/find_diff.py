import os, time, sys
import pyautogui
from PIL import ImageChops
import cv2

# 왼쪽 (원본) 이미지
# 시작 좌표 : 0, 217

# 오른쪽 (비교대상) 이미지
# 시작 좌표 : 1445, 217

# 이미지 크기
# width : 1435
# height : 1364 - 217 = 1147

width, height = 1435, 1147
y_pos = 217
x_sec = 1444

src = pyautogui.screenshot(region=(0, y_pos, width, height))
src.save('src.jpg')

dest = pyautogui.screenshot(region=(x_sec, y_pos, width, height))
dest.save('dest.jpg')

diff = ImageChops.difference(src, dest)
# diff = cv2.absdiff(src, dest)
diff.save('diff.jpg')

# diff.

# sys.exit()

while not os.path.exists('diff.jpg'):
    time.sleep(1)

# import cv2
src_img = cv2.imread('src.jpg')
dest_img = cv2.imread('dest.jpg')
diff_img = cv2.imread('diff.jpg')

# diff_img = cv2.absdiff(src, dest)
# diff_img.save('diff.png')


gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
# gray = cv2.cvtColor(diff_img, cv2.COLOR_RGB2GRAY)
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# binary = cv2.bitwise_not(binary)

contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# contours, _ = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)
for cnt in contours:
    # if cv2.contourArea(cnt) > 100:
    x, y, width, height = cv2.boundingRect(cnt)
    cv2.rectangle(src_img, (x, y), (x + width, y + height), COLOR, 2)
    cv2.rectangle(dest_img, (x, y), (x + width, y + height), COLOR, 2)
    cv2.rectangle(diff_img, (x, y), (x + width, y + height), COLOR, 2)

cv2.imshow('src', src_img)
cv2.imshow('dest', dest_img)
cv2.imshow('diff', diff_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
