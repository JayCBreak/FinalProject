import pygame
import random
import easygui
import subprocess
import webbrowser

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



 


class Button(pygame.sprite.Sprite):
    def __init__(self, image="", x=640, y=360, darkImage = "./images/dot.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.imageName = image
        self.darkIMage = darkImage
        self.center = (x, y)
        self.background = (0, 255, 255)
        self.mouse = pygame.mouse.get_pos()

    def update(self):
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


def main():
    global username, charModel
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Wizard Tower Menu")
    clock = pygame.time.Clock()
    sprTWizard = Button(imgSprTWizard, 320, 90, "./images/tWizard.png")
    sprTTower = Button(imgSPRTTower, 620, 240, "./images/tTower.png")
    btnPlay = Button(imgBtnPlay, 215, 480, "./images/darkplay.png")
    btnTutorial = Button(imgBtnTutorial, 200, 640, "./images/darktutorial.png")
    btnNameSet = Button(imgBtnNameSet, 200, 725, "./images/darksetName.png")
    btnCharacter = Button(imgBtnCharacter, 200, 810, "./images/darkcharacter.png")
    btnExit = Button(imgBtnExit, 200, 890, "./images/darkexit.png")
    secretdoor = Button(imgdoor, 669, 847, "./images/dooR.png")
    allSprites = pygame.sprite.Group(btnPlay, btnCharacter, btnTutorial, btnNameSet, btnExit, secretdoor, sprTWizard, sprTTower)
    background = pygame.image.load(imgBackground)
    screen.blit(background, (0, 0))

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btnPlay.click():
                    game("play")
                elif btnTutorial.click():
                    game("tutorial")
                elif btnNameSet.click():
                    game("nameSet")
                elif btnCharacter.click():
                    game("character")
                elif secretdoor.click():
                    counterfunny = 1
                    while counterfunny <= 50:
                        counterfunny += 1
                        print("Secret Door Discovered!!!")
                    webbrowser.open('https://www.youtube.com/watch?v=oHg5SJYRHA0')
                elif btnExit.click():
                    running = False
        pygame.display.flip()
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)


def game(play = "play"):
    global username, charModel
    if play == "play":
        if username is None:
            username = "player"
            playerlist = open ("playerlist", "w")
            playerlist.write(username + "\n")
            playerlist.close()
        else:
            pass
        subprocess.Popen("python game.py")
    elif play == "tutorial":
        print("This would play a video which would show the tutorial of how to play and how to move.")
        subprocess.Popen("python tutorial.py")
    elif play == "nameSet":

        username = easygui.enterbox("Please Enter your preferred Username.", "Set Your Username")
        if username is None:
            username = "player"
        else:
            username = username[:12]
        print("Thank you for setting your username to "+username+"!")

        playerlist = open ("playerlist", "w")
        playerlist.write(username + "\n")
        playerlist.close()
    elif play == "character":
        print("This would change the players character model.")
        charModel = easygui.buttonbox("Please choose your favorite wizard!", "Choose Your Character!", ["Pink", "White", "Green", "Purple"], image="./images/wizardSelect.png")



print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the Wizard Tower!\n\n\n\n\n\n\n\n")
main()
print("\n\nThank you for playing EpicGamer Co.'s Wizard Tower!\n\n")

