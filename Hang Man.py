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
words = ()

for i in range(len(HANGMAN)):
    print(HANGMAN[i])
    time.sleep(2)
