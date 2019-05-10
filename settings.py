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
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40), #base floor
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 75, 75), #first platform
                 (125, HEIGHT - 350, 75, 75), #second platform was 100,20
                 (350, 200, 75,75), #second last platform was 100,20
                 (175, 100, 75, 75), #last platform was 100,20
                 (0,500,75,75), #third
                 (825,500,75,75),
                 (650,300,75,75)] #fourth
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
LIGHTGREY = (128,128,128)
DARKGREY = (169,169,169)
