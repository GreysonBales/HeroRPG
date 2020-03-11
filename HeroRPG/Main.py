from HeroRPG.Hero import *
players = []


turn = 0
notturn = 1



def switch(turn):
    if turn  == 0 :
        turn = 1
        notturn = 0
    else:
        turn = 0
        notturn = 1
    return turn, notturn



for i in range(2):
    print("Creating Your Hero", i +1)
    player = Hero()
    player.equipAll()
    players.append(player)

while players[0].Alive:
    print()
    print("It is your turn to attack")
    print(players[turn])
    x = players[turn].attack()
    players[notturn].defend(x)
    if players[1].Alive == False:
        print(players[1].name,"has Died")
        item, xp = players[1].die()
        players[0].collectXp(xp)
        players[0].addToInv(item)
        players[0].equipAll()
        print("A new challenger aproaches")
        player = Hero()
        player.equipAll()
        players[1] = player

    turn, notturn = switch(turn)

print("You have died")

