import pygame
from settings import WORLD_MAP, SIZE_TILE
from player import Player
from tile import Tile

from debug import debug
class Level:
    def __init__ (self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for rowIndex,row in enumerate(WORLD_MAP):
            for colIndex, col in enumerate(row):
                x = colIndex * SIZE_TILE
                y  = rowIndex * SIZE_TILE
                if(col == 'x'):
                    Tile((x,y), [self.visible_sprites, self.obstacles_sprites])
                if(col == 'p'):
                    self.player = Player((x,y), [self.visible_sprites])


    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)