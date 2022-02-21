def get_all_tier1():
    mobList1 = []
    for mob in mobs:
        if mob.tier == tier1:
            mobList1.append(mob)
    return mobList1


def get_all_tier2():
    mobList2 = []
    for mob in mobs:
        if mob.tier == tier2:
            mobList2.append(mob)
    return mobList2


def get_all_tier3():
    mobList3 = []
    for mob in mobs:
        if mob.tier == tier3:
            mobList3.append(mob)
    return mobList3


def get_all_tier4():
    mobList4 = []
    for mob in mobs:
        if mob.tier == tier4:
            mobList4.append(mob)
    return mobList4


def get_mobs():
    mobList = []
    for mob1 in get_all_tier4():
        mobList.append(mob1)
    for mob2 in get_all_tier3():
        mobList.append(mob2)
    for mob3 in get_all_tier2():
        mobList.append(mob3)
    for mob4 in get_all_tier1():
        mobList.append(mob4)
    return mobList


def get_mob_list():
    mobList = []
    for mob in get_mobs():
        mobList.append(mob.return_right_path())
        mobList.append(mob.return_left_path())
    return mobList


mobs: set
mobs = set()


class Mob:

    def __init__(self, name, tier):
        self.name = name
        self.tier = tier
        self.blocked = False
        mobs.add(self)

    def return_left_path(self):
        return r'bot\\rsc\\mobs\\' + self.tier + r'\\' + self.name + r'left.png'

    def return_right_path(self):
        return r'bot\\rsc\\mobs\\' + self.tier + r'\\' + self.name + r'right.png'


tier1 = 'tier1'
tier2 = 'tier2'
tier3 = 'tier3'
tier4 = 'tier4'

#Tier 4
buried = Mob('buried', tier4)

#Tier 3
vileRat = Mob('vileRat', tier3)
draugrMage = Mob('draugrMage', tier3)
ogre = Mob('ogre', tier3)
blueFlame = Mob('blueFlame', tier3)
greaterDemon = Mob('greaterDemon', tier3)
greyWolfman = Mob('greyWolfman', tier3)
lesserSluagh = Mob('lesserSluagh', tier3)

#Tier 2
bandit = Mob('bandit', tier2)
bat = Mob('bat', tier2)
brownSpider = Mob('brownSpider', tier2)
crow = Mob('crow', tier2)
demon = Mob('demon', tier2)
fallenMage = Mob('fallenMage', tier2)
fallenThief = Mob('fallenThief', tier2)
fallenWarrior = Mob('fallenWarrior', tier2)
ghost = Mob('ghost', tier2)
greenSlime = Mob('greenSlime', tier2)
hawk = Mob('hawk', tier2)
rat = Mob('rat', tier2)
redSlime = Mob('redSlime', tier2)
skeleton = Mob('skeleton', tier2)
slime = Mob('slime', tier2)
spider = Mob('spider', tier2)
undead = Mob('undead', tier2)
wolf = Mob('wolf', tier2)
wolfman = Mob('wolfman', tier2)

#Tier 1
blueSlime = Mob('blueSlime', tier1)
