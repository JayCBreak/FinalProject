"""
Barrel...
"""
import pygame
pygame.init()


class Barrel(pygame.sprite.Sprite):
    def __init__(self, group, x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        width = 75
        height = 75

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/baRRel.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.y = self.ycord




def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))

    #spikeHitboxes = pygame.sprite.Group()                                  #***Groups needed in main***
    drawbarrel = pygame.sprite.Group()

    lebarrel = Barrel(drawbarrel, 200,200)                     #***Code to summon spikes***





    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False



        drawbarrel.update()
        drawbarrel.draw(screen)


        pygame.display.flip()





if __name__ == "__main__":
    main()

