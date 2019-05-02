import pygame
pygame.init()

class ArrowBlock(pygame.sprite.Sprite):

    def __init__(self, group, groupDraw, x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        #self.group.add(self)
        groupDraw.add(self)
        width = 75
        height = 75

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/arrowblock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.y = self.ycord

class Arrow(pygame.sprite.Sprite):

    def __init__(self, group, groupDraw, x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        #self.group.add(self)
        groupDraw.add(self)
        width = 75
        height = 75

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/arrow.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.y = self.ycord



"""

def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))

    spikeHitboxes = pygame.sprite.Group()                                  #***Groups needed in main***
    drawSpike = pygame.sprite.Group()

    lespike = Spike(spikeHitboxes, drawSpike, 275,200)                     #***Code to summon spikes***
    mespike = Spike(spikeHitboxes, drawSpike, 200,200)
    kespike = Spike(spikeHitboxes, drawSpike, 350,200)
    sespike = Spike(spikeHitboxes, drawSpike, 425 ,200)
    hespike = Spike(spikeHitboxes, drawSpike, 500,200)




    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False



        spikeHitboxes.clear(screen, background)                          #***Updaters needed for spikes***

        spikeHitboxes.update()
        drawSpike.update()

        spikeHitboxes.draw(screen)
        drawSpike.draw(screen)


        pygame.display.flip()





if __name__ == "__main__":
    main()
"""
