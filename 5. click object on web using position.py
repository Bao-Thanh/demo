import pyautogui
import webbrowser
import time

def open_browser_and_search():
    webbrowser.open('https://maps.google.com/')
    
    time.sleep(8)
    pyautogui.typewrite("TMA lab 4", interval=0.1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(334, 490)
    pyautogui.click()

if __name__ == "__main__":
    open_browser_and_search()
