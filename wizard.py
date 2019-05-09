import pygame, sys
from pygame import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Wizard Movement')

#class Wizard(pygame.sprite.Sprite):

WIZARD_WIDTH = 50
WIZARD_HEIGHT = 50
wizardSpeedX = 0
wizardSpeedY= 0
p1Wizard = pygame.Rect(10, 430, WIZARD_WIDTH, WIZARD_HEIGHT)
WIZARD_COLOR = pygame.color.Color("red")

# clock object that will be used to make the game
# have the same speed on all machines regardless
# of the actual machine speed.
clock = pygame.time.Clock()

while True:
    # limit the demo to 50 frames per second
    clock.tick( 50 );

    # clear screen with black color
    screen.fill( (0,0,0) )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[K_a]:
        p1Wizard.left = p1Wizard.left + wizardSpeedX - 6

    if keys[K_d]:
        p1Wizard.right = p1Wizard.right + wizardSpeedX + 6

    if keys[K_w]:
        p1Wizard.top = p1Wizard.top + wizardSpeedY - 3


    # draw the wizard
    screen.fill( WIZARD_COLOR, p1Wizard );

    pygame.display.update()
