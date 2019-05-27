import pygame
pygame.init()

class Checkpoint(pygame.sprite.Sprite):

    def __init__(self, x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)

        width = 75
        height = 75

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/Checkpoint Flag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.y = self.ycord

    def update(self):
        pass

def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))

                                   #***How to spawn a arrow left in***
    flag1 = Checkpoint(275, 200)
    flagGroup = pygame.sprite.Group(flag1)


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

