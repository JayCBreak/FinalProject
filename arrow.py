import pygame
pygame.init()

class ArrowBlock(pygame.sprite.Sprite):

    def __init__(self, x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)

        width = 75
        height = 75

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/arrowblock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.centery = self.ycord

    def update(self):
        pass
class Arrow(pygame.sprite.Sprite):

    def __init__(self,arrowBlockGroup , x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)

        self.arrowBlock = ArrowBlock(x,y)
        arrowBlockGroup.add(self.arrowBlock)

        width = 75
        height = 20

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/arrow.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord -70
        self.rect.centery = self.ycord

    def update(self):
        self.rect.centerx -= 7
        if self.rect.x <= -100:
            self.rect.x = self.xcord -70
        #pass





def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))

    arrowBlockGroup = pygame.sprite.Group()
    arrow = Arrow(arrowBlockGroup , 275,200)
    arrow1 = Arrow(arrowBlockGroup , 100,300)
    arrow2 = Arrow(arrowBlockGroup , 400,600)
    arrow3 = Arrow(arrowBlockGroup , 825,900)
    arrowstuff1 = pygame.sprite.Group( arrow,arrow1, arrow2, arrow3)



    """y_counter = 0
    arrowList = []
    for i in range (10):
        arrow =  Arrow(arrowBlockGroup , 275,0 + y_counter)
        y_counter = y_counter + 100
        arrowstuff1.add(arrow)"""



    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False



        arrowstuff1.clear(screen, background)
        arrowstuff1.update()
        arrowBlockGroup.draw(screen)
        arrowstuff1.draw(screen)



        pygame.display.flip()





if __name__ == "__main__":
    main()

