"""
Spike code:
When player touches spike they
will respawn at last checkpoint.
Hit box will be triangle.
"""
import pygame
pygame.init()



class Hitbox(pygame.sprite.Sprite):
    def __init__(self, x = 0 , y = 0, wid = 100, hei = 100):
        pygame.sprite.Sprite.__init__(self)
        self.width = wid
        self.height = hei

        self.xcord = x
        self.ycord = y

        self.image = pygame.Surface((wid,hei))
        #self.image.fill ((255,0,0))


        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.y = self.ycord



class Spike(pygame.sprite.Sprite):
    def __init__(self, group, groupDraw, x = 0 , y = 0):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        #self.group.add(self)
        groupDraw.add(self)
        width = 200
        height = 200

        self.xcord = x
        self.ycord = y

        self.image = pygame.image.load("./images/Spike.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.y = self.ycord

    def update(self):
        self.hitbox()

    def hitbox(self):
        self.hitbox1 = Hitbox(self.rect.x + 90, self.rect.y + 70, 60, 60)
        self.hitbox2 = Hitbox(self.rect.x + 30, self.rect.y + 140, 140, 60)
        self.hitbox3 = Hitbox(self.rect.x + 70, self.rect.y + 40, 50, 100)
        self.group.add(self.hitbox1)
        self.group.add(self.hitbox2)
        self.group.add(self.hitbox3)

        """self.rect = self.image.get_rect()
        self.hitbox = self.rect.inflate(-40, -20)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)
        self.offset = Vector2(10, 0)"""









def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))
    allSprites = pygame.sprite.Group()
    drawSpike = pygame.sprite.Group()
    lespike = Spike(allSprites, drawSpike, 100,100)




    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False



        allSprites.clear(screen, background)

        allSprites.update()
        drawSpike.update()

        drawSpike.draw(screen)
        allSprites.draw(screen)
        #drawSpike.draw(screen)
        pygame.display.flip()





if __name__ == "__main__":
    main()
