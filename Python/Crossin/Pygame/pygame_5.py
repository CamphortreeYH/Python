# # -*- coding: utf-8 -*-
# import pygame
# from sys import exit
# pygame.init()
# screen = pygame.display.set_mode([450, 800], 0, 32)
# pygame.display.set_caption("Hello, World!")
# background = pygame.image.load("back.jpg").convert()
# plane = pygame.image.load("plane.png").convert_alpha()
# bullet = pygame.image.load("bullet.png").convert_alpha()
# bullet_x = 0
# bullet_y = -1
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     screen.blit(background, (0, 0))
#     x, y = pygame.mouse.get_pos()
#     if bullet_y < 0:
#         bullet_x = x - bullet.get_width() / 2
#         bullet_y = y - bullet.get_height() / 2
#     else:
#         bullet_y -= 5
#     screen.blit(bullet, (bullet_x, bullet_y))
#     x -= plane.get_width() / 2
#     y -= plane.get_height() / 2
#     screen.blit(plane, (x, y))
#     pygame.display.update()

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([450, 800])
pygame.display.set_caption("Hello World!")
background = pygame.image.load("back.jpg")
screen.blit(background, [0, 0])
clock = pygame.time.Clock()

class Plane(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)


my_plane = Plane('plane.png', [10, 10])
my_bullet = Bullet('bullet.png', [0, -5], [10, 10])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            my_plane.rect.center = event.pos
            my_bullet.rect.centerx = event.pos[0]
            if my_bullet.rect.top <= 0:
                my_bullet.rect.centery = event.pos[1]


    clock.tick(30)
    screen.blit(background,(0,0))
    my_bullet.move()
    screen.blit(my_bullet.image, my_bullet.rect)
    screen.blit(my_plane.image, my_plane.rect)
    pygame.display.flip()