#Jared M.
#10/12/18
import random

win=0
phealth = 100
mhealth = 100
print("The end is coming")
choice = input("fight or run")

while choice == "fight":
    playerDamage = random.randrange(0,8)
    mhealth = mhealth - playerDamage
    print("you attack the beasts that lunged at you that were sprouting from the ends origin you attacked and did" , playerDamage , "damage. the monster's health is now at" , mhealth)
    if mhealth <= 0:
        print("you killed the beast")
        win = 1
        break
    if mhealth >= 0:
        monsterDamage = random.randrange(2,6)
        phealth = phealth - monsterDamage
        print("the beast fights back, you take" , monsterDamage , "damage")
    if phealth <= 0:
        print("you died")
        win = 0
        break
    if phealth >= 0 and mhealth >=0:
        print("your health is at" , phealth)
        print("the beast's health is at" , mhealth)
    choice = input("fight or run")
    if choice == 'fight':
        continue
    else:
        break

if choice == "run":
    print("you are a coward")
if  win == 0:
    print("you lose")
if  win == 1:
    print("you won with" , phealth , "health left")
