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
    time.sleep(2)


def get_input():
    option = ""
    while option not in (1, 2):
        option = int(input("What would you like to do?\n"
                           "(Please enter 1 or 2):"))
    return option


def again():
    play_again = 'maybe'
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
    choices = ['']
    """ there are simpler ways of keeping track of the option the player chose in
       a game this short, but as I plan to extend it as a portfolio project I
       felt using a list was a better design choice. Eventually I will probably
       include a player class to keep track of progress through the game"""
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
        choices.insert(0, 'study')

    two(choices)


def two(choices):
    # second player choice
    distractions = ['family', 'work', 'friends', 'stuff', 'social media']
    distraction = random.choice(distractions)
    slow_print("Oh no!")
    slow_print(f"It has been hard to find time to study because of"
               f" {distraction}")
    if choices[0] == 'study':
        slow_print("Luckily with a schedule made up you were prepared to "
                   "manage your time and you are ready to study")
        branch_three(choices)
    elif choices[0] == 'noplan':
        slow_print("Despite your best intentions you didn't manage your time"
                   " well and it is the last minute...")
        bad_ending(distraction)
    else:
        slow_print(f"Well despite your best intention {distraction} has eaten "
                   "up half your time")
        choices[0] = 'noplan'
        branch_one(choices)


def bad_ending(reason):
    slow_print(f"Unfortunatly because of poor planning you did not have enough"
               f"time to deal with {reason}")
    slow_print("and study...")
    slow_print("Hopefully next time will go better!")


def good_ending():
    slow_print("With good planning you have completed your course and your"
               "learning adventure!")


def branch_three(choices):
    slow_print("Reviewing course material is an important part of learning")
    slow_print("Besides making it easier to review, taking notes can help a"
               "student remember difficult material.,,")
    slow_print("That is worth a shot... (Enter 1):")
    slow_print("I have always had a good memory, and that would take too "
               "much time (Enter 2):")
    if get_input() == 1:
        good_ending()
    else:
        bad_ending("poor organization")



def main():
    intro()
    slow_print("Well that was fun wasn't it?")
    again()

if __name__ == "__main__":
    main()
