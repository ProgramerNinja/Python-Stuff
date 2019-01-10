#Jared McMahon
#11/30/2018
#


gameList =  []

while True:
    option = int(input("""
    1 - add a game to your list
    2 - remove a game from your list
    3 - insert a game in to your list
    """))
    if option == 1:
        game = input("what game would you like to add to your list")
        gameList.append(game)
        print(gameList)
    elif option == 2:
        print(gameList)
        game = input("what game would you like to remove from your list")
        while True:
            if game in gameList:
                q = input("are you sure you want to delet " + game)
                if q == "yes":
                    gameList.remove(game)
                    print(gameList)
                    break
                else:
                    print("then why did you choose option 2")
            else:
                print(game + " is not in your list")
    elif option == 3:
        game = input("what game would you like to add to your list")
        pos = int(input("at what position would you like to place " + game + "in your list"))
        pos -= 1

        while True:
            if pos < len(gameList):
                gameList.insert(pos,game)
                print(gameList)
                break
            else:
                print("invalid postion")
    elif option == 4:
        input("press enter to exit")
        break
    else:
        print("thats not a very good option")
