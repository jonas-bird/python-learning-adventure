#!/usr/bin/env python3

"""
Simple adventure game to bore players with educational tips on how
to go about educating themselves.
Final Project for Intro to Programming with Python 1. Part of Udacity's Intro
to Programming Nano-degree.
Author: Jonas Bird
Date: 2022-03-16
"""
import time
import random


def slow_print(message_to_print):
    # Print a string and then pause
    print(message_to_print)
    time.sleep(1)


def get_input():
    option = ""
    while (option != 1) or (option != 2):
        option = int(input("What would you like to do?\n(Please enter 1 or 2)."))
    return option


def again():
    play_again == 'maybe'
    slow_print("THE")
    slow_print("END")
    while True:
        play_again = input("Would you like to play again? (y/n)").lower()
        if play_again == 'y':
            intro()
        elif play_again == 'n':
            break
        else:
            slow_print("Sorry... I don't understand.")

def intro():
    # Introduce the 'player' to the game
    choices = []
    slow_print("Studying a new topic is an adventure.")
    slow_print("Whether you are studying for a university course,")
    slow_print("preparing for a certification,")
    slow_print("or studying a technical topic on your own,")
    slow_print("good study habits and planning can help you learn faster and"
               " retain the information more completly.")
    slow_print("Playing through this game will introduce you to a few ideas"
               " that may help you succeed!")
    branch_one(choices)


def branch_one(choices):
    # first player choice
    slow_print("Enter 1 to make a study plan.")
    slow_print("Enter 2 to study when you have time")

    if get_input() == 1:
        choices[0] = 'plan'
    else:
        choices[0] = ''
    two(choices)


def two(choices):
    # second player choice
    distractions = ['family', 'work', 'friends', 'stuff']
    distraction = random.choice(distractions)
    slow_print("Oh no!")
    slow_print(f"It has been hard to find time to study because of {distraction}")
    if choices[0] == 'plan':
        slow_print("Luckily with a schedule made up you were prepared to "
                   "manage your time and you are ready to study")
        branch_three(choices)
    elif choices[0] == 'noplan':
        slow_print("Despite your best intentions you didn't manage your time"
                   "well and it is the last minute...")
        bad_ending(distraction)
   else:
       slow_print(f"Well despite your best intention {distraction} has eaten up"
                   "half your time")
       choices[0] = 'noplan'
       branch_one(choices)


def bad_ending(reason):
    pass


def branch_three(choices):
    pass


def main():
    intro()
    slow_print("Well that was fun wasn't it?")


if __name__ == "__main__":
    main()
