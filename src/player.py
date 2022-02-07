import pygame
from debug import debug
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles):
        super().__init__(groups)
        self.image = pygame.image.load('src/assets/testAssets/player.png');
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacles = obstacles

    def move(self, speed):
        # normalizado de velocidad diagonal
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision("horizontal")
        self.rect.y += self.direction.y * speed
        self.collision("vertical")

    def collision(self, direction):
        if(direction == "horizontal"):
            for obstacle in self.obstacles:
                if obstacle.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = self.rect.left
                    if self.direction.x < 0:
                        self.rect.left = self.rect.right
        if(direction == 'vertical'):
            for obstacles in self.obstacles:
                if obstacles.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = self.rect.top
                    if self.direction.y < 0:
                        self.rect.top = self.rect.bottom

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


