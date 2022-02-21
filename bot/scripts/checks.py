import pyautogui
from bot.scripts import mob as mobs


def set_mobs_unblocked():
    for mob in mobs.get_mobs():
        mob.blocked = False


last_mob = mobs.Mob


def check_for_mobs():
    for mob in mobs.get_mobs():
        if not mob.blocked:
            print('Searching for Mob: ' + mob.name)
            if mob.name == 'twilightWisp':
                _image_right_ = pyautogui.locateOnScreen(mob.return_right_path(), confidence=0.8)
                _image_left_ = pyautogui.locateOnScreen(mob.return_left_path(), confidence=0.8)
            else:
                _image_right_ = pyautogui.locateOnScreen(mob.return_right_path(), confidence=0.7)
                _image_left_ = pyautogui.locateOnScreen(mob.return_left_path(), confidence=0.7)
            if _image_right_ is not None:
                print('Found Mob: ' + mob.name)
                return mob
            elif _image_left_ is not None:
                print('Found Mob: ' + mob.name)
                _last_mob_ = mob
                return mob
        else:
            print('Blocked Mob: ' + mob.name)


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
