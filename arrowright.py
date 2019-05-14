import pygame
pygame.init()

class ArrowBlockRight(pygame.sprite.Sprite):

    def __init__(self, x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)

        width = 75
        height = 75

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/arrowblockrev.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.centery = self.ycord

    def update(self):
        pass
class ArrowRight(pygame.sprite.Sprite):

    def __init__(self,arrowBlockRightGroup , x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)

        self.arrowBlockRight = ArrowBlockRight(x,y)
        arrowBlockRightGroup.add(self.arrowBlockRight)

        width = 75
        height = 20

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/arrowrev.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord +70
        self.rect.centery = self.ycord

    def update(self):
        self.rect.centerx += 7
        if self.rect.x >= 900:
            self.rect.x = self.xcord +70
        #pass




"""
def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))

    arrowBlockRightGroup = pygame.sprite.Group()                                   #***How to spawn a arrow left in***
    arrow = ArrowRight(arrowBlockRightGroup , 275,200)
    arrow1 = ArrowRight(arrowBlockRightGroup , 100,300)
    arrow2 = ArrowRight(arrowBlockRightGroup , 400,600)
    arrow3 = ArrowRight(arrowBlockRightGroup , 0,900)
    arrowrightstuff = pygame.sprite.Group( arrow,arrow1, arrow2, arrow3)


    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False



        arrowrightstuff.clear(screen, background)                                #***Screen updaters for left arrows***
        arrowrightstuff.update()
        arrowBlockRightGroup.draw(screen)
        arrowrightstuff.draw(screen)



        pygame.display.flip()





if __name__ == "__main__":
    main()
"""
