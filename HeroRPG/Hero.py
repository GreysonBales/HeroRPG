from HeroRPG.Armour import *
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
        self.xpToLevelUp = 90 + (self.level * 10)
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
       #Attack list
        self.atklist = []


       #the set up of inventories
        self.inventory = []
        self.maxinv = 10
        self.popInv()
       #Equipment
        self.helmeq = []
        self.chesteq = []
        self.legeq = []
        self.gloveeq = []
        self.bootseq = []
        self.righthandwep = []
        self.lefthandwep = []

    def popInv(self):
        #gives random amount of pots
        x = random.randint(0,4)
        for i in range(x):
            y = random.randint(0,1)
            if y == 1:
                self.addToInv("Health Potion")
            else:
                self.addToInv("Mana Potion")
        helm = Helm()
        chest = Chest()
        legs = Legs()
        boots = Boots()
        gloves = Gloves()
        x = random.randint(0,5)
        if x == 0:
            weapon = Sword()
        elif x == 1:
            weapon = Dagger()
        elif x == 2:
            weapon = LongBow()
        elif x == 3:
            weapon = Lightsaber()
        else:
            weapon = RustySpoon()
        self.addToInv(helm)
        self.addToInv(chest)
        self.addToInv(legs)
        self.addToInv(boots)
        self.addToInv(gloves)
        self.addToInv(weapon)

    def addToInv(self,item):
        if len(self.inventory) < 10:
            self.inventory.append(item)
        else:
            print("Not enough inventory spaces, upgrade bag or drop items.")
            return

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
            self.atklist = ["Normal","Medium","Strong"]

        if self.playerClass == "Mage":
            self.deff = random.randint(5, 13)
            self.atk = random.randint(10, 20)
            self.luck = random.randint(4, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint (5,20)
            self.agi = random.randint(1, 5)
            self.manaMod = random.randint(15,20)
            self.atklist = ["Normal", "Fireball", "Arcane Blast"]

        if self.playerClass == "Hunter":
            self.deff = random.randint(5, 15)
            self.atk = random.randint(10, 18)
            self.luck = random.randint(7, 13)
            self.stamina = random.randint(7, 14)
            self.iq = random.randint(5, 12)
            self.agi = random.randint(7, 17)
            self.atklist = ["normal", "aimed shot","volly"]

        if self.playerClass == "Dog":
            self.deff = random.randint(1, 100)
            self.atk = random.randint(1, 100)
            self.luck = random.randint(1, 100)
            self.stamina = random.randint(1, 100)
            self.iq = random.randint(1, 100)
            self.agi = random.randint(1, 100)
            self.atklist = ["Normal","Good Boy", "Bark"]

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
            h = random.randint(10,101)
            if h == 101:
                self.healthAct = 1000
            else:
                self.healthAct = h

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
                x = input("Pick a your race : ")
                if x in Hero.RACELIST:
                    return x
            except:
                print("Not a valid option")

    def pickClass(self):
        while True:
            try:
                print(Hero.CLASSLIST[0:3])
                x = input("Pick a your class : ")
                if x in Hero.CLASSLIST:
                    return x
            except:
                print("Not a valid option")

    def die(self):
        if self.healthAct <= 0 :
            self.unequipAll()
            dropXp = 20 * self.level
            dropItem = random.choice(self.inventory)
            return dropItem, dropXp

        else:
            return "", ""

    def levelUp(self):
        if self.xp >= self.xpToLevelUp:
            print("ding level up")
            remxp = self.xp - self.xpToLevelUp
            self.level += 1
            self.xpToLevelUp = 90 + (self.level *10)
            self.xp = remxp

            self.healthMod = self.healthMod + self.level
            self.maxHealth = self.level * self.healthMod
            self.healthAct = self.maxHealth
            if self.playerClass != "Warrior":
                self.manaMod = self.manaMod + self.level
                self.maxMana = self.level * self.manaMod
                self.manaMod = self.maxMana
            self.levelMod()

    def levelMod(self):
        points = random.randint(1, self.level +1)
        while points > 0 :
            print("""
                Luck : {}
                Stamina: {}
                Intelect: {}
                Agility: {}""".format(self.luck,self.stamina,self.iq,self.agi))
            x = input("What Stat would you like to add points to?")
            y = int(input("You have " + str(points) + " points to spend how many would you like to spend in " + x))
            if x == "Stamina":
                self.stamina += y
                points -= y
            elif x == "Luck":
                self.luck += y
                points -= y
            elif x == "Intelect":
                self.iq += y
                points -= y
            elif x == "Agility":
                self.agi += y
                points -= y
            else:
                print("Not an option")

        else:
            return

    def collectXp(self,droppedXp):
        print("you picked up " + str(droppedXp) + " xp")
        self.xp += int(droppedXp)
        self.levelUp()

    def equipGloves(self):
        for i in self.inventory:
            x = type(i)
            if "Gloves" in str(x):
                if len(self.gloveeq) < 1 :
                    print("You equipped a set a gloves")
                    print(i)
                    self.gloveeq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.gloveeq[0].armour
                    self.luck += self.gloveeq[0].luck
                    self.stamina += self.gloveeq[0].stamina
                    self.iq += self.gloveeq[0].iq
                    self.agi += self.gloveeq[0].agi
                else:
                    print("You are wearing gloves already")
                    print(self.gloveeq[0])
                    print("Would you like to replave them with...")
                    print(i)
                    while True:
                        x = input("Yes or No")
                        if x == "Yes" or "yes":
                            print("You've replaced your gloves")
                            self.deff -= self.gloveeq[0].armour
                            self.luck -= self.gloveeq[0].luck
                            self.stamina -= self.gloveeq[0].stamina
                            self.iq -= self.gloveeq[0].iq
                            self.agi -=self.gloveeq[0].agi
                            self.gloveeq.remove(self.gloveeq[0])
                            self.gloveeq.append(i)
                            self.deff += self.gloveeq[0].armour
                            self.luck += self.gloveeq[0].luck
                            self.stamina += self.gloveeq[0].stamina
                            self.iq += self.gloveeq[0].iq
                            self.agi += self.gloveeq[0].agi
                            break
                        elif x == "No" or "no":
                            self.inventory.remove(i)
                            break

    def equipHelm(self):
        for i in self.inventory:
            x = type(i)
            if "Helm" in str(x):
                if len(self.helmeq) < 1:
                    print("You equipped a set a.helms")
                    print(i)
                    self.helmeq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.helmeq[0].armour
                    self.luck += self.helmeq[0].luck
                    self.stamina += self.helmeq[0].stamina
                    self.iq += self.helmeq[0].iq
                    self.agi += self.helmeq[0].agi
                else:
                    print("You are wearing.helms already")
                    print(self.helmeq[0])
                    print("Would you like to replave them with...")
                    print(i)
                    while True:
                        x = input("Yes or No")
                        if x == "Yes" or "yes":
                            print("You've replaced your.helms")
                            self.deff -= self.helmeq[0].armour
                            self.luck -= self.helmeq[0].luck
                            self.stamina -= self.helmeq[0].stamina
                            self.iq -= self.helmeq[0].iq
                            self.agi -= self.helmeq[0].agi
                            self.helmeq.remove(self.helmeq[0])
                            self.helmeq.append(i)
                            self.deff += self.helmeq[0].armour
                            self.luck += self.helmeq[0].luck
                            self.stamina += self.helmeq[0].stamina
                            self.iq += self.helmeq[0].iq
                            self.agi += self.helmeq[0].agi
                            break
                        elif x == "No" or "no":
                            self.inventory.remove(i)
                            break

    def equipChest(self):
        for i in self.inventory:
            x = type(i)
            if "Chest" in str(x):
                if len(self.chesteq) < 1:
                    print("You equipped a set a.chests")
                    print(i)
                    self.chesteq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.chesteq[0].armour
                    self.luck += self.chesteq[0].luck
                    self.stamina += self.chesteq[0].stamina
                    self.iq += self.chesteq[0].iq
                    self.agi += self.chesteq[0].agi
                else:
                    print("You are wearing.chests already")
                    print(self.helmeq[0])
                    print("Would you like to replave them with...")
                    print(i)
                    while True:
                        x = input("Yes or No")
                        if x == "Yes" or "yes":
                            print("You've replaced your.chests")
                            self.deff -= self.chesteq[0].armour
                            self.luck -= self.chesteq[0].luck
                            self.stamina -= self.chesteq[0].stamina
                            self.iq -= self.chesteq[0].iq
                            self.agi -= self.chesteq[0].agi
                            self.chesteq.remove(self.chesteq[0])
                            self.chesteq.append(i)
                            self.deff += self.chesteq[0].armour
                            self.luck += self.chesteq[0].luck
                            self.stamina += self.chesteq[0].stamina
                            self.iq += self.chesteq[0].iq
                            self.agi += self.chesteq[0].agi
                            break
                        elif x == "No" or "no":
                            self.inventory.remove(i)
                            break

    def equipLegs(self):
        for i in self.inventory:
            x = type(i)
            if "Legs" in str(x):
                if len(self.legeq) < 1:
                    print("You equipped a set alegs")
                    print(i)
                    self.legeq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.legeq[0].armour
                    self.luck += self.legeq[0].luck
                    self.stamina += self.legeq[0].stamina
                    self.iq += self.legeq[0].iq
                    self.agi += self.legeq[0].agi
                else:
                    print("You are wearing.legs already")
                    print(self.legeq[0])
                    print("Would you like to replave them with...")
                    print(i)
                    while True:
                        x = input("Yes or No")
                        if x == "Yes" or "yes":
                            print("You've replaced your.legss")
                            self.deff -= self.legeq[0].armour
                            self.luck -= self.legeq[0].luck
                            self.stamina -= self.legeq[0].stamina
                            self.iq -= self.legeq[0].iq
                            self.agi -= self.legeq[0].agi
                            self.legeq.remove(self.legeq[0])
                            self.legeq.append(i)
                            self.deff += self.legeq[0].armour
                            self.luck += self.legeq[0].luck
                            self.stamina += self.legeq[0].stamina
                            self.iq += self.legeq[0].iq
                            self.agi += self.legeq[0].agi
                            break
                        elif x == "No" or "no":
                            self.inventory.remove(i)
                            break

    def equipBoots(self):
        for i in self.inventory:
            x = type(i)
            if "Boots" in str(x):
                if len(self.bootseq) < 1:
                    print("You equipped a set a.bootss")
                    print(i)
                    self.bootseq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.bootseq[0].armour
                    self.luck += self.bootseq[0].luck
                    self.stamina += self.bootseq[0].stamina
                    self.iq += self.bootseq[0].iq
                    self.agi += self.bootseq[0].agi
                else:
                    print("You are wearing.boots already")
                    print(self.bootseq[0])
                    print("Would you like to replave them with...")
                    print(i)
                    while True:
                        x = input("Yes or No")
                        if x == "Yes" or "yes":
                            print("You've replaced your.bootss")
                            self.deff -= self.bootseq[0].armour
                            self.luck -= self.bootseq[0].luck
                            self.stamina -= self.bootseq[0].stamina
                            self.iq -= self.bootseq[0].iq
                            self.agi -= self.bootseq[0].agi
                            self.bootseq.remove(self.bootseq[0])
                            self.bootseq.append(i)
                            self.deff += self.bootseq[0].armour
                            self.luck += self.bootseq[0].luck
                            self.stamina += self.bootseq[0].stamina
                            self.iq += self.bootseq[0].iq
                            self.agi += self.bootseq[0].agi
                            break
                        elif x == "No" or "no":
                            self.inventory.remove(i)
                            break

    def equipWeapon(self):
        for i in self.inventory:
            try:
                if i.eqType == "Weapon":
                    while True:
                        print(i)
                        x = input("Left or Right hand?")
                        if x == "right" or x == "Right":
                            if len(self.righthandwep) < 1:
                                print("You equip the weapon to your right hand and replace the one that was there.")
                                self.righthandwep.append(i)
                                self.inventory.remove(i)
                                self.atk += self.righthandwep[0].strength
                                self.luck += self.righthandwep[0].luck
                                self.stamina += self.righthandwep[0].stamina
                                self.iq += self.righthandwep[0].iq
                                self.agi += self.righthandwep[0].agi
                                break
                            else:
                                z = input("Would you like to replace your weapon?")
                                if z == "No":
                                    pass
                                elif z == "Yes":
                                    self.atk -= self.righthandwep[0].strength
                                    self.luck -= self.righthandwep[0].luck
                                    self.stamina -= self.righthandwep[0].stamina
                                    self.iq -= self.righthandwep[0].iq
                                    self.agi -= self.righthandwep[0].agi
                                    self.righthandwep.remove(self.righthandwep[0])
                                    self.righthandwep.append(i)
                                    self.inventory.remove(i)
                                    self.atk += self.righthandwep[0].strength
                                    self.luck += self.righthandwep[0].luck
                                    self.stamina += self.righthandwep[0].stamina
                                    self.iq += self.righthandwep[0].iq
                                    self.agi += self.righthandwep[0].agi
                                    break


                        elif x == "Left" or x == "left":
                            if len(self.lefthandwep) < 1:
                                print("You equip the weapon to your left hand and replace the one that was there.")
                                if len(self.lefthandwep) < 1:
                                    print("You equip the weapon to your right hand and replace the one that was there.")
                                    self.lefthandwep.append(i)
                                    self.inventory.remove(i)
                                    self.atk += self.lefthandwep[0].strength
                                    self.luck += self.lefthandwep[0].luck
                                    self.stamina += self.lefthandwep[0].stamina
                                    self.iq += self.lefthandwep[0].iq
                                    self.agi += self.lefthandwep[0].agi
                                    break
                                else:
                                    z = input("Would you like to replace your weapon?")
                                    if z == "No":
                                        pass
                                    elif z == "Yes":
                                        self.atk -= self.lefthandwep[0].strength
                                        self.luck -= self.lefthandwep[0].luck
                                        self.stamina -= self.lefthandwep[0].stamina
                                        self.iq -= self.lefthandwep[0].iq
                                        self.agi -= self.lefthandwep[0].agi
                                        self.lefthandwep.remove(self.lefthandwep[0])
                                        self.lefthandwep.append(i)
                                        self.inventory.remove(i)
                                        self.atk += self.lefthandwep[0].strength
                                        self.luck += self.lefthandwep[0].luck
                                        self.stamina += self.lefthandwep[0].stamina
                                        self.iq += self.lefthandwep[0].iq
                                        self.agi += self.lefthandwep[0].agi
                                        break

                else:
                    pass
            except:
                pass

    def equipAll(self):
        self.equipLegs()
        self.equipBoots()
        self.equipChest()
        self.equipGloves()
        self.equipHelm()
        self.equipWeapon()

    def unequipAll(self):
        try:
            self.addToInv(self.helmeq.pop(0))
            self.addToInv(self.chesteq.pop(0))
            self.addToInv(self.legeq.pop(0))
            self.addToInv(self.bootseq.pop(0))
            self.addToInv(self.gloveeq.pop(0))
            self.addToInv(self.righthandwep.pop(0))
            self.addToInv(self.lefthandwep.pop(0))
        except:
            pass


    def useHpPotion(self):
        for i in self.inventory:
            if i == "Health Potion":
                self.healthAct = self.maxHealth
                self.inventory.remove(i)
                return

    def useMpPotion(self):
        for i in self.inventory:
            if i == "Mana Potion":
                self.manaAct = self.maxMana
                self.inventory.remove(i)
                return

    def attack(self):
        roll = random.randint(1,6)
        if roll == 1:
            print("You done missed AAron")
            return 0
        for i in range(len(self.atklist)):
                print(i + 1 , self.atklist[i])
        roll = random.randint(1,12)
        if self.playerClass == "Warrior":
            while True:
                x = input("What would you like to use 1, 2, or 3 or 4 to use a health potion")
                if x == "1":
                    attk=((self.atk + self.stamina)*roll)*.1
                    break
                elif x == "2" and self. stamina > 10:
                    attk=((self.atk + self.stamina)*roll*2)*.1
                    self.stamina -= 5
                    break
                elif x == "3" and self.stamina >20:
                    attk = ((self.atk + self.stamina) * roll * 3) * .1
                    self.stamina -= 10
                    break
                elif x == "4":
                    self.useHpPotion()
                    attk = 0
                    break
                else:
                    print("not an option")
        elif self.playerClass == "Mage":
            while True:
                print(self.manaAct)
                x = input("What would you like to use 1, 2, or 3 or 4 to use a health potion or 5 to use mana potion")
                if x == "1":
                    attk=((self.atk + self.iq)*roll)*.1
                    break
                elif x == "2" and self. manaAct > 2:
                    attk=((self.atk + self.iq)*roll*2)*.1
                    self.manaAct -= 1
                    break
                elif x == "3" and self.manaAct >5:
                    attk = ((self.atk + self.iq) * roll * 3) * .1
                    self.manaAct -= 2
                    break
                elif x == "4":
                    self.useHpPotion()
                    attk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    attk = 0
                    break
                else:
                    print("not an option")
        elif self.playerClass == "Hunter":
            while True:
                print(self.manaAct)
                x = input("What would you like to use 1, 2, or 3 or 4 to use a health potion or 5 to use mana potion")
                if x == "1":
                    attk=((self.atk + self.agi)*roll)*.1
                    break
                elif x == "2" and self.manaAct > 2:
                    attk=((self.atk + self.agi)*roll*2)*.1
                    self.manaAct -= 1
                    break
                elif x == "3" and self.manaAct >5:
                    attk = ((self.atk + self.agi) * roll * 3) * .1
                    self.manaAct -=2
                    break
                elif x == "4":
                    self.useHpPotion()
                    attk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    attk = 0
                    break
                else:
                    print("not an option")

        elif self.playerClass == "Dog":
            while True:
                print(self.manaAct, "Is how much mana you have")
                x = input("What would you like to use 1, 2, or 3 or 4 to use a health potion")
                if x == "1":
                    attk=((self.atk + self.luck)*roll)*.1
                    break
                elif x == "2" and self.manaAct > 2:
                    attk=((self.atk + self.luck)*roll*2)*.5
                    self.manaAct -= 1
                    break
                elif x == "3" and self.manaAct >5:
                    attk = ((self.atk + self.luck) * roll * 3) * .1
                    self.manaAct -=3
                    break
                elif x == "4":
                    self.useHpPotion()
                    attk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    attk = 0
                    break
        crit = 0
        for i in range(self.luck):
            roll = random.randint(0,3)
            crit += roll
        if crit >= 350:
            print("CRITICAL HIT!")
            attk = attk * 3
        print(self.name, "did", attk, "damage")
        return attk

    def defend(self, damage):
        dmg = damage
        roll = random.randint(1,10)
        if roll == 7:
            print("You bloced the attack!!!!")
            dmg = 0
        roll = random.randint(1,6)
        if self.playerClass == "Warrior":
            block = ((self.deff + self.agi) * roll) * .1
        elif self.playerClass == "Mage":
            block = ((self.deff + self.luck) * roll) * .1
        elif self.playerClass == "Hunter":
            block = ((self.deff + self.stamina) * roll) * .1
        elif self.playerClass == "Dog":
            block = ((self.deff + self.iq) * roll) * .5
        print(self.name, "Blocked", block,"Damage")
        dmgdelt = dmg - block
        if dmg >= 0 :
            self.healthAct = self.healthAct - dmgdelt
        if self.healthAct <= 0 :
            self.Alive = False

























































