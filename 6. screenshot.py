import pyautogui
import webbrowser
import time


def open_browser_and_search():
    webbrowser.open('https://www.youtube.com/')

    time.sleep(5)

    searchBar = "searchBar.png"
    searchBar_loc = pyautogui.locateOnScreen(searchBar, confidence=0.8)
    if searchBar_loc is not None:
        print(f"Found YouTube button at: {searchBar_loc}")
        pyautogui.click(searchBar_loc)
        pyautogui.typewrite("Deep Learning", interval=0.1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.screenshot('Deep learning on Youtube.png')

    else:
        print("SearchBar_loc button not found!")
        pyautogui.screenshot('debug_youtube_not_found.png')
        return


if __name__ == "__main__":
    open_browser_and_search()
