"""Game Development with Pygame
Wizard Tower Main Game code

by:
Trey Cowell
William Smith
Brandon Wabnitz
Jacob Chotenovsky

"""
import socket
import queue
import pygame as pg
from settings import *
from sprites import *
from spike import *
from threading import Thread
from scoreboard import Scoreboard

playerList = []
userFile = open("playerlist", "r")
username = userFile.read()
userFile.close()
wizColFile = open("wizCol", "r")
wizCol = wizColFile.read()
wizColFile.close()
defaultWiz = [username, wizCol, "20", "20", "0"]
dq = queue.Queue()
dq.put(defaultWiz)


class Game:
    def __init__(self, q):
        self.q = q
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.scoreboard = Scoreboard()



        self.image = pg.image.load("./images/Stonewall.jpg")
        self.image = pg.transform.scale(self.image, (900, 1000))
        self.screen.blit(self.image, (0, 0))


    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()    #creating a group for the wizards/ sprites/ and scoreboard
        self.platforms = pg.sprite.Group()
        self.scoreGroup = pg.sprite.Group()
        self.netWizGroup = pg.sprite.Group()

        self.player = Player(self)
        #self.player1 = Player1(self)
        #self.player2 = Player2(self)        #getting the specific wizards from sprites.py
        #self.player3 = Player3(self)
        self.netWiz = networkWiz(self)

        self.all_sprites.add(self.player)
        #self.all_sprites.add(self.player1)
        #self.all_sprites.add(self.player2)      #adding the sprites to the group
        #self.all_sprites.add(self.player3)
        self.netWizGroup.add(self.netWiz)



        for plat in PLATFORM_LIST:                     #Change levels by just changing ListValue
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)


        self.spikeHitboxes = pg.sprite.Group()                                  #SPIKES FOR LEVEL 3 ONLY!!
        self.drawSpike = pg.sprite.Group()

        for spike_coordinate in SPIKE_LIST: #Spikes just change ListValue
            (x,y) = spike_coordinate
            lespike = Spike(self.spikeHitboxes, self.drawSpike, x,y)


        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.drawAll()


    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        """if self.player1.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player1, self.platforms, False)
            if hits:
                self.player1.pos.y = hits[0].rect.top
                self.player1.vel.y = 0

        if self.player2.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player2, self.platforms, False)
            if hits:
                self.player2.pos.y = hits[0].rect.top
                self.player2.vel.y = 0

        if self.player3.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player3, self.platforms, False)
            if hits:
                self.player3.pos.y = hits[0].rect.top
                self.player3.vel.y = 0 """

    def events(self):
        global username
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                """
                playerlist = open("playerlist", "r")
                line = " "
                while line != "":
                    line = playerlist.readline()
                    #print (line)
                    if line != "":
                        lineList = line.split(";")
                        pname = lineList[0]
                        #print(pname)
                        #print ("The length is of the list", len(lineList))
                        #lineList[1].strip(['\n'])
                        ppos = lineList[1]
                        ppos.strip("\n")
                        playerList.append([pname, ppos])
                        #print(playerList)
                playerlist.close()
                playerlist = open("playerlist", "w")
                for player in playerList:
                    [pname, ppos] = player
                    if pname != username:
                        humanprofiles.write(pname + " ; " + ppos + " \n")
                playerlist.close()
                """
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player.jump()  #would put the jump animation here
                """if event.key == pg.K_t:
                    self.player1.jump()
                if event.key == pg.K_i:
                    self.player2.jump()
                if event.key == pg.K_UP:
                    self.player3.jump() """

    def drawAll(self):
        # Game Loop - draw

        global dq
        if dq.empty() is False:
            data = dq.get()
            self.netUsername = data[0]
            self.netwizardColour = data[1]          #Trying to draw wizards from across multiple screens
            self.netxCoords = data[2]
            self.netyCoords = data[3]
            self.netlevel = data[4]

        self.scoreboard.updateScores(self.player.pos.y)  #self.player1.pos.y, self.player2.pos.y, self.player3.pos.y
        self.scoreboard.drawscoreboard(self.screen, self.image)

        self.all_sprites.clear(self.screen,self.image)
        self.all_sprites.draw(self.screen)
        self.netWizGroup.clear(self.screen,self.image)
        self.netWizGroup.update(self.netxCoords, self.netyCoords, self.netwizardColour)
        self.netWizGroup.draw(self.screen)
        self.spikeHitboxes.update()
        self.drawSpike.update()

        self.spikeHitboxes.draw(self.screen)            #all this code clears, draws, and updates the sprites
        self.drawSpike.draw(self.screen)

        self.scoreboard.update()


        pg.display.flip()
        q.queue.clear()
        q.put(self.player.pos.x)
        q.put(self.player.pos.y)

    #spikedeath = pygame.sprite.spritecollide(spikeHitboxes, player)
    #if spikedeath:
     #   self.player.pos(450, 930)

    #arrowdeath = pygame.sprite.spritecollide(player, arrow)
    #if arrowdeath:


    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass


class ClientSend:
    def __init__(self, wizard="b", username="Bob"):
        self.w = wizard
        self.n = username
        self.x = -20
        self.y = -20
        self.level = 0
        host = 'gamertime.ddns.net'
        port = 8888
        self.mySocket = socket.socket()
        try:
            self.mySocket.connect((host, port))
            print("Connection Successful at: "+str(host)+":"+str(port))
        except:
            print("Unable to connect to server at: "+str(host)+":"+str(port))
            global s
            s = 0

    def send(self, level=0, q=queue.Queue()):
        self.x = q.get()
        self.y = q.get()
        self.level = level
        message = (str(self.n)+";"+str(self.w)+";"+str(self.x)+";"+str(self.y)+";"+str(self.level))
        #print("Sending message: "+message)
        try:
            self.mySocket.send(message.encode())
        except:
            print("Unable to send data to the Server.")
            exit()

        try:
            data = self.mySocket.recv(1024).decode()
            #print('Received from server: ' + data)
            data = data[2:-1]
            data = data.split(";")
            global dq
            dq.put(data)
        except:
            print("Unable to receive data from the Server.")
            exit()



def main(q=queue.Queue):
    g = Game(q)
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()

    pg.quit()


def network(wizard="b", username="bob", q=queue.Queue()):
    s = ClientSend(wizard, username)
    level = 0
    while True:
        s.send(level, q)

q = queue.Queue()

Thread(target=network, args=(wizCol, username, q)).start()


main(q)

"""
try:
    main(q)
except:
    print ("bad")"""
