import pygame, sys

pygame.init()
screen = pygame.display.set_mode([300, 80])
screen.fill([0, 0, 0])
pygame.display.set_caption("Hello, World!")
background = pygame.image.load("pygame_tiny.png")
screen.blit(background, [50, 10])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()