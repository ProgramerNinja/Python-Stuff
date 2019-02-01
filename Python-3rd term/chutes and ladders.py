# Chutes and ladders
# Jared M.
# 1/19

# imports
########################################################################################################
import random

# global variables
########################################################################################################
p1p = []
p2p = []
p3p = []
p4p = []
EMPTY = " "
# classes
########################################################################################################


class Player(object):

    def __init__(self, name, num):
        self.name = name
        self.position = -1
        self.player_num = num
        self.token = self.name[0]

    def roll(self):
        die1 = random.randrange(1, 6)
        die2 = random.randrange(1, 6)
        roll = die1 + die2
        print("The roll was", die1, "and", die2, ".  Total was:", roll)
        return roll

    def move(self):
        roll = self.roll()
        if self.position + roll < 100:
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
            print("You have to roll a "+str(99-self.position)+" to land on the winning '100' space!")
            oldpos = self.position
            self.position = self.position - ((self.position + roll)-99)
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

        return self.position

    def win(self):
        if self.position == 99:
            print("Yay the torturing has ended")
            return self.token
        else:
            return None


class Board(object):
    def __init__(self):
        self.board = []

    def create_spaces(self):
        esp = Space(0)
        for i in range(100):
            self.board.append(esp)
        sp1 = Space(37)
        self.board[0] = sp1
        sp4 = Space(10)
        self.board[3] = sp4
        sp9 = Space(21)
        self.board[8] = sp9
        sp16 = Space(-11)
        self.board[15] = sp16
        sp21 = Space(11)
        self.board[20] = sp21
        sp28 = Space(64)
        self.board[27] = sp28
        sp51 = Space(13)
        self.board[50] = sp51
        sp56 = Space(-3)
        self.board[55] = sp56
        sp62 = Space(-43)
        self.board[61] = sp62
        sp64 = Space(-4)
        self.board[63] = sp64
        sp71 = Space(11)
        self.board[70] = sp71
        sp80 = Space(20)
        self.board[79] = sp80
        sp87 = Space(-63)
        self.board[86] = sp87
        sp93 = Space(-20)
        self.board[92] = sp93
        sp95 = Space(-20)
        self.board[94] = sp95
        sp98 = Space(-20)
        self.board[97] = sp98
        for i in range(100):
            p1p.append(EMPTY)
            p2p.append(EMPTY)
            p3p.append(EMPTY)
            p4p.append(EMPTY)

    def display_board(self):
        print("------------------------------------------------------------------------")
        print(
            "|91" + p1p[90] + p2p[90] + "  |92" + p1p[91] + p2p[91] + "  |93" + p1p[92] + p2p[92] + "  |94" + p1p[93] +
            p2p[93] + "  |95" + p1p[94] + p2p[94] + "  |96" + p1p[95] + p2p[95] + "  |97" + p1p[96] + p2p[
                96] + "  |98" + p1p[97] + p2p[97] + "  |99" + p1p[98] + p2p[98] + "  |100" + p1p[99] + p2p[99] + "  | ")
        print(
            "|  " + p3p[90] + p4p[90] + "  |  " + p3p[91] + p4p[91] + "  |  " + p3p[92] + p4p[92] + "  |  " + p3p[93] +
            p4p[93] + "  |  " + p3p[94] + p4p[94] + "  |  " + p3p[95] + p4p[95] + "  |  " + p3p[96] + p4p[
                96] + "  |  " + p3p[97] + p4p[97] + "  |  " + p3p[98] + p4p[98] + "  |   " + p3p[99] + p4p[99] + "  | ")
        print("------------------------------------------------------------------------")
        print(
            "|90" + p1p[89] + p2p[89] + "  |89" + p1p[88] + p2p[88] + "  |88" + p1p[87] + p2p[87] + "  |87" + p1p[86] +
            p2p[86] + "  |86" + p1p[85] + p2p[85] + "  |85" + p1p[84] + p2p[84] + "  |84" + p1p[83] + p2p[
                83] + "  |83" + p1p[82] + p2p[82] + "  |82" + p1p[81] + p2p[81] + "  | 81" + p1p[80] + p2p[80] + "  | ")
        print(
            "|  " + p3p[89] + p4p[89] + "  |  " + p3p[88] + p4p[88] + "  |  " + p3p[87] + p4p[87] + "  |  " + p3p[86] +
            p4p[86] + "  |  " + p3p[85] + p4p[85] + "  |  " + p3p[84] + p4p[84] + "  |  " + p3p[83] + p4p[
                83] + "  |  " + p3p[82] + p4p[82] + "  |  " + p3p[81] + p4p[81] + "  |   " + p3p[80] + p4p[80] + "  | ")
        print("------------------------------------------------------------------------")
        print(
            "|71" + p1p[70] + p2p[70] + "  |72" + p1p[71] + p2p[71] + "  |73" + p1p[72] + p2p[72] + "  |74" + p1p[73] +
            p2p[73] + "  |75" + p1p[74] + p2p[74] + "  |76" + p1p[75] + p2p[75] + "  |77" + p1p[76] + p2p[
                76] + "  |78" + p1p[77] + p2p[77] + "  |79" + p1p[78] + p2p[78] + "  | 80" + p1p[79] + p2p[79] + "  | ")
        print(
            "|  " + p3p[70] + p4p[70] + "  |  " + p3p[71] + p4p[71] + "  |  " + p3p[72] + p4p[72] + "  |  " + p3p[73] +
            p4p[73] + "  |  " + p3p[74] + p4p[74] + "  |  " + p3p[75] + p4p[75] + "  |  " + p3p[76] + p4p[
                76] + "  |  " + p3p[77] + p4p[77] + "  |  " + p3p[78] + p4p[78] + "  |   " + p3p[79] + p4p[79] + "  | ")
        print("------------------------------------------------------------------------")
        print(
            "|70" + p1p[69] + p2p[69] + "  |69" + p1p[68] + p2p[68] + "  |68" + p1p[67] + p2p[67] + "  |67" + p1p[66] +
            p2p[66] + "  |66" + p1p[65] + p2p[65] + "  |65" + p1p[64] + p2p[64] + "  |64" + p1p[63] + p2p[
                63] + "  |63" + p1p[62] + p2p[62] + "  |62" + p1p[61] + p2p[61] + "  | 61" + p1p[60] + p2p[60] + "  | ")
        print(
            "|  " + p3p[69] + p4p[69] + "  |  " + p3p[68] + p4p[68] + "  |  " + p3p[67] + p4p[67] + "  |  " + p3p[66] +
            p4p[66] + "  |  " + p3p[65] + p4p[65] + "  |  " + p3p[64] + p4p[64] + "  |  " + p3p[63] + p4p[
                63] + "  |  " + p3p[62] + p4p[62] + "  |  " + p3p[61] + p4p[61] + "  |   " + p3p[60] + p4p[60] + "  | ")
        print("------------------------------------------------------------------------")
        print(
            "|51" + p1p[50] + p2p[50] + "  |52" + p1p[51] + p2p[51] + "  |53" + p1p[52] + p2p[52] + "  |54" + p1p[53] +
            p2p[53] + "  |55" + p1p[54] + p2p[54] + "  |56" + p1p[55] + p2p[55] + "  |57" + p1p[56] + p2p[
                56] + "  |58" + p1p[57] + p2p[57] + "  |59" + p1p[58] + p2p[58] + "  | 60" + p1p[59] + p2p[59] + "  | ")
        print(
            "|  " + p3p[50] + p4p[50] + "  |  " + p3p[51] + p4p[51] + "  |  " + p3p[52] + p4p[52] + "  |  " + p3p[53] +
            p4p[53] + "  |  " + p3p[54] + p4p[54] + "  |  " + p3p[55] + p4p[55] + "  |  " + p3p[56] + p4p[
                56] + "  |  " + p3p[57] + p4p[57] + "  |  " + p3p[58] + p4p[58] + "  |   " + p3p[59] + p4p[59] + "  | ")
        print("------------------------------------------------------------------------")
        print(
            "|50" + p1p[49] + p2p[49] + "  |49" + p1p[48] + p2p[48] + "  |48" + p1p[47] + p2p[47] + "  |47" + p1p[46] +
            p2p[46] + "  |46" + p1p[45] + p2p[45] + "  |45" + p1p[44] + p2p[44] + "  |44" + p1p[43] + p2p[
                43] + "  |43" + p1p[42] + p2p[42] + "  |42" + p1p[41] + p2p[41] + "  | 41" + p1p[40] + p2p[40] + "  | ")
        print(
            "|  " + p3p[49] + p4p[49] + "  |  " + p3p[48] + p4p[48] + "  |  " + p3p[47] + p4p[47] + "  |  " + p3p[46] +
            p4p[46] + "  |  " + p3p[45] + p4p[45] + "  |  " + p3p[44] + p4p[44] + "  |  " + p3p[43] + p4p[
                43] + "  |  " + p3p[42] + p4p[42] + "  |  " + p3p[41] + p4p[41] + "  |   " + p3p[40] + p4p[40] + "  | ")
        print("------------------------------------------------------------------------")
        print(
            "|31" + p1p[30] + p2p[30] + "  |32" + p1p[31] + p2p[31] + "  |33" + p1p[32] + p2p[32] + "  |34" + p1p[33] +
            p2p[33] + "  |35" + p1p[34] + p2p[34] + "  |36" + p1p[35] + p2p[35] + "  |37" + p1p[36] + p2p[
                36] + "  |38" + p1p[37] + p2p[37] + "  |39" + p1p[38] + p2p[38] + "  | 40" + p1p[39] + p2p[39] + "  | ")
        print(
            "|  " + p3p[30] + p4p[30] + "  |  " + p3p[31] + p4p[31] + "  |  " + p3p[32] + p4p[32] + "  |  " + p3p[33] +
            p4p[33] + "  |  " + p3p[34] + p4p[34] + "  |  " + p3p[35] + p4p[35] + "  |  " + p3p[36] + p4p[
                36] + "  |  " + p3p[37] + p4p[37] + "  |  " + p3p[38] + p4p[38] + "  |   " + p3p[39] + p4p[39] + "  | ")
        print("------------------------------------------------------------------------")
        print(
            "|30" + p1p[29] + p2p[29] + "  |29" + p1p[28] + p2p[28] + "  |28" + p1p[27] + p2p[27] + "  |27" + p1p[26] +
            p2p[26] + "  |26" + p1p[25] + p2p[25] + "  |25" + p1p[24] + p2p[24] + "  |24" + p1p[23] + p2p[
                23] + "  |23" + p1p[22] + p2p[22] + "  |22" + p1p[21] + p2p[21] + "  | 21" + p1p[20] + p2p[20] + "  | ")
        print(
            "|  " + p3p[29] + p4p[29] + "  |  " + p3p[28] + p4p[28] + "  |  " + p3p[27] + p4p[27] + "  |  " + p3p[26] +
            p4p[26] + "  |  " + p3p[25] + p4p[25] + "  |  " + p3p[24] + p4p[24] + "  |  " + p3p[23] + p4p[
                23] + "  |  " + p3p[22] + p4p[22] + "  |  " + p3p[21] + p4p[21] + "  |   " + p3p[20] + p4p[20] + "  | ")
        print("------------------------------------------------------------------------")
        print(
            "|11" + p1p[10] + p2p[10] + "  |12" + p1p[11] + p2p[11] + "  |13" + p1p[12] + p2p[12] + "  |14" + p1p[13] +
            p2p[13] + "  |15" + p1p[14] + p2p[14] + "  |16" + p1p[15] + p2p[15] + "  |17" + p1p[16] + p2p[
                16] + "  |18" + p1p[17] + p2p[17] + "  |19" + p1p[18] + p2p[18] + "  | 20" + p1p[19] + p2p[19] + "  | ")
        print(
            "|  " + p3p[10] + p4p[10] + "  |  " + p3p[11] + p4p[11] + "  |  " + p3p[12] + p4p[12] + "  |  " + p3p[13] +
            p4p[13] + "  |  " + p3p[14] + p4p[14] + "  |  " + p3p[15] + p4p[15] + "  |  " + p3p[16] + p4p[
                16] + "  |  " + p3p[17] + p4p[17] + "  |  " + p3p[18] + p4p[18] + "  |   " + p3p[19] + p4p[19] + "  | ")
        print("------------------------------------------------------------------------")
        print("|10" + p1p[9] + p2p[9] + "  | 9" + p1p[8] + p2p[8] + "  | 8" + p1p[7] + p2p[7] + "  | 7" + p1p[6] + p2p[
            6] + "  | 6" + p1p[5] + p2p[5] + "  | 5" + p1p[4] + p2p[4] + "  | 4" + p1p[3] + p2p[3] + "  | 3" + p1p[2] +
              p2p[2] + "  | 2" + p1p[1] + p2p[1] + "  |  1" + p1p[0] + p2p[0] + "  | ")
        print("|  " + p3p[9] + p4p[9] + "  |  " + p3p[8] + p4p[8] + "  |  " + p3p[7] + p4p[7] + "  |  " + p3p[6] + p4p[
            6] + "  |  " + p3p[5] + p4p[5] + "  |  " + p3p[4] + p4p[4] + "  |  " + p3p[3] + p4p[3] + "  |  " + p3p[2] +
              p4p[2] + "  |  " + p3p[1] + p4p[1] + "  |  " + p3p[0] + p4p[0] + "  | ")


class Space(object):
    def __init__(self, move):
        self.move = move

    def move_player(self, player, board):
        oldpos = player.position
        player.position = player.position + self.move
        if self.move > 0:
            print("This place has a ladder. " + player.token + " moves up", self.move, "spaces")
            input("Press enter to continue...")
        elif self.move < 0:
            print("This space has a chute on it." + player.token + " slides down", self.move, "spaces")
            input("Press enter to continue...")
        if self.move > 0 or self.move < 0:
            if player.player_num == 1:
                p1p[oldpos] = EMPTY
                p1p[player.position] = player.token
            elif player.player_num == 2:
                p2p[oldpos] = EMPTY
                p2p[player.position] = player.token
            elif player.player_num == 3:
                p3p[oldpos] = EMPTY
                p3p[player.position] = player.token
            elif player.player_num == 4:
                p4p[oldpos] = EMPTY
                p4p[player.position] = player.token
        Board.display_board(self)


#functions
########################################################################################################
def ask_num():
    num_players = int(input("How many people are playing? (1-4):"))
    return num_players

def switch_turn(num_players, turn):
    winner = None
    while not winner:
        winner = players[turn].win()
        turn + 1
        if turn > num_players:
            turn = 0
    return turn


def winner_congrats():
    winner = players[turn].win()
    print("Hoo Yaa" + winner + "won!")

#main
########################################################################################################
def main():
    num_players = ask_num()
    players = []
    turn = -1
    winner = None
    board = Board()
    board.create_spaces()
    for i in range(num_players):
        print("Player", i+1)
        name = input("Enter your name: ")
        name = name.title()
        player = Player(name, i+1)
        players.append(player)


    while not winner:
        print(players[turn].token + " it is your turn!")
        input("Press enter to roll!")
        players[turn].move()
        playerpos = players[turn].position
        space = board.board[playerpos]
        space.move_player(players[turn], board)
        winner = players[turn].win()
        turn = switch_turn(num_players, turn) ##switch_turn(num_players, turn)

    winner_congrats()
    print(winner)
    input("Press enter to quit...")




#    name = input("What is your name?: ")
#    num = int(input("What player are you? ex. player 1, player 2. Answer with a single digit (1-4): "))
#    player = Player(name,num)
#    print(player.name)
#    print(player.token)
#    print(player.position)
#    winner = None
#    board = Board()
#    while not winner:
#        board.display_board()
#        player.move()
#        winner = player.win()
#        print(p1p)
#        print(winner)
#        input()

#run
########################################################################################################
main()