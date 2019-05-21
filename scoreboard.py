import pygame
pygame.init()

class Scoreboard(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player1scorefull = 0
        self.player2scorefull = 0
        self.player3scorefull = 0
        self.player4scorefull = 0



    def update(self):
        pass

    def score(self, player1pos, player2pos, player3pos, player4pos):
        player1score = 960 - player1pos
        player2score = 960 - player2pos
        player3score = 960 - player3pos
        player4score = 960 - player4pos

        self.player1scorefull += player1score
        self.player2scorefull += player2score
        self.player3scorefull += player3score
        self.player4scorefull += player4score


    def updateScores(self, player1pos, player2pos, player3pos, player4pos):
        print(player1pos, player2pos, player3pos, player4pos)
        print(self.player1scorefull, self.player2scorefull, self.player3scorefull, self.player4scorefull)
        self.score(player1pos, player2pos, player3pos, player4pos)
        self.drawscoreboard()

    def drawscoreboard(self):

        self.font = pygame.font.SysFont("Arial", 20)
        self.text = ("                                                                                                                                                               Player1: %d" % (self.player1scorefull    ))
        """" %d" \
                    "                                                  Player2: &d" \
                    "                                                  Player3: &d" \
        "                                                  Player4: &d" )% (self.player1scorefull, self.player2scorefull, self.player3scorefull, self.player4scorefull)"""
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()



        #display_surface.blit(scoretext, scorebox)



def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))

    scoreboard = Scoreboard()
    scoreboard.updateScores(10,101,10,10)
    #scoreboard.drawscoreboard()#***How to spawn a arrow left in***

    arrowrightstuff = pygame.sprite.Group(scoreboard)


    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False



        arrowrightstuff.clear(screen, background)                                #***Screen updaters for left arrows***
        arrowrightstuff.update()
        arrowrightstuff.draw(screen)



        pygame.display.flip()




if __name__ == "__main__":
    main()



