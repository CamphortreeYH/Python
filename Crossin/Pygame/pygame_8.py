# -*- coding: utf-8 -*-
import pygame
import random
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load("bullet.png").convert_alpha()
        self.active = False
        print "Bullet_init"

    def move(self):
        if self.active:
            self.y -= 3
            print "bullet_y", self.y
        if self.y < 0:
            self.active = False
            print "bullet_y", self.y

    def restart(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width() / 2
        self.y = mouseY - self.image.get_height() / 2
        self.active = True
        print "Bullet_Restart"


class Enemy:
    def restart(self):
        self.x = random.randint(50, 400)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + 0.1

    def __init__(self):
        self.restart()
        self.image = pygame.image.load("enemy.png").convert_alpha()

    def move(self):
        if self.y < 800:
            self.y += self.speed
        else:
            self.restart()


pygame.init()
screen = pygame.display.set_mode((450, 800), 0, 32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load("back.jpg").convert()
plane = pygame.image.load("plane.png").convert_alpha()
bullets = []
for i in range(5):
    bullets.append(Bullet())

count_b =len(bullets)
index_b = 0
interval_b = 0
enemy = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    interval_b -= 1
    print "interval_b:", interval_b
    if interval_b < 0:
        bullets[index_b].restart()
        interval_b = 100
        index_b = (index_b + 1) % count_b
    for b in bullets:
        print "b.index:", bullets.index(b)
        if b.active:
            print "b.active:", b.active
            b.move()
            screen.blit(b.image, (b.x, b.y))
    enemy.move()
    screen.blit(enemy.image, (enemy.x, enemy.y))
    x, y = pygame.mouse.get_pos()
    x -= plane.get_width() / 2
    y -= plane.get_height() / 2
    screen.blit(plane, (x, y))
    pygame.display.update()


# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([450, 800])
# pygame.display.set_caption("Hello World!")
# background = pygame.image.load("back.jpg")
# screen.blit(background, [0, 0])
# clock = pygame.time.Clock()
#
# class Plane(pygame.sprite.Sprite):
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, image_file, speed, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#         self.speed = speed
#
#     def move(self):
#         self.rect = self.rect.move(self.speed)
#
#
# my_plane = Plane('plane.png', [10, 10])
# my_bullet = Bullet('bullet.png', [0, -5], [10, 10])
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.MOUSEMOTION:
#             my_plane.rect.center = event.pos
#             my_bullet.rect.centerx = event.pos[0]
#             if my_bullet.rect.top <= 0:
#                 my_bullet.rect.centery = event.pos[1]
#
#
#     clock.tick(30)
#     screen.blit(background,(0,0))
#     my_bullet.move()
#     screen.blit(my_bullet.image, my_bullet.rect)
#     screen.blit(my_plane.image, my_plane.rect)
#     pygame.display.flip()