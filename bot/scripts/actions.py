import pyautogui
import time

from bot.scripts import locate, mob, checks


def heal(fightCount, countToHeal):
    if fightCount % countToHeal == 0:
        _inn_ = locate.locateInn()
        if _inn_ is not None:
            print('Action: Healing with inn')
            healWithInn(_inn_)
        else:
            print('Action: Healing with potions')
            healWithPotions()


def healWithInn(_inn_):
    pyautogui.click(_inn_)
    time.sleep(1)
    pyautogui.click(933, 248)
    time.sleep(0.5)
    pyautogui.mouseDown(948, 458)
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(4)
    pyautogui.click(929, 975)


def healWithPotions():
    time.sleep(1)
    pyautogui.click(1074, 968)
    pyautogui.mouseDown(1671, 371)
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.click(924, 982)
    time.sleep(1)


def useTorch(fightCount, countToUseTorch):
    if fightCount % countToUseTorch == 0:
        pyautogui.click(1065, 961)
        time.sleep(0.5)
        pyautogui.mouseDown(1673, 731)
        pyautogui.moveTo(1665, 51)
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(0.5)
        _torch_ = pyautogui.locateOnScreen(r'bot\rsc\torch.png', confidence=0.8)
        pyautogui.click(_torch_)
        time.sleep(0.5)
        pyautogui.click(933, 974)


def unblockMobs(fightCount, countToUnlockBlockedMobs):
    print('Action: Unblocking Mobs')
    if fightCount % countToUnlockBlockedMobs == 0:
        for currentMob in mob.mobs:
            currentMob.blocked = False


def clickContinue(_continue_):
    pyautogui.click(_continue_)


def fight(mob, image):
    print(f'Action: Start fighting {mob.name}')
    pyautogui.click(image)
    time.sleep(1)
    battle = pyautogui.locateOnScreen(r'bot\rsc\battle.png', confidence=0.8)
    pyautogui.click(battle)
    time.sleep(0.5)
    _cannot_fight_ = pyautogui.locateOnScreen(r'bot\rsc\youMustWait.png', confidence=0.8)
    if _cannot_fight_ is not None:
        pyautogui.click(924, 982)
        time.sleep(0.5)
        mob.blocked = True
        _cannot_fight_ = None
    else:
        while True:
            if not mob.freeze:
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
            else:
                pyautogui.click(1500, 837)
                time.sleep(0.5)
                freeze = pyautogui.locateOnScreen(r'bot\rsc\freeze.png', confidence=0.8)
                pyautogui.click(freeze)
                if checks.check_for_victory() == 'yes':
                    pyautogui.click(947, 912)
                    time.sleep(0.5)
                    break
                elif checks.check_for_defeat() == 'yes':
                    mob.blocked = True
                    pyautogui.click(947, 912)
                    heal()
                    break