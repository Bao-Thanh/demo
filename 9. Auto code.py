import pyautogui
import time

def open_eclipse():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('eclipse')
    time.sleep(1)
    pyautogui.press('enter')
    
def create_new_file():
    file = "file.png"
    file_loc = pyautogui.locateOnScreen(file, confidence=0.8)
    if file_loc is not None:
        print(f"Found file box at: {file_loc}")
        pyautogui.click(file_loc)
    else:
        print("File box not found!")
        pyautogui.screenshot('debug_file_not_found.png')
        return
    time.sleep(2)
    pyautogui.hotkey('alt', 'shift', 'n')
    time.sleep(2)
    project = "project.png"
    project_loc = pyautogui.locateOnScreen(project, confidence=0.8)
    if file_loc is not None:
        print(f"Found project box at: {project_loc}")
        pyautogui.click(project_loc)
    else:
        print("project box not found!")
        pyautogui.screenshot('debug_project_not_found.png')
        return
    time.sleep(2)
    pyautogui.write('test')
    pyautogui.press('enter')

def create_new_class():
    test = "test.png"
    test_loc = pyautogui.locateOnScreen(test, confidence=0.8)
    if test_loc is not None:
        print(f"Found test box at: {test_loc}")
        pyautogui.click(test_loc)
    else:
        print("Test box not found!")
        pyautogui.screenshot('debug_test_not_found.png')
        return
    time.sleep(3)
    pyautogui.rightClick()
    time.sleep(2)
    new = "new.png"
    new_loc = pyautogui.locateOnScreen(new, confidence=0.8)
    if test_loc is not None:
        print(f"Found test box at: {new_loc}")
        pyautogui.click(new_loc)
    else:
        print("New box not found!")
        pyautogui.screenshot('debug_new_not_found.png')
        return
    time.sleep(3)
    new = "new.png"
    new_loc = pyautogui.locateOnScreen(new, confidence=0.8)
    if new_loc is not None:
        print(f"Found test box at: {new_loc}")
        pyautogui.click(new_loc)
    else:
        print("New box not found!")
        pyautogui.screenshot('debug_new_not_found.png')
        return
    time.sleep(3)
    _class = "class.png"
    class_loc = pyautogui.locateOnScreen(_class, confidence=0.8)
    if new_loc is not None:
        print(f"Found class box at: {class_loc}")
        pyautogui.click(class_loc)
    else:
        print("Class box not found!")
        pyautogui.screenshot('debug_class_not_found.png')
        return;
    time.sleep(3)
    pyautogui.write('demo', interval=0.1)
    pyautogui.press('enter')
    
def code():
    for _ in range(3):
        pyautogui.press('down')
    time.sleep(3)
    code = """
        public static void main(String[] args) {
            System.out.println("This is controlled automatically!!!");
    """
    pyautogui.typewrite(code.strip(), interval=0.1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'i')
    pyautogui.hotkey('ctrl', 's')
    
def run():
    run = "run.png"
    run_loc = pyautogui.locateOnScreen(run, confidence=0.8)
    if run_loc is not None:
        print(f"Found run box at: {run_loc}")
        pyautogui.click(run_loc)
    else:
        print("Run box not found!")
        pyautogui.screenshot('debug_run_not_found.png')
        return
    time.sleep(3)
    pyautogui.screenshot('result.png')

open_eclipse()
time.sleep(40)
create_new_file()
time.sleep(3)
create_new_class()
time.sleep(3)
code()
time.sleep(10)
run()


