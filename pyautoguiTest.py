import pyautogui
import time

# 마우스 위치 확인
# pyautogui.position()

# pyautogui.moveTo 마우스 움직이기
# x 좌표, y좌료, 지연 시간)
pyautogui.moveTo(1863, 48)

# pyautogui.click()
# clicks=2 두번 클릭 interval=2 2초 후 클릭
pyautogui.doubleClick()
# pyautogui.click(clicks=2, interval=2)

time.sleep(1)

# 열자마자 글을 작성하면 글이 써지지 않느다. 
# 메모장이 열리는 시간을 주고 글을 작성해야한다.
# pyautogui.typewrite("Hello")
pyautogui.typewrite(['a', 'b', 'c', 'enter'])
pyautogui.typewrite("Hello")