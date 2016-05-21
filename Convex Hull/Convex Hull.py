import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Convex Hull演算法作業D0240460")
    clock = pygame.time.Clock()
    font = pygame.font.Font("/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc", 36)

    going = True
    while going:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                going = False

        screen.fill((0, 0, 0))
        screen.blit(font.render(str(clock.get_fps()), True, (255, 255, 255)), (10, 10))
        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
