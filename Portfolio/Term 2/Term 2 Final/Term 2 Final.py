##Jared M.
##1/2/2019
##Term 2 Final

import sys

def open_file(file_name,mode):
    """Open File."""
    try:
        file = open(file_name,mode)
    except IOError as e:
        print("unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return file

def next_line(the_file):
    try:
        line = the_file.readline()
    except:
        print("unable to assign the file line of", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
    else:
        """Return next line from the trivia file, formatted."""
        line = line.replace("/","\n")
        return line

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        temp_answer = next_line(the_file)
        answers.append(temp_answer)
        
    correct = next_line(the_file)
    
    if correct:
        correct = correct[0]
    
    explenation = next_line(the_file)
    
    return category, question, answers, correct, explenation

def welcome(title):
    """Welcoming the player."""
    print("\t\tWelcome to my Trivia Quiz!")
    print("\t\t", title, "\n")


def main():
    the_file = open_file("trivia_stuff.txt","r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explenation = next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(answers[i])
        guess = input("What do you think the answer is?: ").lower()
        if guess == correct:
            print("Yay! you got it right!")
            score = score + 1
        else:
            print("That was wrong. :[")
        print(explenation)
        print("Your score is now", score)
        category, question, answers, correct, explenation = next_block(the_file)

    print("Thanks for playing my Trivia quiz.\n\t\tYor Score was ", score, "out of 10")
    input("Press the enter key to exit")
    sys.exit()

main()
