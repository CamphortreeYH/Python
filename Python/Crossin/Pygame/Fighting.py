import pygame, sys
from random import *
pygame.init()
size = width, height = 450, 800
screen = pygame.display.set_mode(size)
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
            self.rect.bottom = 0

my_plane = Plane('plane.png', [10, 10])
planeGroup = pygame.sprite.Group(my_plane)
enemise = []
for i in range(5):
    location = [20*(randint(2, 20)), randint(-50, 100)]
    speed = [0, randint(1, 3)]
    my_enemy = Enemy('enemy.png', speed, location)
    enemise.append(my_enemy)

# bullets = []
# for i in range(5):
#     my_bullet = Bullet('bullet.png', [0, -5], [10, 10])
#     bullets.append(my_bullet)
my_bullet = Bullet('bullet.png', [0, -5], [10, 10])
bulletGroup = pygame.sprite.Group(my_bullet)
points = 0
font = pygame.font.Font(None, 50)
score_text = font.render(str(points), 1, (0, 0, 0))
textpos = [10, 10]
gameover = False
stopped = False
key = ''
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (key == pygame.K_n and gameover):
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            my_plane.rect.center = event.pos
            my_bullet.rect.centerx = event.pos[0]
            if my_bullet.rect.top <= 0:
                my_bullet.rect.centery = event.pos[1]
        elif event.type == pygame.KEYDOWN:
            if gameover:
                key = event.key
            else:
                key = ''
    screen.blit(background,(0,0))
    if not gameover:
        my_bullet.move()
        screen.blit(my_bullet.image, my_bullet.rect)
        # for bullet in bullets:
        #     bullet.move()
        #     screen.blit(bullet.image, bullet.rect)
        screen.blit(my_plane.image, my_plane.rect)
        for enemy in enemise:
            enemy.move()
            if pygame.sprite.spritecollide(enemy, bulletGroup, False):
                enemy.rect.bottom = 0
                points += 10
                font = pygame.font.Font(None, 50)
                score_text = font.render(str(points), 1, (0, 0, 0))

            if pygame.sprite.spritecollide(enemy, planeGroup, False):
                gameover = True
            screen.blit(score_text, textpos)
            screen.blit(enemy.image, enemy.rect)
    if gameover:
        final_text1 = "Game Over"
        final_text2 = "Your final score is : " + str(points)
        final_text3 = "Play again? (Y or N)"
        ft1_font = pygame.font.Font(None, 70)
        ft1_surf = font.render(final_text1, 1, (0, 0, 0))
        ft2_font = pygame.font.Font(None, 50)
        ft2_surf = font.render(final_text2, 1, (0, 0, 0))
        ft3_font = pygame.font.Font(None, 40)
        ft3_surf = font.render(final_text3, 1, (0, 0, 0))
        screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 200])
        screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 300])
        screen.blit(ft3_surf, [screen.get_width() / 2 - ft3_surf.get_width() / 2, 400])
        if key == pygame.K_y:
            points = 0
            score_text = font.render(str(points), 1, (0, 0, 0))
            pygame.time.delay(2000)
            gameover = False
            key = ''

    pygame.display.flip()
