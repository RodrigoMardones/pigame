import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDGHT, HEIGHT))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()
        self.level = Level()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick()
            


if __name__ == "__main__":
    newGame = Game()
    newGame.run()