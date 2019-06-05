# game options/settings
TITLE = "Wizard Tower!"
WIDTH = 900
HEIGHT = 1000
FPS = 60

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.10
PLAYER_GRAV = 0.8

# Starting platforms (x,y,blockx,blocky)


SPIKE_LIST = []
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40), #base floor
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 75, 75), #first platform (was 100,20)
                 (175, HEIGHT - 400, 75, 75), #second platform
                 (0,500,75,75), #third
                 (825,500,75,75), #fourth
                 (650,300,75,75), #fifth
                 (350, 200, 75,75), #sixth
                 (175, 100, 75, 75), #seventh
                 (0,100,75,75)] #eighth

SPIKE_LIST1 = [(0,960),
              (75,960),
              (150,960),
              (225,960),
              (300,960),]
PLATFORM_LIST1 = [(350, HEIGHT - 40, 500, 40), #base floor SHOULD BE 150
                 (600, 750, 75, 75), #first platform
                 (800, 500, 75, 75), #second platform
                 (600,400,75,75), #third
                 (225,600,75,75), #fourth
                 (75,400,75,75), #fifth
                 (0, 200, 75,75), #sixth
                 (175, 100, 75, 75),#seventh
                 (250,100,75,75), #eight
                  (325,100,75,75), #nine
                  (750,75,75,75)] #final

SPIKE_LIST2 = [(525,200),
              (600,200)]
PLATFORM_LIST2 = [(0, HEIGHT - 40, WIDTH, 40), #base floor
                 (450, 750, 75, 75), #first platform
                 (175, 600, 75, 75), #second platform
                 (0,475,75,75), #third
                 (175,300,75,75), #fourth
                 (450,200,75,75), #fifth
                 (675, 200, 75,75), #sixth
                 (825, 100, 75, 75), #seventh
                 (0, 100, 75, 75)] #eighth

SPIKE_LIST3 = [(535,200),
              (615,200)]
PLATFORM_LIST3 = [(0, HEIGHT - 40, WIDTH, 40), #base floor
                 (350,750, 35, 35), #first platform
                 (125, HEIGHT - 400, 35, 35), #second platform
                 (0,500,35,35), #third
                 (795,500,35,35), #fourth
                 (630,300,35,35), #fifth
                 (350, 200, 35,35), #sixth
                 (175, 100, 35, 35)] #seventh






"""WALL_LIST = [(10, HEIGHT -100, WIDTH, 40),
             (WIDTH / 2 - 50, HEIGHT * 3 / 4, 75, 75),
             (125, HEIGHT - 400, 75, 75)]"""


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 255, 255)
PINK = (255,20,255)
LIGHTGREY = (128,128,128)
DARKGREY = (169,169,169)
PURPLE = (153,50,204)
