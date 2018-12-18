import pygame
import os
from pygame.locals import *


class App:

    windowWidth = 640
    windowHeight = 480
    x = 10
    y = 10

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load(os.path.join("resources", "smurf.png")).convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self._image_surf, (self.x, self.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:

                for event in pygame.event.get():
                    self.on_event(event)

                self.on_loop()
                self.on_render()

        self.on_cleanup()


if __name__ == '__main__':
    app = App()
    app.on_execute()
