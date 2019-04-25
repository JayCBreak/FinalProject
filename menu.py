import pygame
import os
os.system("python arrow.py")
os.system("python checkpoint.py")
os.system("python floor.py")
os.system("python network.py")
os.system("python scoreboard.py")
os.system("python spike.py")
os.system("python wall.py")
os.system("python wizard.py")

screenWidth = 900
screenHeight = 1000
FPS = 60
imgBackground = ""
imgBtnPlay = "./images/play.png"
imgBtnCharacterChange = "./images/changeCharacter.png"
imgBtnTutorial = "./images/tutorial.png"
imgBtnNameSet = "./images/setName.png"
imgBtnScoreboard = "./images/scoreboard"
imgBtnExit = "./images/exit"


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
    btnPlay = Button(imgBtnPlay, 0, 0)
    btnCharacterChange = Button(imgBtnCharacterChange, 0, 0)
    btnTutorial = Button(imgBtnTutorial, 0, 0)
    btnNameSet = Button(imgBtnNameSet, 0, 0)
    btnScoreboard = Button(imgBtnScoreboard, 0, 0)
    btnExit = Button(imgBtnExit, 0, 0)
    allSprites = pygame.sprite.Group(btnPlay, btnCharacterChange, btnTutorial, btnNameSet, btnScoreboard, btnExit)
    background = pygame.image.load(imgBackground)
    screen.blit(background, (0, 0))

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.display.flip()
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the Wizard Tower!")
main()
