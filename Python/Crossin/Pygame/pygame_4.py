# # -*- coding: utf-8 -*-
# import pygame
# from sys import exit
# pygame.init()
# screen = pygame.display.set_mode((1617, 640), 0, 32)
# pygame.display.set_caption("Hello World!")
# background = pygame.image.load("big_logo.png").convert()
# plane = pygame.image.load("plane.PNG").convert()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     screen.blit(background, (0, 0))
#
#     x, y = pygame.mouse.get_pos()
#     x -= plane.get_width() / 2
#     y -= plane.get_height() / 2
#     screen.blit(plane, (x, y))
#     pygame.display.update()

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1617, 640])
pygame.display.set_caption("Hello World!")
background = pygame.image.load("big_logo.png")
screen.blit(background, [0, 0])
clock = pygame.time.Clock()

class Plane(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

my_plane = Plane('plane.PNG', [10, 0])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            my_plane.rect.center = event.pos

    clock.tick(30)
    screen.blit(background,(0,0))
    screen.blit(my_plane.image, my_plane.rect)
    pygame.display.flip()