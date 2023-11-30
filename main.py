"""
Final Assignment (Spacebar Breaker)
Joseph Leung
June 14, 2021
"""

from functions import *

### Controls
# spacebar - click the donut
# 1 - purchase upgrade 1
# 2 - purchase upgrade 2
# 3 - purchase upgrade 3
# b - go back from menus
# p - check previous run scores
# h - go to help screen (only on main menu)

# used for upgrade #2 (increases points by upgradeTwo[1] every second)
autoPoints = pygame.USEREVENT + 0
pygame.time.set_timer(autoPoints, 1000)

# variables to control the main loop
screen_change = "menu"
run = True
# main program loop starts here
while run == True:
  # code for displaying static background and donut for game screen
  if screen_change == "game":
    gameBackground()
    if donutSize == 0:
      donut(cookieImage)
    elif donutSize == 1:
      donut(cookieImage_Two)
    elif donutSize == 2:
      donut(cookieImage_Three)
    elif donutSize == 3:
      donut(cookieImage_Four)
    elif donutSize == 4:
      donut(cookieImage_None)
    # displays the counter and upgrade button 
    counterNumber = str(counter)
    pointsDisplay(counterNumber)
    upgradeButton()

  events = pygame.event.get()
  for event in events:
    # code for spacebar and mouse detection
    keys = pygame.key.get_pressed()
    mouseXY=pygame.mouse.get_pos()
    mx=mouseXY[0]
    my=mouseXY[1]
    mouseButton=pygame.mouse.get_pressed()
    # for debugging purposes
    print(steps, counter, upgradeOne[2], upgradeTwo[2], upgradeOne[1], upgradeTwo[1])

    # main menu screen (only shown at the start of program)
    if screen_change == "menu":
      startScreen()
      if keys[K_SPACE] == 1:
        screen_change = "game"
      elif keys[K_h] == 1:
        screen_change = "help"

    if screen_change == "help":
      helpScreen()
      if keys[K_b] == 1:
        screen_change = "menu"

    # main game screen
    if screen_change == "game":
      
      # this userevent checks for upgrade 2 and adds to score every second
      if upgradeTwo[0] > 1:
        if event.type == autoPoints:
          counter += upgradeTwo[1]
      # clicker program starts here
      if event.type == pygame.KEYDOWN: # this checks whether key is held or pressed once
        if event.key == pygame.K_SPACE:
          pressed_space = True
          if pressed_space == True:
            donutSize = donutSize + 1
            counter = counter + steps
            if donutSize == 0:
              donut(cookieImage)
            elif donutSize == 1:
              donut(cookieImage_Two)
            elif donutSize == 2:
              donut(cookieImage_Three)
            elif donutSize == 3:
              donut(cookieImage_Four)
            elif donutSize == 4:
              donut(cookieImage_None)
              donutSize = -1

      if keys[K_p]==1:
        screen_change = "previous run"

      # check for mouse click at certain range of x and y values depending on the upgrade box
      elif mouseButton[0] == 1:
          if mx>100 and mx<400 and my>400 and my<450 and screen_change == "game":
            screen_change = "upgrades"

    # previous run stats screen
    if screen_change == "previous run":
      previousRun()
      if keys[K_b]==1:
        screen_change = "game"

    # upgrades screen
    if screen_change == "upgrades":
      if upgradeTwo[0] > 1: # checks for upgrade 2 again because screen changed
        if event.type == autoPoints:
          counter += upgradeTwo[1]

      # for updating upgrade price
      # price scaling for upgrade 1
      # formula to scale with how many times purchased
      upgradeOne[2] = initialCost * upgradeOne[0] + ((upgradeOne[0] - 1) * 150) 
      upgradeOneValue = str(upgradeOne[2])
      endGameValue = str(endGameCost)

      # if statement to check if bought already or not because upgrade 2 is one time purchase
      if upgradeTwo[2] > 0:
        upgradeTwoValue = str(upgradeTwo[2])
      else:
        upgradeTwoValue = "OOS" # this means out of stock

      upgrades(upgradeTwo, upgradeOneValue, upgradeTwoValue, endGameValue)
      counterNumber = str(counter) 
      pointsDisplay(counterNumber)

      if keys[K_1]==1 and counter-upgradeOne[2]>=0: 
        # did it this way because it's annoying to spam the key for mass upgrade so you can hold down 1 for mass buy
        upgradeOne[0] += 1
        counter -= upgradeOne[2]
        steps = steps * upgradeOne[1]

      elif keys[K_2]==1 and counter-upgradeTwo[2]>=0 and upgradeTwo[0] == 1:
        # user can only purchase this once because it's too op
        upgradeTwo[0] += 1
        counter -= upgradeTwo[2]
        upgradeTwo[1] = (upgradeTwo[1] * upgradeTwo[0]) - upgradeTwo[1]
        upgradeTwo[2] = 0

      elif keys[K_3]==1 and counter-endGameCost>=0: # ends the game if purchased
        counter -= endGameCost
        screen_change = "endgame"

      elif keys[K_b]==1: # back button
        screen_change = "game"

    if event.type == pygame.QUIT:
      # saves current run into a file to display previous run next time the program is ran
      # code taken from in class example
      # first line is the counter, second line is upgrade 1 level, third line is upgrade 2 level (either 0 or 1)
      runEndStats = [str(counter), str(upgradeOne[0]-1), str(upgradeTwo[0]-1)]
      fileout = open("previousRunStats.txt", "w")
      for stat in runEndStats:
        fileout.write(stat+"\n")
      fileout.close()
      run = False
      print ("User exited the program")

  # displaying the end screen once the player purchases the third upgrade
  if screen_change == "endgame":
    gameOver()

  pygame.display.flip()
  clock.tick(fps)