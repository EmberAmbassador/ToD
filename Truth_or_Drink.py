import subprocess
import time
import random
import os

test = "C:/Users/Luca/Desktop/Truth_or_Drink/Decks/1on_the_rocks/(1).pdf"
baseDir = "C:/Users/Luca/Desktop/Games/Private_Games_custom/Truth_or_Drink/Decks"
reader = "C:/Program Files (x86)/Adobe/Acrobat Reader DC/Reader/AcroRd32.exe"

clear = lambda: os.system('cls')

#subP = subprocess.Popen([reader, test])
#time.sleep(2)
#subP.kill()
#print("done")

####################################################################
# Functions to slim down the code
def printPoints():
    print("_____________________________")
    print("Current Scoreboard")
    print("_____________________________")
    print("Benni: " + str(Benni))
    print("Lisa: " + str(Lisa))
    print("Luca: " + str(Luca))
    print("_____________________________")

def anotherRound():
    again = input("This was fun! You wanna go again? \n \n")
    done = False
    while not(done):
        if again == "No":
            done = True
            quit()
        elif again == "Yes":
            done = True
        else:
            again = input("There seems to have been a typo. Try again. \n \n")
####################################################################


while True:
    deck = input("Which deck would you like to play? \n \
1) On the Rocks \n \
2) Extra Dirty \n \
3) Happy Hour \n \
4) Last Call \n \
5) With a Twist not implemented yet (sorry) \n \n")

    Lisa = 0
    Benni = 0
    Luca = 0
    cards = list(range(1, 54))
    endOfRound = False

    deck = int(deck)

####################################################################
#################################################################### 
    if deck == 1:
        deckDir = baseDir + "/1on_the_rocks/"

        clear()
        print("On the rocks has been selected. Good choice! \n")
        while len(cards) > 0 and not(endOfRound):
            clear()
            printPoints()
            card = random.choice(cards)
            cards.remove(card)
            cardDir = deckDir + "(" + str(card) + ").pdf"

            subP = subprocess.Popen([reader, cardDir])

            # Decision for the first winner
            winner1 = input("Choose a winner for the first question \
(or type skip if necessary)\n \n")
            decision = False
            while not(decision):
                if winner1 == "Lisa":
                    Lisa += 1
                    decision = True
                elif winner1 == "Benni":
                    Benni += 1
                    decision = True
                elif winner1 == "Luca":
                    Luca += 1
                    decision = True
                elif winner1 == "skip":
                    print("Card has been skipped")
                    decision = True
                else:
                    winner1 = input("There seems to have been a typo. \
                                    Wanna try again? \n \n")


            # Decision for the second winner
            winner2 = input("Choose a winner for the second question \
(or type skip if necessary)\n \n")

            decision = False
               
            while not(decision):
                if winner2 == "Lisa":
                    Lisa += 1
                    decision = True
                elif winner2 == "Benni":
                    Benni += 1
                    decision = True
                elif winner2 == "Luca":
                    Luca += 1
                    decision = True
                elif winner2 == "skip":
                    print("Card has been skipped")
                    decision = True
                else:
                    winner2 = input("There seems to have been a typo. \
                                    Wanna try again? \n \n")
            
            subP.kill()
            if Benni >= 5:
                print("We have a victor! Congratulations Benni!")
                endOfRound = True
            if Lisa >= 5:
                print("We have a victor! Congratulations Lisa!")
                endOfRound = True
            if Luca >= 5:
                print("We have a victor! Congratulations Luca!")
                endOfRound = True

            if endOfRound:
                anotherRound()
####################################################################
####################################################################

                
####################################################################
#################################################################### 
    if deck == 2:
        deckDir = baseDir + "/2extra_dirty/"

        clear()
        print("Extra Dirty has been selected. Daring today, are we? \n")
        while len(cards) > 0 and not(endOfRound):
            clear()
            printPoints()
            card = random.choice(cards)
            cards.remove(card)
            cardDir = deckDir + "(" + str(card) + ").pdf"

            subP = subprocess.Popen([reader, cardDir])

            # Decision for the first winner
            winner1 = input("Choose a winner for the first question \
(or type skip if necessary)\n \n")
            decision = False

            while not(decision):
                if winner1 == "Lisa":
                    Lisa += 1
                    decision = True
                elif winner1 == "Benni":
                    Benni += 1
                    decision = True
                elif winner1 == "Luca":
                    Luca += 1
                    decision = True
                elif winner1 == "skip":
                    print("Card has been skipped")
                    decision = True
                else:
                    winner1 = input("There seems to have been a typo. \
                                    Wanna try again? \n \n")


            # Decision for the second winner
            winner2 = input("Choose a winner for the second question \
(or type skip if necessary)\n \n")

            decision = False
               
            while not(decision):
                if winner2 == "Lisa":
                    Lisa += 1
                    decision = True
                elif winner2 == "Benni":
                    Benni += 1
                    decision = True
                elif winner2 == "Luca":
                    Luca += 1
                    decision = True
                elif winner2 == "skip":
                    print("Card has been skipped")
                    decision = True
                else:
                    winner2 = input("There seems to have been a typo. \
                                    Wanna try again? \n \n")
            
            subP.kill()
            if Benni >= 5:
                print("We have a victor! Congratulations Benni!")
                endOfRound = True
            if Lisa >= 5:
                print("We have a victor! Congratulations Lisa!")
                endOfRound = True
            if Luca >= 5:
                print("We have a victor! Congratulations Luca!")
                endOfRound = True

            if endOfRound:
                anotherRound()
####################################################################
####################################################################


####################################################################
#################################################################### 
    if deck == 3:
        deckDir = baseDir + "/3happy_hour/"

        clear()
        print("Happy Hour has been selected. The safe choice. \
Why not feel good for a moment, right? \n")
        while len(cards) > 0 and not(endOfRound):
            clear()
            printPoints()
            card = random.choice(cards)
            cards.remove(card)
            cardDir = deckDir + "(" + str(card) + ").pdf"

            subP = subprocess.Popen([reader, cardDir])

            # Decision for the first winner
            winner1 = input("Choose a winner for the first question \
(or type skip if necessary)\n \n")
            decision = False

            while not(decision):
                if winner1 == "Lisa":
                    Lisa += 1
                    decision = True
                elif winner1 == "Benni":
                    Benni += 1
                    decision = True
                elif winner1 == "Luca":
                    Luca += 1
                    decision = True
                elif winner1 == "skip":
                    print("Card has been skipped")
                    decision = True
                else:
                    winner1 = input("There seems to have been a typo. \
                                    Wanna try again? \n \n")


            # Decision for the second winner
            winner2 = input("Choose a winner for the second question \
(or type skip if necessary)\n \n")

            decision = False
               
            while not(decision):
                if winner2 == "Lisa":
                    Lisa += 1
                    decision = True
                elif winner2 == "Benni":
                    Benni += 1
                    decision = True
                elif winner2 == "Luca":
                    Luca += 1
                    decision = True
                elif winner2 == "skip":
                    print("Card has been skipped")
                    decision = True
                else:
                    winner2 = input("There seems to have been a typo. \
                                    Wanna try again? \n \n")
            
            subP.kill()
            if Benni >= 5:
                print("We have a victor! Congratulations Benni!")
                endOfRound = True
            if Lisa >= 5:
                print("We have a victor! Congratulations Lisa!")
                endOfRound = True
            if Luca >= 5:
                print("We have a victor! Congratulations Luca!")
                endOfRound = True

            if endOfRound:
                anotherRound()
####################################################################
####################################################################

####################################################################
#################################################################### 
    if deck == 4:
        deckDir = baseDir + "/4last_call/"

        clear()
        print("Last Call has been selected. I see you have nothing \
left to lose... \n")
        while len(cards) > 0 and not(endOfRound):
            clear()
            printPoints()
            card = random.choice(cards)
            cards.remove(card)
            cardDir = deckDir + "(" + str(card) + ").pdf"

            subP = subprocess.Popen([reader, cardDir])

            # Decision for the first winner
            winner1 = input("Choose a winner for the first question \
(or type skip if necessary)\n \n")
            decision = False

            while not(decision):
                if winner1 == "Lisa":
                    Lisa += 1
                    decision = True
                elif winner1 == "Benni":
                    Benni += 1
                    decision = True
                elif winner1 == "Luca":
                    Luca += 1
                    decision = True
                elif winner1 == "skip":
                    print("Card has been skipped")
                    decision = True
                else:
                    winner1 = input("There seems to have been a typo. \
                                    Wanna try again? \n \n")


            # Decision for the second winner
            winner2 = input("Choose a winner for the second question \
(or type skip if necessary)\n \n")

            decision = False
               
            while not(decision):
                if winner2 == "Lisa":
                    Lisa += 1
                    decision = True
                elif winner2 == "Benni":
                    Benni += 1
                    decision = True
                elif winner2 == "Luca":
                    Luca += 1
                    decision = True
                elif winner2 == "skip":
                    print("Card has been skipped")
                    decision = True
                else:
                    winner2 = input("There seems to have been a typo. \
                                    Wanna try again? \n \n")
            
            subP.kill()
            if Benni >= 5:
                print("We have a victor! Congratulations Benni!")
                endOfRound = True
            if Lisa >= 5:
                print("We have a victor! Congratulations Lisa!")
                endOfRound = True
            if Luca >= 5:
                print("We have a victor! Congratulations Luca!")
                endOfRound = True

            if endOfRound:
                anotherRound()
####################################################################
####################################################################
