import win32api, win32con
from time import sleep as wait
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Discord Spam Caller By Zexor321")

print('''
██▄   ▄█    ▄▄▄▄▄   ▄█▄    ████▄ █▄▄▄▄ ██▄          ▄▄▄▄▄   █ ▄▄  ██   █▀▄▀█     ▄█▄    ██   █    █     ▄███▄   █▄▄▄▄ 
█  █  ██   █     ▀▄ █▀ ▀▄  █   █ █  ▄▀ █  █        █     ▀▄ █   █ █ █  █ █ █     █▀ ▀▄  █ █  █    █     █▀   ▀  █  ▄▀ 
█   █ ██ ▄  ▀▀▀▀▄   █   ▀  █   █ █▀▀▌  █   █     ▄  ▀▀▀▀▄   █▀▀▀  █▄▄█ █ ▄ █     █   ▀  █▄▄█ █    █     ██▄▄    █▀▀▌  
█  █  ▐█  ▀▄▄▄▄▀    █▄  ▄▀ ▀████ █  █  █  █       ▀▄▄▄▄▀    █     █  █ █   █     █▄  ▄▀ █  █ ███▄ ███▄  █▄   ▄▀ █  █  
███▀   ▐            ▀███▀          █   ███▀                  █       █    █      ▀███▀     █     ▀    ▀ ▀███▀     █   
                                  ▀                           ▀     █    ▀                █                      ▀    
By Zexor321 for Windows.
''')

wait(0.25)

print("Warning, you cannot stop the program until all the calls have been completed.")
missedcalls = int(input("\nHow many calls would you like to spam? -> "))

def callbutton(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)   

for _ in range(missedcalls):
    wait(0.2)
    callbutton(1540,45) # first possible call button location
    callbutton(1571,40) # second possible call button location.
    callbutton(1230,210) # hang up as fast as possible.
    print("Done! => Hope they mic up soon! ;)")