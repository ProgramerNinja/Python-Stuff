#Chutes and ladders
#Jared M.
#1/19

#imports
########################################################################################################
import random

#global variables
########################################################################################################
p1p = []
p2p = []
p3p = []
p4p = []
EMPTY = " "
#classes
########################################################################################################
class Player(object):

    def __init__(self,name,num):
        self.name = name
        self.position = -1
        self.player_num = num
        self.token = self.name[0]

    def roll(self):
        die1 = random.randrange(1,6)
        die2 = random.randrange(1,6)
        roll = die1 + die2
        print("The roll was", die1, "and", die2,".  Total was:", roll)
        return roll

    def move(self):
        roll = self.roll()
        if self.position + roll < 99:
            oldpos = self.position
            self.position = self.position + roll
            if self.player_num == 1:
                p1p[oldpos] = EMPTY
                p1p[self.position] = self.token
            elif self.player_num == 2:
                p2p[oldpos] = EMPTY
                p2p[self.position] = self.token
            elif self.player_num == 3:
                p3p[oldpos] = EMPTY
                p3p[self.position] = self.token
            elif self.player_num == 4:
                p3p[oldpos] = EMPTY
                p3p[self.position] = self.token
        else:
            print("You have to roll roll a "+str(99-self.position)+" to land on the winning '100' space!")
        return


    def win(self):
        if self.position == 99:
            print("Yay the torturing has ended")
            return self.token
        else:
            return None



class Board(object):
    pass

class Space(object):
    pass

#functions
########################################################################################################
def ask_num():
    pass

def switch_turn():
    pass

def winner_congrats():
    pass

#main
########################################################################################################
def main():
    for x in range(99):
        p1p.append(EMPTY)
        p2p.append(EMPTY)
        p3p.append(EMPTY)
        p4p.append(EMPTY)

    name = input("What is your name?: ")
    num = int(input("What player are you? ex. player 1, player 2. Answer with a single digit (1-4): "))
    player = Player(name,num)
    print(player.name)
    print(player.token)
    print(player.position)
    winner = None
    while not winner:
        player.move()
        winner = player.win()
        print(p1p)
        print(winner)

#run
########################################################################################################
main()