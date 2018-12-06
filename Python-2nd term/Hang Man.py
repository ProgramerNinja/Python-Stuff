#Jared ,McMahon
#hangman game
#11/26/2018

#imports
import time
import random

#constants
HANGMAN = (
"""
 ________
 |      |
 |      |
 |
 |
 |
 |
 |
 |
 |
 |
 |
------------
""",
"""
 ________
 |      |
 |      |
 |      Q
 |
 |
 |
 |
 |
 |
 |
 |
------------
""",
"""
 ________
 |      |
 |      |
 |      Q
 |      |\\
 |
 |
 |
 |
 |
 |
 |
------------
""",
"""
 ________
 |      |
 |      |
 |      Q
 |     /|\\
 |
 |
 |
 |
 |
 |
 |
------------
""",
"""
 ________
 |      |
 |      |
 |      Q
 |     /|\\
 |      |
 |     /
 |
 |
 |
 |
 |
------------
""",
"""
 ________
 |      |
 |      |
 |      Q
 |     /|\\
 |      |
 |     / \\
 |
 |
 |
 |Dead!!!
 |   So Dead!!!
------------
""")



MAX_WRONG = len(HANGMAN)-1
WORDS = ("INPUT","BREAK","IMPORT","FOR LOOP","PYTHON")

word = random.choice(WORDS) #word to be guessed
so_far = "_"*len((word)) #one dash for each letter
wrong = 0 # nuber of wrong guesses
used = [] # letters already guessed

print("Welcome to Hangman. Good Luck!")

while wrong < MAX_WRONG and so_far != word:

    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("So far, the word is:\n", so_far)
    
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()


    while guess in used:
        print("You've already guessed that letter" , guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nYes!",guess, "is in the word!")

        #create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry," ,guess, "isn't in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")

else:
    print("\nYou guessed it!")
print("\n The word was", word)

input("\n\nPress the enter key to exit.")























