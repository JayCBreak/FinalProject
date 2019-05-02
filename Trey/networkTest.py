import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

def main():

    image = pygame.Surface((50,50))
    image.fill((36, 76, 0))

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0,0))
    screen.blit(image, (100,100))

    clock = pygame.time.Clock()
    keepGoing = True
    pygame.mouse.set_visible(True)

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        pygame.display.flip()
if __name__ == "__main__":
    main()
