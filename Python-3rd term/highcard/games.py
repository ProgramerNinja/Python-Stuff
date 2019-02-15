# Jared M.
# 2/13/2019
# Card Games

class Player(object):
    """ A player for the game """

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name
        rep = rep + " " + str(self.score)
        return rep


def ask_number(question, low, high):
    # ask_num(question="how many players: ", low=2, high=11)

    """Gets a number from user when called"""
    while True:
        num_players = input(question)
        try:
            num_players = int(num_players)
            if low <= num_players < high:
                return num_players
            else:
                print("Sorry, please choose again")
        except:
            print("That was not a valid input.")


def ask_yes_no(question):
    #   ask_yes_no(question="bipitty boppity boop")

    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question + " y or n").lower()
    return response


def switch_turn(num_players, turn):
    # turn = -1
    # num_players = ask_num(question="how many players: ", low=2, high=11)
    # turn = switch_turn(num_players, turn)
    # switch_turn(num_players, turn)
    # print(turn)

    """when called it switches turn to next player"""
    turn = turn + 1
    if turn >= num_players:
        turn = 0
    return turn


def roll():
    # print(roll())

    """rolls a pair of six sided dice when called"""
    import random
    die1 = random.randrange(1, 6)
    die2 = random.randrange(1, 6)
    total = die1 + die2
    print("The roll was", die1, "and", die2, ".  Total was:", total)
    return total, die1, die2


def winner_congrats(winner):
    # winner = "joe"
    # winner_congrats(winner)

    """Congrats the 'winner'"""
    print("Hoo Yaa", winner, "won!")


if __name__ == "__main__":
    print("You ran  this module directly (and did not import it).")
    input("\n\nPress the enter key to exit.")
