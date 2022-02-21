import os

import pyautogui
import time

import test

fileList = os.listdir(r'scripts\rsc\mobs')
mobList = []

for file in fileList:
    if file.endswith('.png') or file.endswith('.PNG'):
        mobList.append(r'scripts\rsc\mobs\\' + file)


def check_for_mob():
    for mob in mobList:
        print(mob)
        _image_ = pyautogui.locateOnScreen(mob, confidence=0.6)
        if _image_ is not None:
            print(mob)
            return _image_


def check_for_victory():
    _victory_screen_ = pyautogui.locateOnScreen(r'scripts\rsc\victory.png', confidence=0.6)
    if _victory_screen_ is not None:
        return 'yes'
    else:
        return 'no'


def check_for_defeat():
    _defeat_screen_ = pyautogui.locateOnScreen(r'scripts\rsc\defeat.png', confidence=0.6)
    if _defeat_screen_ is not None:
        return 'yes'
    else:
        return 'no'


def locate_inn():
    _inn_ = pyautogui.locateOnScreen(r'scripts\rsc\inn.png', confidence=0.6)
    if _inn_ is not None:
        return _inn_


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
    _inn_ = locate_inn()
    if _inn_ is not None:
        heal_with_inn(_inn_)
    else:
        heal_with_potions()


index = 0
while True:
    index += 1
    if index is 3:
        heal()
        index = 0
    _continue_ = pyautogui.locateOnScreen(r'scripts\rsc\continue.png', confidence=0.8)
    if _continue_ is not None:
        pyautogui.click(_continue_)
        time.sleep(1)
    else:
        _image_ = check_for_mob()
        if _image_ is not None:
            pyautogui.click(_image_)
            time.sleep(0.5)
            pyautogui.click(941, 641)
            time.sleep(0.5)
            _cannot_fight_ = pyautogui.locateOnScreen(r'scripts\rsc\youMustWait.png', confidence=0.8)
            if _cannot_fight_ is not None:
                pyautogui.click(924, 982)
                time.sleep(0.5)
            else:
                while True:
                    pyautogui.click(317, 852)
                    time.sleep(0.5)
                    if check_for_victory() == 'yes':
                        pyautogui.click(947, 912)
                        time.sleep(0.5)
                        break
                    elif check_for_defeat() == 'yes':
                        pyautogui.click(947, 912)
                        heal()
                        break
