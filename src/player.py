import pygame
from debug import debug
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('src/assets/testAssets/player.png');
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def move(self, speed):
        # normalizado de velocidad diagonal
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * speed

    def input(self):
        # inputs del jugador
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_UP]):
            self.direction.y = -1
        elif(keys[pygame.K_DOWN]):
            self.direction.y = 1
        else:
            self.direction.y = 0
    
        if(keys[pygame.K_LEFT]):
            self.direction.x = -1
        elif(keys[pygame.K_RIGHT]):
            self.direction.x = +1
        else:
            self.direction.x = 0
    
    def update(self):
        self.input()
        self.move(self.speed)


