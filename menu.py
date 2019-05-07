import pygame
import random
import easygui
import subprocess

screenWidth = 900
screenHeight = 1000
FPS = 60
randBackground = random.randint(0, 100)
if randBackground == 1:
    imgBackground = "./images/whatbackground.jpeg"
else:
    imgBackground = "./images/background.jpeg"
imgSprTWizard = "./images/tWizard.png"
imgSPRTTower = "./images/tTower.png"
imgBtnPlay = "./images/play.png"
imgBtnCharacter = "./images/character.png"
imgBtnTutorial = "./images/tutorial.png"
imgBtnNameSet = "./images/setName.png"
imgBtnScoreboard = "./images/scoreboard.png"
imgBtnExit = "./images/exit.png"





class Button(pygame.sprite.Sprite):
    def __init__(self, image="", x=640, y=360):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.center = (x,y)
        self.background = (0,255,255)
        self.mouse = pygame.mouse.get_pos()

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.mouse = pygame.mouse.get_pos()

    def click(self):
        # return true or false based on mouse over the button
        if self.rect.collidepoint(self.mouse):
            return True
        else:
            return False


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Wizard Tower Menu")
    clock = pygame.time.Clock()
    sprTWizard = Button(imgSprTWizard, 320, 90)
    sprTTower = Button(imgSPRTTower, 620, 240)
    btnPlay = Button(imgBtnPlay, 215, 415)
    btnTutorial = Button(imgBtnTutorial, 200, 555)
    btnNameSet = Button(imgBtnNameSet, 200, 640)
    btnCharacter = Button(imgBtnCharacter, 200, 725)
    btnScoreboard = Button(imgBtnScoreboard, 200, 805)
    btnExit = Button(imgBtnExit, 200, 890)
    allSprites = pygame.sprite.Group(btnPlay, btnCharacter, btnTutorial, btnNameSet, btnScoreboard, btnExit, sprTWizard, sprTTower)
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
                elif btnScoreboard.click():
                    game("scoreboard")
                elif btnExit.click():
                    running = False
        pygame.display.flip()
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

def game(play = "play"):
    if play == "play":
        subprocess.Popen("python game.py")
    elif play == "tutorial":
        print("This would play a video which would show the tutorial of how to play and how to move.")
        subprocess.Popen("python tutorial.py")
    elif play == "nameSet":
        username = easygui.enterbox("Please Enter your preferred Username.", "Set Your Username")
        print("Thank you for setting your username to "+username+"!")
    elif play == "character":
        print("This would change the players character model.")
        charModel = easygui.buttonbox("Please choose your favorite wizard!", "Choose Your Character!", ["Pink", "White", "Green", "Blue"], image="./images/wizardSelect.png")
    elif play == "scoreboard":
        subprocess.Popen("python scoreboard.py")


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the Wizard Tower!\n\n\n\n\n\n\n\n")
main()
print("\n\nThank you for playing EpicGamer Co.'s Wizard Tower!\n\n")
