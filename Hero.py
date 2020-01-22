import random
class Hero(object):
    RACELIST = ["Human", "Elf", "Dwarf","Dog"]
    CLASSLIST = ["Warrior", "Mage", "Hunter","Dog"]

    def __init__(self):
        self.Alive = True
        self.level = 1
        self.race = self.pickRace()
        self.playerClass = self.pickClass()
        self.name = input("Enter your name here.")
       #leveling up
        self.xp = 0
        self.levelUp = 90 + (self.level * 10)
       #Main Health set up
        self.healthMod = 10
        self.maxHealth = self.level * self.healthMod
        self.healthAct = self.maxHealth
       #Main Mana Set up
        self.manaMod = 10
        self.maxMana = self.level * self.manaMod
        self.manaAct = self.maxMana
       #base stats
        self.deff = 0
        self.atk = 0
        self.luck = 0
        self.stamina = 0
        self.iq = 0
        self.agi = 0
       # setting the base values on the class
        self.setMods()

    def setMods(self):

        ### Class settings

        if self.playerClass == "Warrior":
            self.deff = random.randint(5,20)
            self.atk = random.randint(5,15)
            self.luck = random.randint(1,5)
            self.stamina = random.randint(15,20)
            self.iq = 1
            self.agi = random.randint(1,5)
            self.maxMana = 0

        if self.playerClass == "Mage":
            self.deff = random.randint(5, 13)
            self.atk = random.randint(10, 20)
            self.luck = random.randint(4, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint (5,20)
            self.agi = random.randint(1, 5)
            self.manaMod = random.randint(15,20)

        if self.playerClass == "Hunter":
            self.deff = random.randint(5, 15)
            self.atk = random.randint(10, 18)
            self.luck = random.randint(7, 13)
            self.stamina = random.randint(7, 14)
            self.iq = random.randint(5, 12)
            self.agi = random.randint(7, 17)

        if self.playerClass == "Dog":
            self.deff = random.randint(1, 100)
            self.atk = random.randint(1, 100)
            self.luck = random.randint(1, 100)
            self.stamina = random.randint(1, 100)
            self.iq = random.randint(1, 100)
            self.agi = random.randint(1, 100)

        ### Race settings

        if self.race == "Elf":
            self.stamina -= 2
            self.iq += 2

        if self.race == "Dwarf":
            self.stamina += 2
            self.iq -= 2

        if self.race == "Dog":
            self.deff += random.randint(1, 100)
            self.atk += random.randint(1, 100)
            self.luck += random.randint(1, 100)
            self.stamina += random.randint(1, 100)
            self.iq += random.randint(1, 100)
            self.agi += random.randint(1, 100)
            self.healthAct+= random.randint(1, 100)



    def __str__(self):
        rep = str.format("""
        Name = {}
        Level = {}
        Race = {}
        Class = {}
        Health = {}
        Xp = {}
        Mana = {}
        Defence = {}
        Attack = {}
        Luck = {}
        Stamina = {}
        Intelect = {}
        Agility = {}
        """,self.name, self.level, self.race, self.playerClass, self.healthAct, self.xp, self.manaAct, self.deff,
            self.atk, self.luck, self.stamina, self.iq, self.agi)
        return rep


    def pickRace(self):
        while True:
            try:
                print(Hero.RACELIST[0:3])
                x = input("Pick a your race")
                if x in Hero.RACELIST:
                    return x
            except:
                print("Not a valid option")

    def pickClass(self):
        while True:
            try:
                print(Hero.CLASSLIST[0:3])
                x = input("Pick a your class")
                if x in Hero.CLASSLIST:
                    return x
            except:
                print("Not a valid option")





test = Hero()
print(test)