import pygame
import sys
import os
import math

pygame.init()

SCREEN_SIZE = 600
FPS = 50

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREY = (80, 80, 80)
BACKGROUND_COLOR = GREY
STAGE_posx = 0

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()

gravity = 10
PLAYER_SIZE = 40
PLAYER_VEL = 10

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

class thing:
    def __init__(self, posx, posy, velx, vely, size):
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely
        self.size = size

    def fall(self):
        if self.posy < SCREEN_SIZE - self.size:
            self.posy = self.posy + self.vely
        else:
            self.posy = SCREEN_SIZE - self.size

    def update_vel(self, grav):
        self.vely = self.vely + grav

class Background:
    def __init__(self, bglist, firstbg):
        self.loadedbg = []
        for bg in bglist:
            self.loadedbg.append(pygame.image.load(os.path.join(bg[0], bg[1])))

        self.currentbg = firstbg
        self.background_image = self.loadedbg[self.currentbg]
        self.bg_width, self.bg_height = self.background_image.get_rect().size

    def changebg(self, currentbg):
        self.currentbg = currentbg
        self.background_image = self.loadedbg[self.currentbg]
        self.bg_width, self.bg_height = self.background_image.get_rect().size

class floor:
    def __init__(self,posx, posy, size):
        pass

lvl_1_list = (('background\level_1','fondo0.png'),('background\level_1','fondo1.png'))
bg = Background(lvl_1_list, 0)

run = True
th1 = thing(SCREEN_SIZE/2, 0, PLAYER_VEL, 0, PLAYER_SIZE)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if th1.posy == (SCREEN_SIZE - th1.size):
            th1.posy = th1.posy - 1
            th1.vely = -15
    if keys[pygame.K_RIGHT]:
        if th1.posx < SCREEN_SIZE/2 - th1.size:
            th1.posx = th1.posx + th1.velx
        elif abs(STAGE_posx) + SCREEN_SIZE < bg.bg_width :
            STAGE_posx = STAGE_posx - th1.velx
        elif th1.posx < SCREEN_SIZE - th1.size:
            th1.posx = th1.posx + th1.velx
        else:
            th1.posx = SCREEN_SIZE - th1.size
    if keys[pygame.K_LEFT]:
        if th1.posx > 0:
            th1.posx = th1.posx - th1.velx
        else:
            th1.posx = 0

    if keys[pygame.K_s]:
        if bg.currentbg == 0 :
            bg.changebg(1)
        else:
            bg.changebg(0)


    clock.tick(FPS)

    screen.fill(BACKGROUND_COLOR)
    screen.blit(bg.background_image, (STAGE_posx, 0))

    pygame.draw.rect(screen, BLUE, (th1.posx, th1.posy, th1.size, th1.size))


    th1.fall()
    th1.update_vel(gravity / FPS)


    pygame.display.update()