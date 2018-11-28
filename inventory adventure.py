#hero's inventory
#Jared McMahon
#11/28
import os
import random
def hud():
    print("stats:",playerStats)
    print("inventory:",inventory)
    print("equiped",equiped)

chestItems = ["gold", "gems", "elven sword", "bow", "crossbow", "boots", "hat", "sun", "traps"]
playerHealth = 100
playerArmor = 1250
playerAttack = 250
playerMoney = 0
inventory = ["Rusty Sword", "Leather Armor","Wood Shield","Small Healing Potion"]
maxInventory = 10
equiped = []
playerStats = ["health",playerHealth,"armor",playerArmor,
               "attack",playerAttack,"money",playerMoney]

print("As you start off on your journey you take with you the following:")
print("player status")
print(playerStats)
print()
print("Your items include:")

for item in inventory:
    print(item)

input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("You have", len(inventory), "/", maxInventory, "items in your inventory.")
print("So you can pick up",maxInventory-len(inventory), "more items.")
input("\nPress the enter key to continue.")
os.system('cls')
hud()

input("\nYou get attacked and take damage.")
playerStats[1] -= 22
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("\nYou have taken some damage on your journey\n",
    "your health is at", playerStats, "\n")
input("you need to use a healing potion. \nPress the enter key to continue.")

if "small healing potion" in inventory:
    print("You will live to fight another day, because you used a healing potion")
    playerStats[1] += 20
    inventory.remove("small healing potion")
input("\nPress the enter key to continue.")
os.system('cls')
hud()

for i in range(len(inventory)):
    print(str(i),inventory[i])
print("lets equipt some armor")
index = input("\nEnter the index number for an armor item in your inventory:")

while index.isdigit()==False:
    index = input("\nEnter the index number for an armor item in your inventory:")
index=int(index)
while index > len(inventory)-1 or index < 0 or index == "":
    print("That number is out of range")
    index = input("\nEnter the index number for an armor item in your inventory:")
    while index.isdigit()==False:
        index = input("\nEnter the index number for an armor item in your inventory:")
    index=int(index)
    


print("You equip your", inventory[index])
equiped.append(inventory[index])
inventory.remove(inventory[index])
if "leather aromor" in equiped:
    playerStats[3] += 1000
if "wood shield" in equipped:
    playerStats[3] =+ 500
input("\nPress the enter key to continue.")
os.system('cls')
hud()

chest = []
for i in range(random.randrange(len(chewstItems))):
    item = random.choice(chestItems)
    chest.append(item)

print("You find a chest which contains:")
print(chest)
print()
print("You add the contents of the chest to your inventory")

if len(inventory) + len(chest) < maxInventory:
    inventory += chest
else:
    drop = len(inventory) + len(chest) - maxInventory
    for i in range(drop):
        x = random.choice(chest)
        chest.remove(x)
    inventory += chest
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("convert tresure to gold")
if "gold" in inventory:
    playerStats[7] +=100
    inventory.remove("gold")
if "gems" in inventory:
    playerStats[7] +=1000
    inventory.remove("gems")
input("\nPress the enter key to continue.")
os.system('cls')
hud()

if playerStats[7] > 100:
    print("do you want sell your sword for 20 gold and buy a cross bow for 100 gold")
    playerStats[7] -= 80
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("You trade your last 2 items from your inventory for a new item.")
inventory[len(inventory)-s:len(inventory)] = ["Orb of Fortue Telling"]
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("In a great battle, your sheild was destroyed")
for i in range(len(inventory)):
    if inventory[i] == "wood shield":
        del inventory[i]
    if equiped[i] == "wood shield":
        del equiped[i]
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("your first 2 items were stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")
os.system('cls')
hud()

input("\nPress the enter key to continue.")








