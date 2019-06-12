"""Wizard Tower Menu
This code helps the user navigate the different sections of code and helps customize the characters to the players content.
It also helps introduce how to play the game and the different concepts.
"""
# import the various modules used
import pygame
import random
import easygui
import subprocess
import webbrowser
# setup variables to help draw pictures and establish screen size
screenWidth = 900
screenHeight = 1000
FPS = 60
randBackground = random.randint(0, 100)
if randBackground == 1:
    imgBackground = "./images/WizardTowerArm.png"
else:
    imgBackground = "./images/WizardTower.png"
imgSprTWizard = "./images/tWizard.png"
imgSPRTTower = "./images/tTower.png"
imgBtnPlay = "./images/play.png"
imgBtnCharacter = "./images/character.png"
imgBtnTutorial = "./images/tutorial.png"
imgBtnNameSet = "./images/setName.png"
imgBtnExit = "./images/exit.png"
imgdoor = "./images/dooR.png"
username = None

# Button class used to draw out the various buttons used
class Button(pygame.sprite.Sprite):
    def __init__(self, image="", x=640, y=360, darkImage = "./images/dot.png"): # initalize the class
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)  # setup variables, load images, get mouse pos, draw
        self.imageName = image
        self.darkIMage = darkImage
        self.center = (x, y)
        self.background = (0, 255, 255)
        self.mouse = pygame.mouse.get_pos()

    def update(self): # this function updates the image and allows the buttons to be pushed
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.mouse = pygame.mouse.get_pos()
        self.hover()

    def click(self):
        # return true or false based on mouse over the button
        if self.rect.collidepoint(self.mouse):
            return True
        else:
            return False

    def hover(self):
        # return true or false based on mouse over the button
        if self.rect.collidepoint(self.mouse):
            self.image = pygame.image.load(self.darkIMage)
        else:
            self.image = pygame.image.load(self.imageName)


def main(): # starts the code
    global username, charModel # gets global variables for username and character models
    pygame.init() # this initalizes pygame, mixer and makes a screen
    pygame.mixer.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Wizard Tower Menu")
    clock = pygame.time.Clock()
    sprTWizard = Button(imgSprTWizard, 320, 90, "./images/tWizard.png") # this section of code loads in all the buttons
    sprTTower = Button(imgSPRTTower, 620, 240, "./images/tTower.png")
    btnPlay = Button(imgBtnPlay, 215, 480, "./images/darkplay.png")
    btnTutorial = Button(imgBtnTutorial, 200, 640, "./images/darktutorial.png")
    btnNameSet = Button(imgBtnNameSet, 200, 725, "./images/darksetName.png")
    btnCharacter = Button(imgBtnCharacter, 200, 810, "./images/darkcharacter.png")
    btnExit = Button(imgBtnExit, 200, 890, "./images/darkexit.png")
    secretdoor = Button(imgdoor, 669, 847, "./images/dooR.png")
    allSprites = pygame.sprite.Group(btnPlay, btnCharacter, btnTutorial, btnNameSet, btnExit, secretdoor, sprTWizard, sprTTower)
    background = pygame.image.load(imgBackground)   # loads the background and blits it
    screen.blit(background, (0, 0))
    pygame.mixer.music.load('./sounds/Stand Proud and End of the World 8 - bit NES Remix.ogg')
    pygame.mixer.music.play(-1)

    running = True
    while running: # begins the running loop
        clock.tick(FPS)
        for event in pygame.event.get(): # checks for an event to occur and does the action that suites it
            if event.type == pygame.QUIT: # if quit then it quits
                running = False
                pygame.mixer.music.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # button pushed runs the appropriate code
                if btnPlay.click():
                    game("play")
                elif btnTutorial.click():
                    game("tutorial")
                elif btnNameSet.click():
                    game("nameSet")
                elif btnCharacter.click():
                    game("character")
                elif secretdoor.click(): # funny easter egg
                    counterfunny = 1
                    while counterfunny <= 50:
                        counterfunny += 1
                        print("Secret Door Discovered!!!")
                    webbrowser.open('https://www.youtube.com/watch?v=oHg5SJYRHA0')
                elif btnExit.click():
                    running = False
                    pygame.mixer.music.stop()
        pygame.display.flip() # flips the display, clears, updates and draws all the sprites
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)


def game(play="play"):  # defines the game and allows for the appropriate code to be run based on the button hit
    global username, charModel  # imports global usernames
    if play == "play":  # Runs game.py which is the game
        if username is None:
            username = "player"
            playerlist = open ("playerlist", "w")
            playerlist.write(username + "\n")
            playerlist.close()
        subprocess.Popen("python game.py")
    elif play == "tutorial": # Runs the code to explain how to play
        print("Use WASD to move and jump! The higher you get the better!")
    elif play == "nameSet": # allows the user to set a custom username
        username = easygui.enterbox("Please Enter your preferred Username.", "Set Your Username")
        if username is None:
            username = "player"
        else:
            username = username[:12]
        print("Thank you for setting your username to "+username+"!")
        playerlist = open ("playerlist", "w")
        playerlist.write(username + "\n")
        playerlist.close()
    elif play == "character": # Allows the user to change wizard colour
        charModel = easygui.buttonbox("Please choose your favorite wizard!", "Choose Your Character!", ["Pink", "White", "Green", "Blue"], image="./images/wizardSelect.png")
        if charModel == "Pink":
            charModel = "p"
        elif charModel == "White":
            charModel = "w"
        elif charModel == "Green":
            charModel = "g"
        elif charModel == "Blue":
            charModel = "b"
        wizCol = open("wizCol", "w")
        wizCol.write(charModel)
        wizCol.close()

# welcomes the user and says goodbye to the user while running the menu inbetween
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the Wizard Tower!\n\n\n\n\n\n\n\n")
main()
print("\n\nThank you for playing EpicGamer Co.'s Wizard Tower!\n\n")
