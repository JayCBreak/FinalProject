import pygame
pygame.init()


class Label(pygame.sprite.Sprite):

    def __init__(self, text="", posx=200, posy=100, colour=(0, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("./typewriter/TypewriterThin.otf", 35)
        self.text = text
        self.center = (posx, posy)
        self.background = (255, 255, 255)

    def update(self):
        #print (self.text)
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.background = (255, 255, 255)





class Scoreboard():

    def __init__(self):
        self.player1scorefull = 0
        self.player2scorefull = 0
        self.player3scorefull = 0
        self.player4scorefull = 0
        #self.lines = []
        self.labelList = []
        self.group = pygame.sprite.Group()
        self.start = True
        self.createscoreboard()



    def update(self):
        count = 0
        for label in self.labelList:
            label.text = self.textList[count]
            #print ("The value in the text list is ", self.textList[count])
            count +=1
        """print ("the size of thelist is", self.labelList)
        for item in self.labelList:
            print ("the tiemis ", item)
            item.update()"""

    def score(self, player1pos, player2pos, player3pos, player4pos):
        self.player1scorefull = 0
        self.player2scorefull = 0
        self.player3scorefull = 0
        self.player4scorefull = 0

        player1score = 960 - player1pos
        player2score = 960 - player2pos
        player3score = 960 - player3pos
        player4score = 960 - player4pos

        self.player1scorefull += player1score
        self.player2scorefull += player2score
        self.player3scorefull += player3score
        self.player4scorefull += player4score
        #print (self.player1scorefull)

        self.textList = ["Player1: %d"% self.player1scorefull,
                     "Player2: %d"% self.player2scorefull,
                     "Player3: %d"% self.player3scorefull,
                     "Player4: %d"% self.player4scorefull]

    def updateScores(self, player1pos, player2pos, player3pos, player4pos):
        #print(player1pos, player2pos, player3pos, player4pos)
        #self.lines = []

        self.score(player1pos, player2pos, player3pos, player4pos)
        #self.createscoreboard()

    def createscoreboard(self):

        self.font = pygame.font.Font("./typewriter/TypewriterThin.otf", 15)
        self.textList = ["Player1: %d"% self.player1scorefull,
                     "Player2: %d"% self.player2scorefull,
                     "Player3: %d"% self.player3scorefull,
                     "Player4: %d"% self.player4scorefull]
        yPos = 20
        self.labelList = []
        for lineOfText in (self.textList):
            label = Label(lineOfText, 800, yPos)
            yPos += 25
            self.labelList.append(label)

        #print ("the labels are ", self.labelList)
        """self.lines.append( self.font.render(self.text[0], 1, (0, 0, 0)))
        self.lines.append( self.font.render(self.text[1], 1, (0, 0, 0)))
        self.lines.append( self.font.render(self.text[2], 1, (0, 0, 0)))
        self.lines.append( self.font.render(self.text[3], 1, (0, 0, 0)))"""


    def drawscoreboard(self, screen,bricks):
        if self.start == True:
            self.group = pygame.sprite.Group()

            self.group.add(self.labelList)
            self.start = False
        #print ("When adding the labelst to the groupo", self.labelList)


        self.group.clear(screen,bricks)
        self.group.update()
        self.group.draw(screen)
        #print ("drawing scoreboard")
        """yPos = 10
        self.labelList = []
        for i in (self.lines):
            label = Label(i, 750, yPos)
            self.labelList.append(label)
            #screen.blit(i, (750,yPos))
            
            #label.update()
        print (self.labelList)"""




def main():
    screen = pygame.display.set_mode((900, 1000))



    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 0, 0))
    screen.blit(background, (0,0))

    scoreboard = Scoreboard()
    scoreboard.updateScores(960,843,629,305)




    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False


        #screen.blit(background, (0,0))
        #if scoreboard.start == True:
        scoreboard.drawscoreboard(screen, background)

        pygame.display.flip()


if __name__ == "__main__":
    main()



