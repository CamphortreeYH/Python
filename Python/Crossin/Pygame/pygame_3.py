

# import pygame
# from sys import exit
# pygame.init()
# screen = pygame.display.set_mode((300, 80), 0 , 32)
# pygame.display.set_caption("Hello, World!")
# background = pygame.image.load("pygame_tiny.png").convert()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             background = pygame.image.load("logo_lofi.png").convert()
#     screen.blit(background, (0, 0))
#     pygame.display.update()

import pygame, sys

pygame.init()
screen = pygame.display.set_mode([300, 80])
screen.fill([255, 255, 255])
pygame.display.set_caption("Hello, World!")
background = pygame.image.load("pygame_tiny.png")
screen.blit(background, [50, 10])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, [255, 255, 255], [50, 10, 200, 60], 0)
            background = pygame.image.load("logo_lofi.png")
            screen.blit(background, [49, 10])
            pygame.display.flip()