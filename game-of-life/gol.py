import pygame
from enum import Enum

class CellStatus(Enum):
    ALIVE = 1
    DEAD = 2

# TODO: Make 2D
class Tape:
    def __init__(self, a: [CellStatus]):
        self.a = a

    def _postoidx(self, p: int) -> int:
        if p == 0:
            return p
        elif p > 0:
            return 2*p-1
        else:
            return -2*p

    def __getitem__(self, pos):
        assert not isinstance(pos, tuple) 
        idx = self._postoidx(pos)
        if len(self.a) <= idx:
            self.a.extend([CellStatus.DEAD] * ((idx-len(self.a) + 1) + 100) )
        return self.a[idx]
            
    def set(self, s: CellStatus, pos: int):
        idx = self._postoidx(pos)
        if len(self.a) <= idx:
            self.a.extend([CellStatus.DEAD] * ((idx-len(self.a) + 1) + 100) )
        self.a[idx] = s

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()



if __name__ == "__main__":
    main()
