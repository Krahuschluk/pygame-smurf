import pygame
import sys

from pygame.locals import *


def main_loop():
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((1000, 1000))

    pygame.display.set_caption('SMASH')
    while True:

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (100, 50, 20, 20))
                pygame.display.update()


if __name__ == '__main__':
    main_loop()
