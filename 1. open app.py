import pyautogui
import time

def open_calculator():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('calculator')
    time.sleep(1)
    pyautogui.press('enter')

def perform_calculations():
    time.sleep(2)
    pyautogui.write('123')
    pyautogui.press('+')
    pyautogui.write('456')
    pyautogui.press('enter')

if __name__ == "__main__":
    open_calculator()
    perform_calculations()
