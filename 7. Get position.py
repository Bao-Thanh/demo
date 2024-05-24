import pyautogui
import time

time.sleep(5)

x, y = pyautogui.position()

print(f"Tọa độ hiện tại của con trỏ chuột là: ({x}, {y})")
