"""
This function file contains all of the program's functions and most of the variables
"""

###### usefull lines of code in this file to test bugs and you don't want to spam your spacebar too many times. (replace initialCost variable to a lower number to test for upgrades)

import pygame, sys,os, time
from pygame.locals import *
from fonts import *

# initial setup commands
# setting up pygame window
pygame.init()
screenWidth = 500
screenHeight = 600
window = pygame.display.set_mode((screenWidth, screenHeight))  # set resolution of the window 
screen = pygame.display.get_surface() 
pygame.display.set_caption('Goodluck to your spacebar') # title of program
gameIcon = pygame.image.load('images/icon.png')
pygame.display.set_icon(gameIcon)
# controls fps that the program runs
clock = pygame.time.Clock()
fps = 60

### variables
# color variables
white = [255, 255, 255]
brown = [69, 22, 0]
black = [0, 0, 0]
red = [255, 0, 0]

# image loading for the ui/game
# cookie's image
cookieImage = pygame.image.load("images/donut.png")
cookieImage_Two = pygame.image.load("images/donutTwo.png")
cookieImage_Three = pygame.image.load("images/donutThree.png")
cookieImage_Four = pygame.image.load("images/donutFour.png")
cookieImage_None = pygame.image.load("images/noDonut.png")
# backgrounds
menu_background = pygame.image.load("images/menuBackground.png")
game_background = pygame.image.load("images/gameBackground.png")
help_screen = pygame.image.load("images/help_screen.png")
# end game screen
end_game_background = pygame.image.load("images/endgamebackground.png")

# variables to control size of donut per click
donutSize = -1

# variables that track points
counter = -1
steps = 1

### programs functions
## menu functions
startingText = "Press spacebar to start"
middleTextValue = (len(startingText)*20//4 + 5)
helpTextOne = "Press H for Help"

# menu/start screen
def startScreen():
  # 'click your mouse to start' (text box)
  screen.blit(menu_background, (0,0))
  pygame.draw.rect(screen, white, (screenWidth//2 - middleTextValue - 10,screenHeight//2 - 30, 235, 65))
  screen.blit(fontMain.render(startingText, 1, (black)), (screenWidth//2 - middleTextValue,screenHeight//2 - 10))
  # help screen "H"
  screen.blit(fontMain.render(helpTextOne, 1, (white)), (screenWidth//2 - (len(helpTextOne)*20//4 + 5), screenHeight - 100))

## help screen function
def helpScreen():
  screen.blit(help_screen, (0,0))

## main game functions
# prints donut onto the screen (parameter determines the image of the donut)
sizeOriginal = 300
def donut(cookie):
  # cookie image for game
  screen.blit(cookie,(screenWidth/2 - sizeOriginal//2, screenHeight/3 - sizeOriginal//2))

# displays game's background
def gameBackground():
  # displays the background
  screen.blit(game_background, (-100, -300))

## points function
# function to print out the points/# of donut bites
counterText = "Donut Bites:"
def pointsDisplay(strCounter):
  # displays the text
  screen.blit(fontMain.render(counterText, 1, (brown)), (screenWidth//2 - (len(counterText)*20//4 + 5), 10))
  # displays the counter in string
  screen.blit(fontMain.render(strCounter, 1, (white)), (screenWidth//2 + (len(counterText) + 50), 10))

## Upgrades Functions
upgrades = "Upgrades"
def upgradeButton():
    pygame.draw.rect(screen, black, (screenWidth//2 - 150,400, 300, 50))
    screen.blit(fontMain.render("Upgrades", 1, (white)), (screenWidth//2 - (len("Upgrades")*20//4 + 5), 412))

# function to draw upgrades tab on screen
# initial cost of upgrades are the same for each
initialCost = 50
# variables for first upgrade
upgradeOne = [1, 2, initialCost]
# [0] = amount of upgrade 1 purchased 
# [1] = upgrade 1 effect (points multiplier per click)
# [2] = holds the cost of upgrade 1 starts as initial
upgradeOneText = "Press (1): 2x Multiplier:"

# variables for second upgrade
upgradeTwo = [1, 50, 1000]
# [0] = amount of upgrade 2 purchased
# [1] = upgrade 2 effect (amount of points gained per second)
# [2] = flat cost of upgrade 2
upgradeTwoText = "Press (2): {} points every second:".format(upgradeTwo[1])
# variables for end game
endGame = "Press (3) to beat the game:"
endGameCost = initialCost * 100000 # can lower this to test bugs for end game

def upgrades(upgradeTwo,upgradeOneValue, upgradeTwoValue, endGameValue):
  screen.blit(game_background, (-100, -300))
  # upgrades 1 text display
  screen.blit(fontMain.render(upgradeOneText, 1, (black)), (20, 50))
  screen.blit(fontMain.render(upgradeOneValue, 1, (white)), (400, 50))
  # upgrades 2 text display
  screen.blit(fontMain.render(upgradeTwoText, 1, (black)), (20, 125))
  screen.blit(fontMain.render(upgradeTwoValue, 1, (white)), (400, 125))
  # ends the game text displays
  screen.blit(fontMain.render(endGame, 1, (black)), (20, 200))
  screen.blit(fontMain.render(endGameValue, 1, (white)), (20, 250))
  # tells user how to go back to game screen
  screen.blit(fontMain.render("Press b to return to game screen", 1, (black)), (20, 325))

## end game screen function
gameOverText = "Congrats you beat donut clicker!"
lengthText = (len(gameOverText)*20//4 + 5)
def gameOver():
  screen.blit(end_game_background, (0,0))
  screen.blit(fontMain.render(gameOverText, 1, (red)), (screenWidth // 2 - lengthText, 10))
  
## previous run stats display
def previousRun():
  # opening the previous run's stats for display (this code was taken from in class list example)
  infile = open("previousRunStats.txt", "r") # r is for reading
  listlines = infile.readlines()    #read all the lines of the file into a list
  infile.close()
  for i in range(len(listlines)):
    # remove the newline character from the line
    cleanline = listlines[i].replace("\n","")
    #resave it at the same spot
    listlines[i] = cleanline
  previousRun = "Previous Run"
  previousCounter = ["Donut Bites:", listlines[0]]
  previousUpgrade1Level = ["Upgrade 1 Level:", listlines[1]]
  previousUpgrade2Level = ["Upgrade 2 Level:", listlines[2]]
  # displays background with header
  screen.blit(game_background, (-100, -300))
  screen.blit(fontMain.render(previousRun, 1, (black)), (20, 20))
  # displays previous donut bites (counter)
  screen.blit(fontMain.render(previousCounter[0], 1, (black)), (20, 70))
  screen.blit(fontMain.render(previousCounter[1], 1, (black)), (200, 70))
  # displays previous upgrade 1 level
  screen.blit(fontMain.render(previousUpgrade1Level[0], 1, (black)), (20, 100))
  screen.blit(fontMain.render(previousUpgrade1Level[1], 1, (black)), (200, 100))
  # displays previous upgrade 2 level
  screen.blit(fontMain.render(previousUpgrade2Level[0], 1, (black)), (20, 130))
  screen.blit(fontMain.render(previousUpgrade2Level[1], 1, (black)), (200, 130))