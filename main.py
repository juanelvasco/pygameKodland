import pygame, sys
import random
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
   pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("HiriRUNNER")

# Cargar imágenes
BG = pygame.image.load("assets/Background.png")
PLAYER_IMAGE = pygame.image.load("assets/player.png")
ENEMY_IMAGE = pygame.image.load("assets/enemy.png")

def play():
    player_rect = PLAYER_IMAGE.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
    player_speed = 5

    enemies = []
    enemy_speed = 3

    clock = pygame.time.Clock()

    score = 0
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:
            player_rect.x += player_speed

        SCREEN.blit(BG, (0, 0))  # Dibujar el fondo
        SCREEN.blit(PLAYER_IMAGE, player_rect)  # Dibujar al jugador

        # Generar enemigos aleatorios
        if random.randint(0, 100) < 3:  # Ajusta el valor para cambiar la frecuencia de aparición de enemigos
            enemy_rect = ENEMY_IMAGE.get_rect(center=(random.randint(50, SCREEN_WIDTH - 50), 0))
            enemies.append(enemy_rect)

        # Mover y dibujar enemigos
        for enemy_rect in enemies:
            enemy_rect.y += enemy_speed
            SCREEN.blit(ENEMY_IMAGE, enemy_rect)

            # Comprobar colisión con el jugador
            if player_rect.colliderect(enemy_rect):
                print("Game Over!")
                pygame.quit()
                sys.exit()

            # Comprobar si el enemigo ha salido de la pantalla
            if enemy_rect.y > SCREEN_HEIGHT:
                enemies.remove(enemy_rect)
                score += 1

        # Mostrar el marcador (score)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        SCREEN.blit(score_text, (SCREEN_WIDTH - 150, 20))

        pygame.display.update()
        clock.tick(60)
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("HiriRUNNER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()