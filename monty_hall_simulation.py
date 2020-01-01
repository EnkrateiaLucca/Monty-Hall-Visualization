import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import random


class MontyHall:
    def __init__(self,rounds=100, number_runs=1000):
        self.rounds = rounds
        self.number_runs = number_runs
        self.victories = 0
        self.losts = 0

    def play_game(self):
        counter = 0
        victories = 0
        losts = 0
        for i in range(self.rounds):
            doors = [1,2,3]
            print("Welcome to the Monty Hall problem!")
            winning_door = random.choice(doors)
            choice = int(input("Select a door (1,2,3):"))
            doors.pop(doors.index(winning_door))
            goat_door = doors[0]
            if goat_door == choice:
                goat_door = doors[1]
            doors.append(winning_door)
            print("Doors. {}".format(doors))
            print("This door is a goat: {}".format(goat_door))
            switch_question = input("Would you like to switch? (y or n):")
            if switch_question == "y":
                doors.remove(goat_door)
                print("CHOICE: {}".format(choice))
                doors.remove(choice)
                choice = doors[0]
            if choice == winning_door:
                print("Your door: {}".format(choice))
                print("Winning door: {}".format(winning_door))
                print("You won!")
                self.victories += 1
            else:
                print("Your door: {}".format(choice))
                print("Winning door: {}".format(winning_door))
                print("You loose!")
                self.losts +=1

            counter+=1

        print("Number of victories: {}".format(self.victories))
        print("Number of losts: {}".format(self.losts))


    def simulate(self,strategy="switch", show=False):
        counter = 0
        self.victories = []
        self.losts = []
        for i in range(self.number_runs):
            doors = [1,2,3]
            winning_door = random.choice(doors)
            choice = random.choice(doors)
            doors.pop(doors.index(winning_door))
            goat_door = doors[0]
            if goat_door == choice:
                goat_door = doors[1]
            doors.append(winning_door)
            switch_question = strategy
            if switch_question == "switch":
                doors.remove(goat_door)
                doors.remove(choice)
                choice = doors[0]
            if choice == winning_door:
                print("Your door: {}".format(choice))
                print("Winning door: {}".format(winning_door))
                print("You won!")
                self.victories.append(1)
            else:
                print("Your door: {}".format(choice))
                print("Winning door: {}".format(winning_door))
                print("You loose!")
                self.losts.append(0)

            counter+=1


if __name__=="__main__":
    ratios = []
    strategy = "switch"
    for i in range(1,100):
        monty = MontyHall(number_runs=10 * i)
        monty.simulate(strategy, show=False)
        ratios.append(len(monty.victories)/(len(monty.losts) + len(monty.victories)))

    plt.plot(ratios)
    plt.ylim(0,1)
    plt.title("Ratios for victories")
    plt.show()

