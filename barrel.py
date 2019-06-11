"""
Barrel code:
Simple fun code for pure
ascetics and visual design
to fill in any dead area.
"""

import pygame
pygame.init()

class Barrel(pygame.sprite.Sprite): #Fun code to place a barrel that doesn't have a hitbox

    def __init__(self, x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)

        width = 75
        height = 75

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/baRRelsmol.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.y = self.ycord

    def update(self):
        pass

#Code tester
def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))

    flag2 = Barrel(200, 200)
    flag1 = Barrel(275, 200)
    flag3 = Barrel(350,200)
    flagGroup = pygame.sprite.Group(flag1,flag2,flag3)


    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False



        flagGroup.update()
        flagGroup.draw(screen)



        pygame.display.flip()



if __name__ == "__main__":
    main()
