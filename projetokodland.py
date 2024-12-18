import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Project")


clock = pygame.time.Clock()


font = pygame.font.SysFont("Arial", 36)

def draw_text(text, color, x, y):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Main Menu", WHITE, WIDTH // 2 - 100, HEIGHT // 2 - 100)
        draw_text("Press ENTER to Start", WHITE, WIDTH // 2 - 150, HEIGHT // 2)
        draw_text("Press ESC to Quit", WHITE, WIDTH // 2 - 150, HEIGHT // 2 + 50)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def spawn_enemy():
    x = random.randint(0, WIDTH - 50)
    y = random.randint(-100, -40)
    speed = random.randint(3, 8)
    return pygame.Rect(x, y, 50, 50), speed

def game_loop():
    player = pygame.Rect(WIDTH // 2, HEIGHT - 60, 50, 50)
    enemies = [spawn_enemy() for _ in range(5)]
    score = 0

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 5

        
        for enemy, speed in enemies:
            enemy.y += speed
            if enemy.top > HEIGHT:
                enemies.remove((enemy, speed))
                enemies.append(spawn_enemy())
                score += 1

        
        for enemy, _ in enemies:
            if player.colliderect(enemy):
                game_over(score)

       
        pygame.draw.rect(screen, BLUE, player)
        for enemy, _ in enemies:
            pygame.draw.rect(screen, RED, enemy)

       
        draw_text(f"Score: {score}", WHITE, 10, 10)

        pygame.display.flip()
        clock.tick(FPS)

def game_over(score):
    while True:
        screen.fill(BLACK)
        draw_text("Game Over", WHITE, WIDTH // 2 - 100, HEIGHT // 2 - 100)
        draw_text(f"Your Score: {score}", WHITE, WIDTH // 2 - 100, HEIGHT // 2)
        draw_text("Press ENTER to Retry", WHITE, WIDTH // 2 - 150, HEIGHT // 2 + 50)
        draw_text("Press ESC to Quit", WHITE, WIDTH // 2 - 150, HEIGHT // 2 + 100)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()

