import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('src/assets/testAssets/rock.png');
        self.rect = self.image.get_rect(topleft = pos)
    
