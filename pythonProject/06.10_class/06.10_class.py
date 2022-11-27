import time

import numpy as np
import pygame

def dbscan():
    eps = 30
    minNeigh = 4


def pygame_func():
    pygame.init()
    points_x = []
    points_y = []
    points = []
    screen = pygame.display.set_mode([1500, 800])
    screen.fill(color='white')
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if pygame.mouse.get_pressed()[0]:
                pygame.draw.circle(screen, 'black', event.pos, 5)
                x, y = event.pos
                points_x.append(x)
                points_y.append(y)
                time.sleep(0.05)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    points.insert(0, points_x)
                    points.insert(1, points_y)
                    np.matrix(points)
                    print(points)
        pygame.display.update()

if __name__ == "__main__":
    pygame_func()