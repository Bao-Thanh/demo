import pyautogui

image = "setting.png"
loc = pyautogui.locateOnScreen(image)
pyautogui.click(loc)
