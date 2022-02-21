import pyautogui


def locate_inn():
    _inn_ = pyautogui.locateOnScreen(r'bot\rsc\inn.png', confidence=0.6)
    if _inn_ is not None:
        return _inn_
