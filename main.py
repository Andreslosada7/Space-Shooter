import pygame
import sys
from player import Player
from projectile import Projectile
from enemy import Enemy
import random

# Inicializar pygame
pygame.init()
# Inicializa el módulo de sonido
pygame.mixer.init()  

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Espacial")

# Colores y FPS
BLACK = (0, 0, 0)
FPS = 60
CLOCK = pygame.time.Clock()

def main():
    run = True
    player = Player()
    all_sprites = pygame.sprite.Group(player)
    projectiles = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Crear enemigos iniciales
    for _ in range(10):
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    # Cargar la imagen de fondo
    background = pygame.image.load("assets/space_background.jpg").convert()

    # Cargar el logo de Kodland
    kodland = pygame.image.load("assets/kodland.png").convert()

    # Cargar la música de fondo
    pygame.mixer.music.load("assets/background_music.mp3") 
    pygame.mixer.music.play(-1)

    # Cargar el sonido del disparo
    shoot_sound = pygame.mixer.Sound("assets/shoot.wav")


    score = 0
    start_ticks = pygame.time.get_ticks() 

    while run:
        CLOCK.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                projectile = Projectile(player.rect.centerx, player.rect.top)
                projectiles.add(projectile)
                all_sprites.add(projectile)

                # Reproducir el sonido de disparo
                shoot_sound.play()


        player.update(keys)

        # Actualizar proyectiles y enemigos
        projectiles.update()
        enemies.update()

        # Detección de colisiones entre proyectiles y enemigos
        hits = pygame.sprite.groupcollide(projectiles, enemies, True, True)
        for hit in hits:
            score += 1
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Detección de colisiones entre el jugador y enemigos
        if pygame.sprite.spritecollide(player, enemies, False):
            player.lose_life()
            # Reubica al enemigo que colisionó
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    enemy.rect.y = random.randint(-100, -40)
                    enemy.rect.x = random.randint(0, 750)

        # Si el jugador pierde todas las vidas
        if player.lives <= 0:
            run = False  # Termina el juego

        # Control de tiempo
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Calcular el tiempo en segundos
        if seconds > 20:  # 20 segundos de duración
            run = False  # Termina el juego

        # Dibujar el fondo
        WINDOW.blit(background, (0, 0)) 

        # Dibujar el logo
        kodland_img = pygame.transform.scale(kodland, (200, 80)) 
        WINDOW.blit(kodland_img, (300, 0))  

        # Dibujar todo en la ventana
        all_sprites.draw(WINDOW)

        # Mostrar el puntaje y las vidas
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Puntaje: {score}", True, (255, 255, 255))
        WINDOW.blit(score_text, (10, 10))
        lives_text = font.render(f"Vidas: {player.lives}", True, (255, 255, 255))
        WINDOW.blit(lives_text, (10, 40))

        pygame.display.update()

    # Mostrar el menú de victoria o derrota
    show_end_menu(score, player.lives)

def show_end_menu(score, lives):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WINDOW.fill(BLACK)
        font = pygame.font.SysFont(None, 40)
        if lives <= 0:
            end_text = font.render("¡Perdiste!", True, (255, 0, 0))
        else:
            end_text = font.render("¡Sobreviviste! ¡lo lograste!", True, (0, 255, 0))

        score_text = font.render(f"Tu puntaje: {score}", True, (255, 255, 255))
        restart_text = font.render("presiona R para empezar de nuevo", True, (255, 255, 255))
        kodland_text = font.render("¡Viva Kodland!", True, (255, 255, 255))

        WINDOW.blit(kodland_text, (200, 100))
        WINDOW.blit(end_text, (200, 200))
        WINDOW.blit(score_text, (200, 300))
        WINDOW.blit(restart_text, (200, 400))

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:  # Presionar 'R' para reiniciar el juego
            main()
        if keys[pygame.K_q]:  # Presionar 'Q' para salir del juego
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
