import pygame
from settings import WORLD_MAP, SIZE_TILE
from player import Player
from tile import Tile

from debug import debug
class Level:
    def __init__ (self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
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
                    self.player = Player((x,y), [self.visible_sprites],self.obstacles_sprites)


    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_height
        self.offset.y = player.rect.centery - self.half_width    
  
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_rect)
