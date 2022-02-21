import pyautogui
import time

from bot.scripts import locate, checks


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


index = 0
while True:
    if index == 2:
        heal()
        index = 0
    _continue_ = pyautogui.locateOnScreen(r'bot\rsc\continue.png', confidence=0.8)
    if _continue_ is not None:
        pyautogui.click(_continue_)
        time.sleep(1)
    else:
        _image_ = checks.check_for_mob()
        if _image_ is not None:
            index += 1
            pyautogui.click(_image_)
            time.sleep(0.5)
            pyautogui.click(941, 641)
            time.sleep(0.5)
            _cannot_fight_ = pyautogui.locateOnScreen(r'bot\rsc\youMustWait.png', confidence=0.8)
            if _cannot_fight_ is not None:
                pyautogui.click(924, 982)
                time.sleep(0.5)
            else:
                while True:
                    pyautogui.click(317, 852)
                    time.sleep(0.5)
                    if checks.check_for_victory() == 'yes':
                        pyautogui.click(947, 912)
                        time.sleep(0.5)
                        break
                    elif checks.check_for_defeat() == 'yes':
                        pyautogui.click(947, 912)
                        heal()
                        break
