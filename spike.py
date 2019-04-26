"""
Spike code:
When player touches spike they
will respawn at last checkpoint.
Hit box will be triangle.
"""

class spike():
    def __init__(self, x = 0 , y = 0):
        self.xcord = x
        self.ycord = y

    def drawspike(self):
        pygame.draw.polygon(screen, RED, (brickX, brickY, brickW, brickH), OUTLINE)
        spike = Image.open("spike")
