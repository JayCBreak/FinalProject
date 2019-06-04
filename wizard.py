import pygame

class drawPlayers(pygame.sprite.Sprite):
    if wizardColour == ("p"):
        otherplayer = Player()
    elif wizardColour == ("g"):
        otherplayer = Player1()
    elif wizardColour == ("w"):
        otherplayer = Player2()
    elif wizardColour == ("b"):
        otherplayer = Player3()
    while True:
        otherplayer.pos(xcoords, ycoords)
