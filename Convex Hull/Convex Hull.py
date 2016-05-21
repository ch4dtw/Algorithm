import pygame

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Convex Hull_D0240460")
    clock = pygame.time.Clock()
    font = pygame.font.Font("/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc", 36)

    while True:
        screen.fill(WHITE)
        pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    main()
