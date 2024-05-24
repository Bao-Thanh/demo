import pyautogui
import time

time.sleep(2)

pyautogui.hotkey('win', 'shift', 's')

time.sleep(2)

start_x, start_y = 100, 100
pyautogui.moveTo(start_x, start_y)

pyautogui.mouseDown()

end_x, end_y = 500, 400
pyautogui.moveTo(end_x, end_y, duration=1)

pyautogui.mouseUp()

time.sleep(2)
