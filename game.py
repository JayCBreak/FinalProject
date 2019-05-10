import pygame
import sys

screenWidth = 900
screenHeight = 1000
FPS = 60

class Character(pygame.sprite.Sprite):
    def __init__(self, wizard):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 500)) #Size of Sprite
        self.image = pygame.image.load("./images/"+wizard+"/Idle/tile000.png")
        self.rect = self.image.get_rect() #Insert Character sprites
        self.dx = 6
        self.dy = 6

    def update(self):
        self.move()
        self.wrap()

    def move(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_a]:
            self.rect.centerx -= self.dx
        if k[pygame.K_d]:
            self.rect.centerx += self.dx
        if k[pygame.K_w]:
            self.rect.centery -= self.dy
        if k[pygame.K_s]:
            self.rect.centery += self.dy

    def wrap(self):
        if self.rect.left > screen.get_width():
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = screen.get_width()
        if self.rect.top > screen.get_height():
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = screen.get_height()

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Wizard Tower Game")
    clock = pygame.time.Clock()
    wizard = Character("b")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        wizard.move()

    print("This would connect to the server which is running the game, sending the variable username, character and also send xy data.")


main()
