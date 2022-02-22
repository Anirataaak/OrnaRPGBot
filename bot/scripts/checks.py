import pyautogui
from bot.scripts import mob as mobs


def set_mobs_unblocked():
    for mob in mobs.mobs:
        mob.blocked = False


def searchForMobImage(mobList):
    for mob in mobList:
        if not mob.blocked:
            print('Searching for Mob: ' + mob.name)
            if mob.name == 'twilightWisp' or mob.name == 'smallDragon':
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


def checkForMobs(tier, playerTier):
    currentTier = tier
    while True:
        if currentTier == mobs.tier7:
            image = searchForMobImage(mobs.getMobsByTier(mobs.tier7))
            if image is not None:
                return image, mobs.tier7
            else:
                currentTier = mobs.tier6
        if currentTier == mobs.tier6:
            image = searchForMobImage(mobs.getMobsByTier(mobs.tier6))
            if image is not None:
                return image, mobs.tier6
            else:
                currentTier = mobs.tier5
        if currentTier == mobs.tier5:
            image = searchForMobImage(mobs.getMobsByTier(mobs.tier5))
            if image is not None:
                return image, mobs.tier5
            else:
                currentTier = mobs.tier4
        if currentTier == mobs.tier4:
            image = searchForMobImage(mobs.getMobsByTier(mobs.tier4))
            if image is not None:
                return image, mobs.tier4
            else:
                currentTier = mobs.tier3
        if currentTier == mobs.tier3:
            image = searchForMobImage(mobs.getMobsByTier(mobs.tier3))
            if image is not None:
                return image, mobs.tier3
            else:
                currentTier = mobs.tier2
        if currentTier == mobs.tier2:
            image = searchForMobImage(mobs.getMobsByTier(mobs.tier2))
            if image is not None:
                return image, mobs.tier2
            else:
                currentTier = mobs.tier1
        if currentTier == mobs.tier1:
            image = searchForMobImage(mobs.getMobsByTier(mobs.tier1))
            if image is not None:
                return image, mobs.tier1
            else:
                currentTier = f'tier{playerTier}'


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
