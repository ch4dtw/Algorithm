import pygame
import random
import numpy as np

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
GRAY  = (192, 192, 192)

going = True
screen = clock = font = None
dot = []
start_x = 50
start_y = 50
grid = 500
dot_number = 100
dotline = []


class dots:
    def __init__(self):
        self.x = 0
        self.y = 0


def init():
    global screen,clock,font
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Convex Hull_D0240460")
    clock = pygame.time.Clock()
    font = pygame.font.Font("/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc", 36)
    clock = pygame.time.Clock()
    create_dot()


def draw():
    global screen, clock, font
    screen.fill(WHITE)
    screen.blit(font.render("FPS: {0:.2F}".format(clock.get_fps()), True, BLACK), (10, 10))
    pygame.draw.rect(screen, GRAY, [start_x, start_y, grid, grid], 0)
    draw_dot()
    pygame.display.update()


def drawline():
    pass


def create_dot():
    global dot, start_x, start_y
    for i in range(dot_number):
        temp = dots()
        temp.x = random.randint(0, grid)
        temp.y = random.randint(0, grid)
        dot.append(temp)
    pass


def draw_dot():
    global dot ,start_x ,start_y
    for i in range(dot_number):
        pygame.draw.circle(screen, BLACK, [dot[i].x+start_x, dot[i].y+start_y], 2)
    pass


def find_dot():
    global dot,screen
    leftmost = 0
    for i in range(dot_number):
        if leftmost < dot[i].x:
            leftmost = dot[i].y


if __name__ == '__main__':
    init()

    while going:
        draw()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif (e.type == pygame.KEYDOWN) and (e.key == pygame.K_RETURN):
                drawline()
        clock.tick(60)