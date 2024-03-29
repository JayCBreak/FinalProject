# Sprite classes for platform game
"""Seperate to keep game.py as organized as possible
This file contains all of the wizards, their movement,
and """

import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite): #Pink Wizard
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 30))
        self.image.fill(PINK)
        wizColFile = open("wizCol","r")
        self.wizCol = wizColFile.read()
        wizColFile.close()
        self.image = pg.image.load("./images/"+self.wizCol+"/Idle/tile000.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 1) #spawns
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform, gravity
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self): #movement
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
            self.image = pg.image.load("./images/"+self.wizCol+"/Run/tile005LEFT.png")
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
            self.image = pg.image.load("./images/"+self.wizCol+"/Run/tile005.png")


        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos




"""class Player1(pg.sprite.Sprite): #Green Wizard
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 30))
        self.image.fill(GREEN)
        self.image = pg.image.load("./images/g/Idle/tile000.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH - 650, HEIGHT / 1)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform, gravity
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self): #movement
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_f]:
            self.acc.x = -PLAYER_ACC
            self.image = pg.image.load("./images/g/Run/tile005LEFT.png")
        if keys[pg.K_h]:
            self.acc.x = PLAYER_ACC
            self.image = pg.image.load("./images/g/Run/tile005.png")


        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos


class Player2(pg.sprite.Sprite): #White Wizard
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 30))
        self.image.fill(WHITE)
        self.image = pg.image.load("./images/w/Idle/tile000.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH - 200, HEIGHT / 1)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform, gravity
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self): #movement
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_j]:
            self.acc.x = -PLAYER_ACC
            self.image = pg.image.load("./images/w/Run/tile005LEFT.png")
        if keys[pg.K_l]:
            self.acc.x = PLAYER_ACC
            self.image = pg.image.load("./images/w/Run/tile005.png")


        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos



class Player3(pg.sprite.Sprite): #Purple/Blue Wizard
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 30))
        self.image.fill(PURPLE)
        self.image = pg.image.load("./images/b/Idle/tile000.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH - 100, HEIGHT / 1)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform, gravity
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self): #movement
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            self.image = pg.image.load("./images/b/Run/tile005LEFT.png")
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            self.image = pg.image.load("./images/b/Run/tile005.png")



        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos """


class networkWiz(pg.sprite.Sprite): #Network Wizard
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 30))
        self.image.fill(PURPLE)
        self.image = pg.image.load("./images/b/Idle/tile000.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH - 100, HEIGHT / 1)

    def update(self, xCoords, yCoords, wizCol): #movement
        self.pos.x = float(xCoords)
        self.pos.y = float(yCoords)
        self.image = pg.image.load("./images/"+wizCol+"/Idle/tile000.png")

        self.rect.midbottom = self.pos






class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(LIGHTGREY)
        self.image = pg.image.load("./images/Wood Block.png")
        self.image = pg.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Wall(pg.sprite.Sprite):
    def __int__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(DARKGREY)
        self.image = pg.image.load()
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 40
