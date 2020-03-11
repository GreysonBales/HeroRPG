import random


class Equipment(object):
    RARITY = ["Trash", "Common", "Rare", "Epic", "Legendary"]

    def __init__(self, eqType):
        self.rareMod, self.rarityLevel = self.pickRare()

        self.eqType = eqType

    def pickRare(self):
        x = random.randint(1, 10)

        if x >= 1 and x <= 2:
            return 1, Equipment.RARITY[0]
        elif x > 2 and x <= 5:
            return 2, Equipment.RARITY[1]
        elif x > 5 and x < 8:
            return 4, Equipment.RARITY[2]
        elif x >= 8 and x <= 9:
            return 8, Equipment.RARITY[3]
        elif x == 10:
            return 16, Equipment.RARITY[4]

class Armour(Equipment):
    ARMOURTYPE = ["Helm", "Chest", "Legs", "Boots", "Gloves"]

    def __init__(self, aType):
        super(Armour, self).__init__("Armour")
        self.armourType = aType
        self.armour = 0
        self.luck = 0
        self.stamina = 0
        self.iq = 0
        self.agi = 0

    def __str__(self):
        return """
                Armour Type : {}
                Rarity Level : {}
                Armour : {}
                Luck : {}
                Stamina : {}
                Intelect : {}
                Agility: {}
                """.format(self.armourType, self.rarityLevel, self.armour, self.luck, self.stamina, self.iq, self.agi)

class Helm(Armour):
    def __init__(self):
        super(Helm, self).__init__(Armour.ARMOURTYPE[0])
        self.armour = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(0, 8) + self.rareMod
        self.agi = random.randint(0, 8) + self.rareMod
        self.iq = random.randint(0, 8) + self.rareMod
        self.luck = random.randint(0, 8) + self.rareMod

class Chest(Armour):
    def __init__(self):
        super(Chest, self).__init__(Armour.ARMOURTYPE[1])
        self.armour = random.randint(10, 25) * self.rareMod
        self.stamina = random.randint(10, 25) + self.rareMod
        self.agi = random.randint(10, 25) + self.rareMod
        self.iq = random.randint(10, 25) + self.rareMod
        self.luck = random.randint(10, 25) + self.rareMod

class Legs(Armour):
    def __init__(self):
        super(Legs, self).__init__(Armour.ARMOURTYPE[2])
        self.armour = random.randint(5, 15) * self.rareMod
        self.stamina = random.randint(5, 15) + self.rareMod
        self.agi = random.randint(5, 15) + self.rareMod
        self.iq = random.randint(5, 15) + self.rareMod
        self.luck = random.randint(5, 15) + self.rareMod

class Boots(Armour):
    def __init__(self):
        super(Boots, self).__init__(Armour.ARMOURTYPE[3])
        self.armour = random.randint(5, 10) + self.rareMod
        self.stamina = random.randint(3, 10) + self.rareMod
        self.agi = random.randint(3, 10) + self.rareMod
        self.iq = random.randint(3, 10) + self.rareMod
        self.luck = random.randint(3, 10) + self.rareMod

class Gloves(Armour):
    def __init__(self):
        super(Gloves, self).__init__(Armour.ARMOURTYPE[4])
        self.armour = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(2, 10) * self.rareMod
        self.agi = random.randint(2, 10) * self.rareMod
        self.iq = random.randint(2, 10) * self.rareMod
        self.luck = random.randint(2, 10) * self.rareMod

class Weapon(Equipment):
    WEAPONTYPE = ["Sword","Dagger","LongBow","Lightsaber","RustySpoon"]

    def __init__(self,wType):
        super(Weapon, self).__init__("Weapon")
        self.weaponType = wType
        self.strength = 0
        self.luck = 0
        self.stamina = 0
        self.iq = 0
        self.agi = 0

    def __str__(self):
        return """
                Weapon Type : {}
                Rarity Level : {}
                Strength : {}
                Luck : {}
                Stamina : {}
                Intelect : {}
                Agility: {}
                """.format(self.weaponType, self.rarityLevel, self.strength, self.luck, self.stamina, self.iq, self.agi)

class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(Weapon.WEAPONTYPE[0])
        self.strength = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(2, 10) * self.rareMod
        self.agi = random.randint(2, 10) * self.rareMod
        self.iq = random.randint(2, 10) * self.rareMod
        self.luck = random.randint(2, 10) * self.rareMod

class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__(Weapon.WEAPONTYPE[1])
        self.strength = random.randint(10, 15) * self.rareMod
        self.stamina = random.randint(5, 10) * self.rareMod
        self.agi = random.randint(5, 10) * self.rareMod
        self.iq = random.randint(5, 10) * self.rareMod
        self.luck = random.randint(5, 10) * self.rareMod

class LongBow(Weapon):
    def __init__(self):
        super(LongBow, self).__init__(Weapon.WEAPONTYPE[2])
        self.strength = random.randint(10, 15) * self.rareMod
        self.stamina = random.randint(20, 30) + self.rareMod
        self.agi = random.randint(20, 30) + self.rareMod
        self.iq = random.randint(10, 15) + self.rareMod
        self.luck = random.randint(5, 10) + self.rareMod

class Lightsaber(Weapon):
    def __init__(self):
        super(Lightsaber, self).__init__(Weapon.WEAPONTYPE[3])
        self.strength = random.randint(15, 20) * self.rareMod
        self.stamina = random.randint(15, 20) + self.rareMod
        self.agi = random.randint(15, 20) + self.rareMod
        self.iq = random.randint(5, 10) + self.rareMod
        self.luck = random.randint(15, 20) + self.rareMod

class RustySpoon(Weapon):
    def __init__(self):
        super(RustySpoon, self).__init__(Weapon.WEAPONTYPE[4])
        self.strength = random.randint(1, 100) * self.rareMod
        self.stamina = random.randint(1, 100) * self.rareMod
        self.agi = random.randint(1, 100) * self.rareMod
        self.iq = random.randint(1, 100) * self.rareMod
        self.luck = random.randint(1, 100) * self.rareMod