import pyautogui
import os

fileList = os.listdir(r'bot\rsc\mobs')
mobList = []

for file in fileList:
    if file.endswith('.png') or file.endswith('.PNG'):
        mobList.append(r'bot\rsc\mobs\\' + file)


    def check_for_mob():
        for mob in mobList:
            print(mob)
            _image_ = pyautogui.locateOnScreen(mob, confidence=0.6)
            if _image_ is not None:
                print(mob)
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
