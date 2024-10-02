import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 750)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.rect.x = random.randint(0, 750)
            self.rect.y = random.randint(-100, -40)
