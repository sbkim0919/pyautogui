import pyautogui

# 원하는 이미지를 스크린샷을 찍어 해당 영역을 찾아 클릭한다.

#  좌표 확인
# print(pyautogui.position())

# 스크린샷을 찍어 이미지 저장
pyautogui.screenshot("1.png", region=(2163, 785, 70, 45))

# 이미지 센터값 추출
num1 = pyautogui.locateCenterOnScreen('1.png')
# 리턴된 센터값으로 마우스를 이동 후 클릭
pyautogui.click(num1)