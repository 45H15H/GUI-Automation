import pyautogui
import time
import keyboard
import win32api, win32con

def click(x,y):
    '''
    click function to click at the (x, y) coordinates
    '''
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


'''
tile coordinates:
(318, 900)
(448, 900)
(570, 900)
(680, 900)

'''
while keyboard.is_pressed('q') == False: # condition for keyboard interrupt
    if pyautogui.pixel(318, 900) [0] == 0:
        click(318, 900)
    if pyautogui.pixel(448, 900) [0] == 0:
        click(448, 900)
    if pyautogui.pixel(570, 900) [0] == 0:
        click(570, 900)
    if pyautogui.pixel(680, 900) [0] == 0:
        click(680, 900)





