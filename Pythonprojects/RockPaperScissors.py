#1 = rock
#2 = paper
#3 = scissors

#1 = player1
#2 = player2
#3 = show results

import time
import random

import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def introduce():
    print("Hello, Welcome to Rock, Paper, Scissors")
    
    time.sleep(1.5)
        
    print("\nHere are some rules:\nRock kills Scissors, Scissors kills Paper, Paper kills rock\n\nYou pick your options with the keys Z,X,C (Rock, Paper, Scissors)")
    
    time.sleep(1.5)
    startgame()

def startgame():    
    inputvar = input("\nChoose an option. Play with computer, Play with friend (C,F)")
    inputvar = inputvar.lower()

    if inputvar in ("c","f"):
        if inputvar == "c":
           print("\nPlaying against: Computer")
           playwithcomputer()
        elif inputvar == "f":
           print("\nPlaying against: Friend")
           playwithfriend()
    else:
        print("Invalid answer")
        startgame()

def playwithfriend():
    actionlist = ["Rock", "Paper", "Scissors"]
    
    player_one_choice = None
    player_two_choice = None

    questioninput = input("\nPlayer1 turn\nPick your options with the keys Z,X,C (Rock, Paper, Scissors)")
    questioninput = questioninput.lower()
    if questioninput in ("z","x","c"):
        if questioninput == "z":
           clearConsole()
           player_one_choice = actionlist[0]
        elif questioninput == "x":
           clearConsole()
           player_one_choice = actionlist[1]
        elif questioninput == "c":
           clearConsole()
           player_one_choice = actionlist[2]
    else:
        print("Invalid answer")
        playwithfriend()

    questioninput = input("\nPlayer2 turn\nPick your options with the keys Z,X,C (Rock, Paper, Scissors)")
    questioninput = questioninput.lower()
    if questioninput in ("z","x","c"):
        if questioninput == "z":
           clearConsole()
           player_two_choice = actionlist[0]
        elif questioninput == "x":
           clearConsole()
           player_two_choice = actionlist[1]
        elif questioninput == "c":
           clearConsole()
           player_two_choice = actionlist[2]
    else:
        print("Invalid answer")
        playwithfriend()

    print("\nPlayer1 picked: \"" + player_one_choice + "\" Player2 picked: \"" + player_two_choice + "\"\n")

    if player_one_choice == actionlist[0]:
        if player_two_choice == actionlist[0]:
            print("Its a draw!")
            playwithfriend()
        elif player_two_choice == actionlist[1]:
            print("You lost!")
            startgame()
        elif player_two_choice == actionlist[2]:
            print("You win!")
            startgame()
    elif player_one_choice == actionlist[1]:
        if player_two_choice == actionlist[0]:
            print("You win!")
            startgame()
        elif player_two_choice == actionlist[1]:
            print("Its a draw!")
            playwithfriend()
        elif player_two_choice == actionlist[2]:
            print("You lost!")
            startgame()
    elif player_one_choice == actionlist[2]:
        if player_two_choice == actionlist[0]:
            print("You lost!")
            startgame()
        elif player_two_choice == actionlist[1]:
            print("You win!")
            startgame()
        elif player_two_choice == actionlist[2]:
            print("Its a draw!")
            playwithfriend()

def playwithcomputer():
    actionlist = ["Rock", "Paper", "Scissors"]
    
    computerchoice = None
    playerchoice = None
    
    questioninput = input("\nPick your options with the keys Z,X,C (Rock, Paper, Scissors)")
    questioninput = questioninput.lower()

    if questioninput in ("z","x","c"):
        if questioninput == "z":
            clearConsole()
            playerchoice = actionlist[0]
        elif questioninput == "x":
            clearConsole()
            playerchoice = actionlist[1]
        elif questioninput == "c":
            clearConsole()
            playerchoice = actionlist[2]
    else:
        print("Invalid answer")
        playwithcomputer()    

    computerchoice = random.choice(actionlist)
    print("\nYou picked: \"" + playerchoice + "\" Computer picked: \"" + computerchoice + "\"\n")

    if playerchoice == actionlist[0]:
        if computerchoice == actionlist[0]:
            print("Its a draw!")
            playwithcomputer()
        elif computerchoice == actionlist[1]:
            print("You lost!")
            startgame()
        elif computerchoice == actionlist[2]:
            print("You win!")
            startgame()
    elif playerchoice == actionlist[1]:
        if computerchoice == actionlist[0]:
            print("You win!")
            startgame()
        elif computerchoice == actionlist[1]:
            print("Its a draw!")
            playwithcomputer()
        elif computerchoice == actionlist[2]:
            print("You lost!")
            startgame()
    elif playerchoice == actionlist[2]:
        if computerchoice == actionlist[0]:
            print("You lost!")
            startgame()
        elif computerchoice == actionlist[1]:
            print("You win!")
            startgame()
        elif computerchoice == actionlist[2]:
            print("Its a draw!")
            playwithcomputer()

introduce()
