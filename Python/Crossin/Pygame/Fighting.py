import pygame, sys
pygame.init()
size = width, height = 450, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello World!")
background = pygame.image.load("back.jpg")
screen.blit(background, [0, 0])
# clock = pygame.time.Clock()

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.bottom > height:
            self.speed[1] = 0

my_plane = Plane('plane.png', [10, 10])
my_bullet = Bullet('bullet.png', [0, -5], [10, 10])
my_enemy = Enemy('enemy.png', [0, 3], [200, -50])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            my_plane.rect.center = event.pos
            my_bullet.rect.centerx = event.pos[0]
            if my_bullet.rect.top <= 0:
                my_bullet.rect.centery = event.pos[1]


    # clock.tick(30)
    screen.blit(background,(0,0))
    my_bullet.move()
    screen.blit(my_bullet.image, my_bullet.rect)
    screen.blit(my_plane.image, my_plane.rect)
    my_enemy.move()
    screen.blit(my_enemy.image, my_enemy.rect)
    pygame.display.flip()