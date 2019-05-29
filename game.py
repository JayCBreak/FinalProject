"""Game Development with Pygame
Wizard Tower Main Game code

by:
Trey Cowell
Will Smith
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
from time import sleep
from scoreboard import Scoreboard


class Game:
    def __init__(self, q):
        self.q = q
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        ###self.background = pg.image.load("./images/Stone Brick.png")
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.scoreboard = Scoreboard()

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        """self.walls = pg.sprite.Group()"""
        self.player = Player(self)
        self.player1 = Player1(self)
        self.player2 = Player2(self)
        self.player3 = Player3(self)

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player1)
        self.all_sprites.add(self.player2)
        self.all_sprites.add(self.player3)



        for plat in PLATFORM_LIST3: #Levels just change ListValue
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        """for wall in WALL_LIST:
            wa = Wall(*wall)
            self.all_sprites.add(wa)
            self.walls.add(wa)"""


        self.spikeHitboxes = pg.sprite.Group()                                  #SPIKES FOR LEVEL 3 ONLY!!
        self.drawSpike = pg.sprite.Group()

        for spike_coordinate in SPIKE_LIST2: #Spikes just change ListValue
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
                            #print ("All sprites", self.all_sprites)    TESTING TO SEE HOW MANY
                            #print ("hit spickess", self.spikeHitboxes) SPIKES HAVE BEEN DRAWN
                            #print ("spikes", self.drawSpike)

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        if self.player1.vel.y > 0:
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
                self.player3.vel.y = 0

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player.jump() #put the jump animation here
                if event.key == pg.K_t:
                    self.player1.jump()
                if event.key == pg.K_i:
                    self.player2.jump()
                if event.key == pg.K_UP:
                    self.player3.jump()

    def drawAll(self):
        # Game Loop - draw
        self.scoreboard.updateScores(self.player.pos.y, self.player1.pos.y, self.player2.pos.y, self.player3.pos.y)
        self.screen.fill(DARKGREY)
        """self.background.drawbackground(self.screen)
        width = 900
        height = 1000
        #self.image = pg.image.load("./images/Stone Brick.png")
        #self.image = pg.transform.scale(self.image,(width,height))"""




        self.all_sprites.draw(self.screen)
        self.scoreboard.drawscoreboard(self.screen)

        self.spikeHitboxes.update()
        self.drawSpike.update()

        self.spikeHitboxes.draw(self.screen)
        self.drawSpike.draw(self.screen)



        pg.display.flip()
        send = 0
        send += 1
        if send % 10 == 0:
            q.queue.clear()
            q.put(self.player.pos.x)
            q.put(self.player.pos.y)


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

    def send(self, level=0, q=queue.Queue()):
        sleep(0.05)
        self.x = q.get()
        self.y = q.get()
        self.level = level
        message = str([self.n, self.w,  self.x, self.y, self.level])
        print("Sending message: "+message)
        self.mySocket.send(message.encode())
        data = self.mySocket.recv(1024).decode()
        print('Received from server: ' + data)


def main(q=queue.Queue):
    g = Game(q)
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()

    pg.quit()


def network(wizard="b", username="bob", q=queue.Queue()):
    s = ClientSend(wizard, username)
    if s != 0:
        level = 0
        while True:
            s.send(level, q)

q = queue.Queue()

Thread(target=network, args=("Wizard", "Username", q)).start()

main(q)
