#!/usr/bin
#-*- coding:utf-8 -*-

import sys,pygame,time
import numpy as np
from pygame.locals import *

WIDTH = 80
HEIGHT = 60

pygame.button_down = False
pygame.clock_start = 0
pygame.world = np.zeros((HEIGHT,WIDTH))

class Cell(pygame.sprite.Sprite):
    size = 10

    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.size,self.size])
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.topleft = position

def draw():
    screen.fill((0,0,0))#重置画布
    for col in range(pygame.world.shape[1]):
        for row in range(pygame.world.shape[0]):
            if (pygame.world[row][col]):
                new_cell = Cell((col*Cell.size,row*Cell.size))
                screen.blit(new_cell.image,new_cell.rect)#绘制位图(image,initial position)

def next_generation():
    count = sum(np.roll(np.roll(pygame.world,i,0),j,1) for i in (-1,0,1) for j in (-1,0,1) if (i !=0 or j!=0))
    pygame.world =((count == 3) | ((pygame.world ==1) & (count == 2))).astype('int')

def init():
    pygame.world.fill(0)
    draw()
    return 'Stop'

def stop():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key  == K_RETURN:
            print('Move')
            return 'Move'

        if event.type == KEYDOWN and event.key  == K_r:
            return 'Reset'

        if event.type == MOUSEBUTTONDOWN:
            pygame.button_down = True
            pygame.button_type = event.button

        if event.type == MOUSEBUTTONUP:
            pygame.button_down = False

        if pygame.button_down:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = int(mouse_x / Cell.size)
            row = int(mouse_y / Cell.size)
            print(col,row)
            if pygame.button_type == 1:
                pygame.world[row][col] = 1
            elif pygame.button_type == 3:
                pygame.world[row][col] = 0
            draw()

    return 'Stop'

def move():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_SPACE:
            return 'Stop'

        if event.type == KEYDOWN and event.key == K_r:
            return 'Reset'

        if event.type == MOUSEBUTTONDOWN:
            pygame.button_down = True;
            pygame.button_type = event.button

        if event.type == MOUSEBUTTONUP:
            pygame.button_down = False
            
        if pygame.button_down:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            col = int(mouse_x/Cell.size)
            row = int(mouse_y/Cell.size)

            if pygame.button_type == 1:
                pygame.world[row][col] = 1
            elif pygame.button_type == 3:
                pygame.world[row][col] = 0
            draw()

    if time.clock() - pygame.clock_start > 0.02:
        next_generation()
        draw()
        pygame.clock_start = time.clock()

    return 'Move'

if __name__ == '__main__':
    state_actions = {
            'Reset':init,
            'Stop':stop,
            'Move':move
            }
    state = 'Reset'

    pygame.init()
    pygame.display.set_caption('Conway\'s Game of Life')

    screen = pygame.display.set_mode((WIDTH*Cell.size,HEIGHT*Cell.size))

    while True:
        state = state_actions[state]()
        pygame.display.update()
