"""
Spike code:
When player touches spike they
will respawn at last checkpoint.
Hit box will be triangle.
"""
import pygame

class spike():
    def __init__(self, x = 0 , y = 0):
        width = 20
        height = 20

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("Spike.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()

    def drawspike(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Spike.png")
        self.rect = self.image.get_rect()
        self.reset()

    def hitbox(self):
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(-40, -20)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)
        self.offset = Vector2(10, 0)
