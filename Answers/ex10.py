'''
Exercise 10: Rock Paper Scissors Project
- Ask player if they choose rock, paper, or Scissors
- Have computer RANDOMLY choose one of the three
- Compare the choices and decide who wins
- Print result of game
'''

from random import randint

def choice():
    throw = raw_input("Would you like to throw Rock, Paper, or Scissors? (Please type r, p, or s)")

    return throw

def comp_choice():
    throw = {1: 'r', 2: 'p', 3: 's'}
    num = randint(1,3)

    return throw[num]

def logic(choice1, choice2):
    if choice1 == choice2:
        print "Draw!\n"
    elif choice1 == "r" and choice2 == "p":
        print "You: Rock"
        print "Computer: Paper"
        print "Computer wins with Paper!\n"
    elif choice1 == "p" and choice2 == "r":
        print "You: Paper"
        print "Computer: Rock"
        print "You win with Paper!\n"
    elif choice1 == "r" and choice2 == "s":
        print "You: Rock"
        print "Computer: Scissors"
        print "You win with Rock!\n"
    elif choice1 == "s" and choice2 == "r":
        print "You: Scissors"
        print "Computer: Rock"
        print "Computer wins with Rock!\n"
    elif choice1 == "p" and choice2 == "s":
        print "You: Paper"
        print "Computer: Scissors"
        print "Computer wins with Scissors!\n"
    elif choice1 == "s" and choice2 == "p":
        print "You: Scissors"
        print "Computer: Paper"
        print "You win with Scissors!\n"

while True:
    user = choice()
    computer = comp_choice()
    logic(user,computer)
