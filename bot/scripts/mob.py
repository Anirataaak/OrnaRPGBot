def getMobsByTier(tier):
    mobList = []
    print(f'Initializing {tier} mobs')
    for mob in mobs:
        if mob.tier == tier:
            mobList.append(mob)
    print(f'Successful initialized {tier} mobs')
    return mobList


def get_mobs():
    mobList = []
    for mob in mobs:
        mobList.append(mob)
    return mobList


mobs: set
mobs = set()


class Mob:

    def __init__(self, name, tier):
        self.name = name
        self.tier = tier
        self.blocked = False
        self.freeze = False
        mobs.add(self)

    def return_left_path(self):
        return fr'bot\\rsc\\mobs\\{self.tier}\\{self.name}left.png'

    def return_right_path(self):
        return fr'bot\\rsc\\mobs\\{self.tier}\\{self.name}right.png'


tier1 = 'tier1'
tier2 = 'tier2'
tier3 = 'tier3'
tier4 = 'tier4'
tier5 = 'tier5'
tier6 = 'tier6'
tier7 = 'tier7'
tier8 = 'tier8'
tier9 = 'tier9'
tier10 = 'tier10'
tier11 = 'tier11'

# Tier 11

# Tier 10

# Tier 9

# Tier 8

# Tier 7
camazotz = Mob('camazotz', tier7)
greatOrcMarauder = Mob('greatOrcMarauder', tier7)
greatOrc = Mob('greatOrc', tier7)
highFomorianMage = Mob('highFomorianMage', tier7)
highFomorian = Mob('highFomorian', tier7)
lostPharaoh = Mob('lostPharaoh', tier7)
warg = Mob('warg', tier7)
darkElfRogue = Mob('darkElfRogue', tier7)
minotaur = Mob('minotaur', tier7)
orcLord = Mob('orcLord', tier7)
draconianLord = Mob('draconianLord', tier7)
twilightWisp = Mob('twilightWisp', tier7)
fallenWanderer = Mob('fallenWanderer', tier7)
redBasilisk = Mob('redBasilisk', tier7)

# Tier 6
highDraconianMage = Mob('highDraconianMage', tier6)
highDraconianWarrior = Mob('highDraconianWarrior', tier6)
greatWyvern = Mob('greatWyvern', tier6)
ancientDraugrMage = Mob('ancientDraugrMage', tier6)
ancientDraugr = Mob('ancientDraugr', tier6)
gargoyle = Mob('gargoyle', tier6)
basilisk = Mob('basilisk', tier6)
greatUshiOni = Mob('greatUshiOni', tier6)
frostTroll = Mob('frostTroll', tier6)
arcaneFlame = Mob('arcaneFlame', tier6).freeze = True

# Tier 5
greatTroll = Mob('greatTroll', tier5)
darkSlime = Mob('darkSlime', tier5)
carrionCrow = Mob('carrionCrow', tier5)
adamantineKnight = Mob('adamantineKnight', tier5)
smallDragon = Mob('smallDragon', tier5)
darkestDemon = Mob('darkestDemon', tier5)
midnightImp = Mob('midnightImp', tier5)
orcMarauder = Mob('orcMarauder', tier5)
greaterCyclops = Mob('greaterCyclops', tier5)
harpy = Mob('harpy', tier5)
orgeBrute = Mob('orgeBrute', tier5)
seer = Mob('seer', tier5)
ushiOni = Mob('ushiOni', tier5)

# Tier 4
darkWidow = Mob('darkWidow', tier4)
fomorianMage = Mob('fomorianMage', tier4)
fomorianWarrior = Mob('fomorianWarrior', tier4)
orcBrute = Mob('orcBrute', tier4)
magmaGolem = Mob('magmaGolem', tier4)
ghost = Mob('ghost', tier4)
drake = Mob('drake', tier4)
yokai = Mob('yokai', tier4)
rottenSlime = Mob('rottenSlime', tier4)
cobra = Mob('cobra', tier4)
darkElf = Mob('darkElf', tier4)
fairy = Mob('fairy', tier4)

# Tier 3
vileRat = Mob('vileRat', tier3)
draugrMage = Mob('draugrMage', tier3)
ogre = Mob('ogre', tier3)
blueFlame = Mob('blueFlame', tier3)
greaterDemon = Mob('greaterDemon', tier3)
greyWolfman = Mob('greyWolfman', tier3)
lesserSluagh = Mob('lesserSluagh', tier3)
hellhound = Mob('hellhound', tier3)
jinn = Mob('jinn', tier3)
zu = Mob('zu', tier3)
draconianAcolyte = Mob('draconianAcolyte', tier3)
hobgoblinMage = Mob('hobgoblinMage', tier3)
golem = Mob('golem', tier3)
hobgoblin = Mob('hobgoblin', tier3)
greaterSnake = Mob('greaterSnake', tier3)
mithrilArmor = Mob('mithrilArmor', tier3)
draconianRogue = Mob('draconianRogue', tier3)
buried = Mob('buried', tier3)
fallenKnight = Mob('fallenKnight', tier3)
skeletonWarrior = Mob('skeletonWarrior', tier3)
vampire = Mob('vampire', tier3)
fallenWitch = Mob('fallenWitch', tier3)

# Tier 2
livingArmor = Mob('livingArmor', tier2)
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
blackWidow = Mob('blackWidow', tier2)
undead = Mob('undead', tier2)
wolf = Mob('wolf', tier2)
wolfman = Mob('wolfman', tier2)
goblin = Mob('goblin', tier2)
flame = Mob('flame', tier2).freeze = True
evilEye = Mob('evilEye', tier2)
goblinWarrior = Mob('goblinWarrior', tier2)
feralHorse = Mob('feralHorse', tier2)
draconianMage = Mob('draconianMage', tier2)

# Tier 1
blueSlime = Mob('blueSlime', tier1)
snake = Mob('snake', tier1)
