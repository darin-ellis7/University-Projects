#Author: Darin Ellis
#Email: dmel227@g.uky.edu
#Section 014
#Purpose: To create a game of "roulette" where the user wagers in-game cash on bets
#on the outcome of the roll.
#Preconditions: All user inputs: number bet on, amount bet, the inputs for the side bets, whether to continue or not.
#Postconditions: How much the user won/lost, whether they want to continue, or a forced end.
#Date Completed: 11/9/14

from random import *
from graphics import *

#get_number_to_bet_on
#Purpose: this function will return the number the player wants to bet on, after validating it.
#Preconditions: none
#Postconditions: return a valid number representing the number that the player bet on.
def get_number_to_bet_on():
    number = int(input("What number do you want to bet on? 0-36 "))
    while(number > 36 or number < 0):
        if number > 36:
            print("That number is too high! Try again.")
            number = int(input("What number do you want to bet on? 0-36 "))
        if number < 0:
            print("That number is too low! Try again.")
            number = int(input("What number do you want to bet on? 0-36 "))            
    return number

#get_amount_to_bet
#Purpose: to receive, validate and return a user's bet.
#Preconditions: the amount in the user's pot, an int.
#Postconditions: a valid int representing the bet amount.
def get_amount_to_bet(p):
    bet = int(input("How much do you want to bet? "))
    while(bet > p or bet < 1):
        if bet > p:
            print("You don't have that much in your pot! Try again.")
        if bet < 1:
            print("You can't bet nothing or negatives! Try again.")
        bet = int(input("How much do you want to bet? "))
    return bet

#get_choice
#Purpose: to determine what the user wants to bet on.
#Preconditions: two characters, depending on which bet, and a string message to display for it.
#Postconditions: returns the choice
def get_choice(a, b, c):
    phrase = "Do you want to bet on " + c + " "
    choice = input(phrase)
    choice = choice.upper()
    while(choice != a and choice != b and choice != "N"):
        print("Bad input! Try again")
        choice = input(phrase)
        choice = choice.upper() 
    return choice

#get_randnum
#Purpose: to generate a random number for where the ball lands.
#Preconditions: none.
#Postconditions: a random int between 0-36
def get_randnum():
    random = randrange(0, 37)
    return random

#display_spin
#Purpose: to display the number that the ball landed on.
#Preconditions: the random integer determined by get_randnum.
#Postconditions: a graphics window
def display_spin(x):
    win = GraphWin("BIG BLUE ROULETTE", 550, 450)
    win.setCoords(0, 0, 550, 450)
    
    if x % 3 == 0:
        color1 = "red"
        color2 = "black"
    else:
        color1 = "black"
        color2 = "red"
    
    wheel = Circle(Point (275, -100), 500)
    wheel.draw(win)
    wheel.setFill("brown4")
    
    center = Polygon(Point(275, -50), Point(140, 375), Point(410, 375))
    center.draw(win)
    center.setFill(color1)
    
    left1_color = "black"
    left1 = Polygon(Point(275, -50), Point(-75, 250), Point(140, 375))
    left1.draw(win)
    left1.setFill(color2)
    
    left2 = Polygon(Point(275, -50), Point(-75, 250), Point(-5, -5))
    left2.draw(win)
    left2.setFill(color1)    
    
    right1 = Polygon(Point(275, -50), Point(625, 250), Point(410, 375))
    right1.draw(win)
    right1.setFill(color2)       

    right2 = Polygon(Point(275, -50), Point(625, 250), Point(555, -5))
    right2.draw(win)
    right2.setFill(color1)
    
    triangle = Polygon(Point(275, 350), Point(250, 425), Point(300, 425))
    triangle.draw(win)
    triangle.setFill("green")    
    
    cent_display = Text(Point(275, 300), x)
    cent_display.draw(win)
    cent_display.setFill("white")
    cent_display.setSize(30)
    cent_display.setStyle('bold')
    
    if x == 0:
        y = 36
    else:
        y = x - 1
    
    left_display = Text(Point(100, 225), y)
    left_display.draw(win)
    left_display.setFill("white")
    left_display.setSize(30)
    left_display.setStyle('bold')
    
    if x == 36:
        z = 0
    else:
        z = x +1

    right_display = Text(Point(450, 225), z)
    right_display.draw(win)
    right_display.setFill("white")
    right_display.setSize(30)
    right_display.setStyle('bold')
    
    click = Text(Point(450, 50), "Click to continue")
    click.draw(win)
    click.setFill("white")
    click.setSize(20)
            
    win.getMouse()
    win.close()    

#get_winnings
#Purpose: to calculate and return the changes in the player's pot.
#Preconditions: the number the player chose, the random number, the amount bet, and their choices from EON, RBN, and HLN.
#Postconditions: the amount of money won/lost (integer)
def get_winnings(number, random, bet, EON, RBN, HLN):
    main = 0
    first = 0
    second = 0
    third = 0
    if number == random:
        main = bet * 5
        print("You hit the number! You win 5 times your bet! $", main)
    else:
        main = 0
    if EON != "N":
        if random % 2 == 0:
            first_check = "E"
        else: 
            first_check = "O"
        if first_check == EON:
            first = bet * 2
            print("You won two times your bet on even/odd! +$", first)
        else:
            first = 0 - bet
            print("You lost your bet on even/odd! -$", abs(first))
    if RBN != "N":
        if random % 3 == 0:
            second_check = "R"
        else:
            second_check = "B"
        if second_check == RBN:
            second = bet * 3
            print("You won three times your bet on red/black! +$", second, sep="")
        else:
            second = 0 - (bet * 2)
            print("You lost two times your bet on red/black! -$", abs(second), sep="")
    if HLN != "N":
        if random > 18:
            third_check = "H"
        else:
            third_check = "L"
        if third_check == HLN:
            third = bet
            print("You won your bet on high/low! +$", third, sep="")
        else:
            third = 0 - bet
            print("You lost your bet on high/low! -$", abs(third), sep="")
            
    earnings = main + first + second + third
    return earnings

#get_y_or_n
#Purpose: to determine whether the user wants to continue or not.
#Preconditions: none.
#Postconditions: y or n (string)
def get_y_or_n():
    cont = input("Do you want to play again? (y/n) ")
    cont = cont.lower()
    while(cont != "y" and cont != "n"):
        print("Invalid input! Try again.")
        cont = input("Do you want to play again? (y/n) ")
        cont = cont.lower()
    return cont

#the main function
def main():
    pot = 100
    play_flag = True
    while(play_flag == True):
        print("Spin and Win! Big Blue Roulette!")
        print("Your pot is $", pot,". Good luck!", sep="")
        number = get_number_to_bet_on()
        bet = get_amount_to_bet(pot)
        EON = get_choice("E", "O", "even/odd/no bet? (E/O/N)")
        RBN = get_choice("R", "B", "red/black/no bet? (R/B/N)")
        HLN = get_choice("H", "L", "high/low/no bet? (H/L/N)")        
        random = get_randnum()    
        display_spin(random)
        print("")
        print("Spinning.......1..2..3..4...and the number is", random)
        print("")
        earnings = get_winnings(number, random, bet, EON, RBN, HLN)
        pot += earnings
        print("Your pot is now $", pot, sep="")
        print("")
        if pot <= 0:
            play_flag = False
            print("You ended with a pot amount of $", pot , ". You lose! Better luck next time!", sep="")
        else:
            cont = get_y_or_n()
            print("")
            if cont == "n":
                play_flag = False
                print("You chose to leave Big Blue Roulette with $", pot, "! Play again later!", sep="")
        print("")
        
main()
        
    
