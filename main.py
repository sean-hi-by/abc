import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
TARGET_SIZE = 30
TARGET_COUNT = 5
FPS = 30

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Target class
class Target:
    def __init__(self):
        self.x = random.randint(0, WIDTH - TARGET_SIZE)
        self.y = random.randint(0, HEIGHT // 2)
        self.size = TARGET_SIZE

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.size, self.size))

# Function to check if a target is hit
def is_hit(target, pos):
    x, y = pos
    return (target.x <= x <= target.x + target.size) and (target.y <= y <= target.y + target.size)

def main():
    clock = pygame.time.Clock()
    score = 0
    targets = [Target() for _ in range(TARGET_COUNT)]

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for target in targets[:]:
                    if is_hit(target, event.pos):
                        targets.remove(target)
                        score += 1
                        break

        for target in targets:
            target.draw()

        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        if not targets:
            font = pygame.font.Font(None, 48)
            game_over_text = font.render(f"Game Over! Your score: {score}", True, BLACK)
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            score = 0
            targets = [Target() for _ in range(TARGET_COUNT)]

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()