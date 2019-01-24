import time
import random




class Critter(object):
    """A virtual pet"""

    def ___init___(self, name):
        print("A new critter has been born!")
        self.name = name
        self.__boredom = 0
        self.__hunger = 0

    def __pass_time(self):
        self.__hunger += 1
        self.__boredom += 1

    def play(self):
        print("You take", self.name, "for a walk")
        fun = random.randrange(1,8)
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def talk(self):
        print("\nHi, I'm", self.name)
        print(self.name, "is in a bad mood.")

    def eat(self):
        print("You fed", self.name, "a bagel")
        food = random.randrange(3,10)
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__Pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            mood = "Happy"
        elif 5 < unhappiness <= 10:
            mood = "Okay"
        elif 10 < unhappiness <= 15:
            mood = "Frustrated"
        else:
            mood = "Furiated"
        return mood

def main():
        name = input("What do you want to name your critter?: ")
        crit1 = Critter()
        choice = 0
        while choice == 0:
            print("What do you want to do?\n0. Quit\n1. Have the critter talk\n2. Feed the critter\n3. Play with the critter.")
            choice = int(input("Enter 1,2,3,4: "))
        if choice == 0:
            print("Goodbye")
            exit()
        elif choice == 1:
            crit1.talk()
        elif choice == 2:
            crit1.eat()
        elif choice == 3:
            crit1.play()
        else:
            print("That is not a valid input.")
            exit()

main()





crit = Critter("poochie")
crit.talk()