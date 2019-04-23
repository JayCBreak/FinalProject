import pygame, random
screenWidth = 800
screenHeight = 400
FPS = 60

def setup():
    global screenHeight, screenWidth, FPS, screen
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Wizard Tower")
    clock = pygame.time.Clock()
    main()

def main():
    global screenWidth, screenHeight, screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.display.flip()

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the Wizard Tower!")
setup()
pygame.QUIT
