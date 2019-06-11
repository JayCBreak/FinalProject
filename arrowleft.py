"""
Arrow code:
When player touches an arrow they
will respawn at last checkpoint.
Arrows will be moving across the screen.
"""

import pygame
pygame.init()

class ArrowBlockLeft(pygame.sprite.Sprite): #Code that creates the block which the arrow starts from

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
class ArrowLeft(pygame.sprite.Sprite): #Code for the moving arrow

    def __init__(self,arrowBlockLeftGroup , x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)

        self.arrowBlockLeft = ArrowBlockLeft(x,y)
        arrowBlockLeftGroup.add(self.arrowBlockLeft)

        width = 75
        height = 20

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/arrow.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord -70
        self.rect.centery = self.ycord

    def update(self): #Moving code for arrow
        self.rect.centerx -= 10
        if self.rect.x <= -100:
            self.rect.x = self.xcord -70
        #pass




#Testing Area for code
def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))

    arrowBlockLeftGroup = pygame.sprite.Group()                                   #***How to spawn a arrow left in***
    arrow = ArrowLeft(arrowBlockLeftGroup , 275,200)
    arrow1 = ArrowLeft(arrowBlockLeftGroup , 100,300)
    arrow2 = ArrowLeft(arrowBlockLeftGroup , 400,600)
    arrow3 = ArrowLeft(arrowBlockLeftGroup , 825,900)
    arrowleftstuff = pygame.sprite.Group( arrow,arrow1, arrow2, arrow3)


    #y_counter = 0
   # arrowList = []                                                             #Useless stuff please ignore
    #for i in range (10):
      #  arrow =  Arrow(arrowBlockGroup , 275,0 + y_counter)
      #  y_counter = y_counter + 100
       # arrowstuff1.add(arrow)



    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False



        arrowleftstuff.clear(screen, background)                                #***Screen updaters for left arrows***
        arrowleftstuff.update()
        arrowBlockLeftGroup.draw(screen)
        arrowleftstuff.draw(screen)



        pygame.display.flip()





if __name__ == "__main__":
    main()


