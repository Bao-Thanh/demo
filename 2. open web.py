import pyautogui
import webbrowser
import time

def open_browser_and_search():
    webbrowser.open('https://www.google.com')
    
    time.sleep(5)
    
    pyautogui.write('Python')
    pyautogui.press('enter')

if __name__ == "__main__":
    open_browser_and_search()
