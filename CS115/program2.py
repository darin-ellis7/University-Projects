#Author: Darin Ellis
#Email: dmel227@g.uky.edu
#Section 014
#Purpose: To create a game determining whether the player's bird hit a 
#randomly-generated pig based on user-input velocity and angle.
#Date completed: 10/19/2014
#Preconditions: User-input number of rounds, difficulty, velocity, and angle.
#Postconditions: Calculated distance, height, positions of pictures calculated from
#angle/velocity, a psuedorandom location of one picture, and text messages,
#based on level of success.

from graphics import *
from math import *
from random import *

def main():
    
    #window settings
    win = GraphWin("ANGRY BIRDS!", 550, 450)
    win.setCoords(0, 0, 550, 450)
    
    #header
    header = Text(Point(275, 400), "Angry Birds!")
    header.setSize(30)
    header.setStyle('bold')
    header.draw(win)
    
    #input of rounds
    rdsPrompt = Text(Point(400, 350), "Number of rounds")
    rdsPrompt.draw(win)
    rdsBox = Entry(Point(500, 350), 4)
    rdsBox.draw(win)
    rdsBox.getText()
    win.getMouse()
    rds = rdsBox.getText()
    rdsBox.undraw()
    rdsFinal = Text(Point(500, 350), rds)
    rdsFinal.draw(win)
    
    #input of difficulty
    diffPrompt = Text(Point(400, 325), "Difficulty")
    diffPrompt.draw(win)
    diffBox = Entry(Point(500, 325), 4)
    diffBox.draw(win)
    diffBox.getText()
    win.getMouse()
    diff = diffBox.getText()
    diffBox.undraw()
    diffFinal = Text(Point(500, 325), diff)
    diffFinal.draw(win)
    
    #insert pics
    bird1 = Image(Point(30, 30), "angry.gif")
    bird1.draw(win)
    
    pig1 = Image(Point(520, 30), "pig.gif")
    pig1.draw(win)
    
    #points display
    points = Text(Point(260, 30), "Points")
    points.draw(win)
    pointTotal = 0
    pointDisp = Text(Point(300, 30), pointTotal)
    pointDisp.draw(win)

    #round display
    Round = Text(Point(50, 400), "Round")
    Round.draw(win)
    
    #convert rds to int so it can be used in the range
    rds = int(rds)
    
    #The Loop
    for i in range(1, rds + 1):
        #round number display
        rdsNum = Text(Point(80, 400), i)
        rdsNum.draw(win)
        
        #random pig location & display
        pigLoc = randrange(425, 526)
        pigText1 = Text(Point(50, 350), "Pig Location")
        pigText1.draw(win)
        pigText2 = Text(Point(120, 350), pigLoc)
        pigText2.draw(win)
        pig1.undraw()
        pig2 = Image(Point(pigLoc, 30), "pig.gif")
        pig2.draw(win)
        
        #velocity input
        veloPrompt = Text(Point(400, 300), "Velocity?")
        veloPrompt.draw(win)
        veloBox = Entry(Point(500, 300), 4)
        veloBox.draw(win)
        veloBox.getText()
        win.getMouse()
        velo = veloBox.getText()
        veloBox.undraw()
        veloFinal = Text(Point(500, 300), velo)
        veloFinal.draw(win)
        velo = float(velo)
        
        #angle input
        anglePrompt = Text(Point(400, 275), "Angle?")
        anglePrompt.draw(win)
        angleBox = Entry(Point(500, 275), 4)
        angleBox.draw(win)
        angleBox.getText()
        win.getMouse()
        angle = angleBox.getText()
        angleBox.undraw()
        angleFinal = Text(Point(500, 275), angle)
        angleFinal.draw(win)
        angle = float(angle)
        
        #convert from degrees to radians
        angle = (angle * pi) / 180
        
        #calculate height and display it
        height = (velo**2 * sin(angle)**2) / (2 * 9.8)
        height = int(round(height, 0))
        heightText1 = Text(Point(50, 325), "Height")
        heightText1.draw(win)
        heightText2 = Text(Point(100, 325), height)
        heightText2.draw(win)
        
        #calculate distance and display it
        distance = (velo**2 * sin(2* angle)) / 9.8
        distance = int(round(distance, 0))
        distanceText1 = Text(Point(50, 300), "Distance")
        distanceText1.draw(win)
        distanceText2 = Text(Point(110, 300), distance)
        distanceText2.draw(win)
        
        #more bird pics
        mid = distance / 2
        bird2 = Image(Point(mid, height), "angry.gif")
        bird2.draw(win)
        bird3 = Image(Point(distance, 30), "angry.gif")
        bird3.draw(win)
        
        #if/else for points
        diff = float(diff)
        check = abs(distance - pigLoc)
        if check <= diff:
            pointTotal = pointTotal + 1
            gotHim = Text(Point(75, 275), "You got him!")
            gotHim.draw(win)
        else:
            pointTotal = pointTotal
            gotHim = Text(Point(75, 275), "You missed him!")
            gotHim.draw(win)
        
        #update points display
        pointDisp.undraw()
        pointDisp = Text(Point(300, 30), pointTotal)
        pointDisp.draw(win)
    

        #pause
        cont = Text(Point(275, 200), "Click to continue")
        cont.setSize(20)
        cont.draw(win)
        win.getMouse()
        
        #undraw most things
        rdsNum.undraw()
        pigText2.undraw()
        pigText1.undraw()
        pig2.undraw()
        bird2.undraw()
        bird3.undraw()
        veloFinal.undraw()
        angleFinal.undraw()
        heightText2.undraw()
        distanceText2.undraw()
        gotHim.undraw()
        cont.undraw()
        distanceText1.undraw()
        heightText1.undraw()
        veloPrompt.undraw()
        anglePrompt.undraw()

    #final undraws
    bird1.undraw()
    Round.undraw()
    
    #farewell message depending on success
    if pointTotal == 0:
        score1 = Text(Point(240, 200), "You didn't get any pigs.")
        score1.draw(win)
        bye = Text(Point(275, 150), "Try again!")
        bye.draw(win)
        
    if pointTotal == 1:
        score1 = Text(Point(240, 200), "You got a pig.")
        score1.draw(win)
        bye = Text(Point(275, 150), "Thanks for playing!")
        bye.draw(win)
        
    if pointTotal > 1:
        score1 = Text(Point(240, 200), "You got")
        score1.draw(win)
        score2 = Text(Point(275, 200), pointTotal)
        score2.draw(win)
        score3 = Text(Point(305, 200), "pigs!")
        score3.draw(win)
        bye = Text(Point(275, 150), "Thanks for playing!")
        bye.draw(win)
    
    #close window
    win.getMouse()
    win.close()
    
main()
