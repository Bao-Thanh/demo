import pyautogui
import webbrowser
import time

def open_browser_and_search():
    webbrowser.open('https://www.google.com')
    time.sleep(5)
    
    search = "search.png"
    search_loc = pyautogui.locateOnScreen(search, confidence=0.8)
    if search_loc is not None:
        print(f"Found search box at: {search_loc}")
        pyautogui.click(search_loc)
    else:
        print("Search box not found!")
        pyautogui.screenshot('debug_search_not_found.png')
        return
    
    time.sleep(5)
    
    youtube = "youtube.png"
    youtube_loc = pyautogui.locateOnScreen(youtube, confidence=0.8)
    if youtube_loc is not None:
        print(f"Found YouTube button at: {youtube_loc}")
        pyautogui.click(youtube_loc)
    else:
        print("YouTube button not found!")
        pyautogui.screenshot('debug_youtube_not_found.png')
        return

    time.sleep(5)
    
    searchBar = "searchBar.png"
    searchBar_loc = pyautogui.locateOnScreen(searchBar, confidence=0.8)
    if searchBar_loc is not None:
        print(f"Found YouTube button at: {searchBar_loc}")
        pyautogui.click(searchBar_loc)
        time.sleep(3)
        pyautogui.write('Python')
        pyautogui.press('enter')
    else:
        print("SearchBar_loc button not found!")
        pyautogui.screenshot('debug_youtube_not_found.png')
        return
    time.sleep(3)
    pyautogui.moveTo(952, 440)
    for _ in range(10):
        pyautogui.scroll(-500)
        time.sleep(1)
    
if __name__ == "__main__":
    open_browser_and_search()
