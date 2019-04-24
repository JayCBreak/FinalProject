import pygame
import random
import game
import network
screenWidth = 900
screenHeight = 1000
FPS = 60


class Button(pygame.sprite.Sprite):
    def __init__(self, image = "", posx = 640, posy = 360, color = (255,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.center = (posx,posy)
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

def setup():
    global screenHeight, screenWidth, FPS, screen, clock
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Wizard Tower Menu")
    clock = pygame.time.Clock()
    main()

def main():
    global screenWidth, screenHeight, screen, clock
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.display.flip()
        

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the Wizard Tower!")
setup()
