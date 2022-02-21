import pyautogui
from bot.scripts import mob


def check_for_mobs():
    for monster in mob.get_mob_list():
        print(monster)
        _image_ = pyautogui.locateOnScreen(monster, confidence=0.5)
        if _image_ is not None:
            print(monster)
            return _image_


def check_for_victory():
    _victory_screen_ = pyautogui.locateOnScreen(r'bot\rsc\victory.png', confidence=0.6)
    if _victory_screen_ is not None:
        return 'yes'
    else:
        return 'no'


def check_for_defeat():
    _defeat_screen_ = pyautogui.locateOnScreen(r'bot\rsc\defeat.png', confidence=0.6)
    if _defeat_screen_ is not None:
        return 'yes'
    else:
        return 'no'
