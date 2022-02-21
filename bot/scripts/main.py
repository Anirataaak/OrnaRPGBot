import pyautogui
import time

from bot.scripts import locate, checks, mob

playerTier = 'tier4'


def heal_with_inn(_inn_):
    pyautogui.click(_inn_)
    time.sleep(1)
    pyautogui.click(933, 248)
    time.sleep(0.5)
    pyautogui.mouseDown(948, 458)
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(4)
    pyautogui.click(929, 975)


def heal_with_potions():
    time.sleep(0.5)
    pyautogui.click(1074, 968)
    pyautogui.mouseDown(1671, 371)
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.click(924, 982)
    time.sleep(0.5)


def heal():
    _inn_ = locate.locate_inn()
    if _inn_ is not None:
        heal_with_inn(_inn_)
    else:
        heal_with_potions()


def fight(mob, image):
    pyautogui.click(image)
    time.sleep(0.5)
    pyautogui.click(941, 641)
    time.sleep(0.5)
    _cannot_fight_ = pyautogui.locateOnScreen(r'bot\rsc\youMustWait.png', confidence=0.8)
    if _cannot_fight_ is not None:
        pyautogui.click(924, 982)
        time.sleep(0.5)
        mob.blocked = True
        _cannot_fight_ = None
    else:
        while True:
            pyautogui.click(317, 852)
            time.sleep(0.5)
            if checks.check_for_victory() == 'yes':
                pyautogui.click(947, 912)
                time.sleep(0.5)
                break
            elif checks.check_for_defeat() == 'yes':
                mob.blocked = True
                pyautogui.click(947, 912)
                heal()
                break


index = 0
mobIndex = 0
while True:
    if index == 4:
        heal()
        index = 0
    if mobIndex == 5:
        checks.set_mobs_unblocked()
        mobIndex = 0
    time.sleep(1)
    _continue_ = pyautogui.locateOnScreen(r'bot\rsc\continue.png', confidence=0.8)
    if _continue_ is not None:
        pyautogui.click(_continue_)
        time.sleep(1)
        _continue_ = None
    else:
        mob = checks.check_for_mobs()
        if mob is not None:
            index += 1
            _image_left_ = pyautogui.locateOnScreen(mob.return_left_path(), confidence=0.7)
            _image_right_ = pyautogui.locateOnScreen(mob.return_right_path(), confidence=0.7)
            if _image_left_ is not None:
                fight(mob, _image_left_)
                mobIndex += 1
                until = 5 - mobIndex
                if until != 0:
                    print('Fights until block resets ' + str(until))
            elif _image_right_ is not None:
                fight(mob, _image_right_)
                mobIndex += 1
                until = 5 - mobIndex
                if until != 0:
                    print('Fights until block resets ' + str(until))
