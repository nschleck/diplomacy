import pygame, sys



pygame.init()

DISPLAY = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()
    pygame.display.update()
