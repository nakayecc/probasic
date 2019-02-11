import random

attacker = []
defender = []


def army():
    try:
        val = int(input("How many units attack: "))
        while not (1 <= val <= 3):
            print("select od 1-3")
            val = int(input("How many units attack: "))
        val2 = int(input("How many units attack: "))
        while not (1 <= val2 <= 2):
            print("select 1-2")
            val2 = int(input("How many units attack: "))
    except ValueError:
        print("select int values")
        army()
    return val, val2


def roll():
    for x in range(val):
        tmp = random.randrange(1, 7)
        attacker.append(tmp)
    for y in range(val2):
        tmp = random.randrange(1, 7)
        defender.append(tmp)


def fight(val1, val2, attacker, defender):
    deflost = 0
    attlost = 0
    if (val1 > val2):
        min = val2
    else:
        min = val1

    for x in range(min):
        if (attacker[x] > defender[x]):
            deflost = deflost + 1
        elif (defender[x] >= attacker[x]):
            attlost = attlost + 1
    return deflost, attlost


val, val2 = army()
roll()
print("Dice: ")
print('Attacker: ' + '-'.join(map(str, attacker)))
print('Defender: ' + '-'.join(map(str, defender)))
print('\n')
print("Outcome: ")
dl, al = fight(val, val2, attacker, defender)
print('Attacker: Lost: ' + str(al) + ' unit')
print('Defender: Lost: ' + str(dl) + ' unit')
