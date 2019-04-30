import pygame
import os
import easygui
os.system("python arrow.py")
os.system("python checkpoint.py")
os.system("python floor.py")
os.system("python game.py")
os.system("python network.py")
os.system("python scoreboard.py")
os.system("python spike.py")
os.system("python tutorial.py")
os.system("python wall.py")
os.system("python wizard.py")

screenWidth = 900
screenHeight = 1000
FPS = 60
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
    def __init__(self, image = "", x = 640, y = 360):
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
        pygame.display.flip()
        pygame.mouse.set_visible(True)

def game(play = "play"):
    if play == "play":
        print("This would connect to the server which is running the game, sending the variable username, and character.")
    elif play == "tutorial":
        print("This would play a video which would show the tutorial of how to play and how to move.")
    elif play == "nameSet":
        username = easygui.enterbox("Please Enter your preferred Username.", "Set Your Username")
    elif play == "character":
        print("This would change the players character model.")
        charModel = easygui.buttonbox("Please choose your favorite wizard!", "Choose Your Character!", ["Pink", "White", "Green", "Blue"], image="./images/wizardSelect.png")
    elif play == "scoreboard":
        print("This would ping the server for a file which hosts the top players.")


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the Wizard Tower!\n\n\n\n\n\n\n\n")
main()
print("\n\nThank you for playing EpicGamer Co.'s Wizard Tower!\n\n")
