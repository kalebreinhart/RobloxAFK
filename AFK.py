# Just Jump - A Roblox AFK tool
# 5-8-23 KJR

import time
import win32gui
import re
import mousekey
import random

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

def AFK():
    w = WindowMgr()
    w.find_window_wildcard(".*Roblox.*") # Set the window name to find Roblox
    w.set_foreground() # Set window focus to found window

    mousekey.Press(32, delay=1) # Press the space bar

while True:
    AFK()  
    time.sleep(random.randint(100, 200))  # Rndom time between 100 and 200 secs
