import pyautogui


def locateInn():
    _inn_ = pyautogui.locateOnScreen(r'bot\rsc\inn.png', confidence=0.6)
    if _inn_ is not None:
        return _inn_


def locateContinue():
    _continue_ = pyautogui.locateOnScreen(r'bot\rsc\continue.png', confidence=0.8)
    if _continue_ is not None:
        return _continue_


def locateMob(mob):
    if mob.name == 'twilightWisp' or mob.name == 'smallDragon':
        imageLeft = pyautogui.locateOnScreen(mob.return_left_path(), confidence=0.8)
        imageRight = pyautogui.locateOnScreen(mob.return_right_path(), confidence=0.8)
    else:
        imageLeft = pyautogui.locateOnScreen(mob.return_left_path(), confidence=0.8)
        imageRight = pyautogui.locateOnScreen(mob.return_right_path(), confidence=0.8)

    if imageLeft is not None:
        return imageLeft
    elif imageRight is not None:
        return imageRight
