import time

import actions
import locate
import checks

#Settings

countToHeal = 5
countToUnlockBlockedMobs = 8
countToUseTorch = 200
playerTier = 3

#CountVariables

fightCount = 0
currentTier = f'tier{playerTier}'

#Bot-Loop

while True:
    actions.heal(fightCount, countToHeal)
    time.sleep(1)
    actions.unblockMobs(fightCount, countToUnlockBlockedMobs)
    time.sleep(1)
    actions.useTorch(fightCount, countToUseTorch)
    time.sleep(1)
    continueButton = locate.locateContinue()
    if continueButton is not None:
        actions.clickContinue(continueButton)
        time.sleep(1)
    else:
        mob, currentTier = checks.checkForMobs(currentTier, playerTier)
        if mob is not None:
            mobImage = locate.locateMob(mob)
            if mobImage is not None:
                actions.fight(mob, mobImage)
                fightCount += 1
