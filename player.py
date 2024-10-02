import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/nave.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 150)) 
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)
        self.speed = 5
        self.lives = 3

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def update(self, keys):
        self.move(keys)

    def lose_life(self):
        self.lives -= 1 