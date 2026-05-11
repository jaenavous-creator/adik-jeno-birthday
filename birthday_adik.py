import pygame
import sys
import math

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adik Jeno Birthday")

clock = pygame.time.Clock()

BACKGROUND = (20, 10, 40)
WHITE = (255, 255, 255)
PINK = (255, 170, 220)
CAKE = (255, 200, 150)
YELLOW = (255, 240, 120)

title_font = pygame.font.SysFont("arial", 45)
small_font = pygame.font.SysFont("arial", 25)

balloons = []

for i in range(10):
    balloons.append([80 * i + 50, HEIGHT])

running = True

while running:

    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(50):
        pygame.draw.circle(
            screen,
            WHITE,
            ((i * 40) % WIDTH, (i * 70) % HEIGHT),
            2
        )

    text = title_font.render("Adik Birthday_21", True, WHITE)
    screen.blit(text, (220, 70))

    text2 = small_font.render("for Adik", True, PINK)
    screen.blit(text2, (390, 130))

    for balloon in balloons:

        pygame.draw.circle(
            screen,
            PINK,
            (balloon[0], int(balloon[1])),
            20
        )

        pygame.draw.line(
            screen,
            WHITE,
            (balloon[0], balloon[1] + 20),
            (balloon[0], balloon[1] + 50),
            2
        )

        balloon[1] -= 0.5

        if balloon[1] < -50:
            balloon[1] = HEIGHT + 50

    pygame.draw.rect(screen, CAKE, (320, 400, 260, 60), border_radius=10)

    pygame.draw.rect(screen, CAKE, (360, 340, 180, 50), border_radius=10)

    pygame.draw.rect(screen, CAKE, (400, 290, 100, 40), border_radius=10)

    pygame.draw.rect(screen, WHITE, (445, 240, 10, 50))

    flame = 220 + math.sin(pygame.time.get_ticks() * 0.02) * 5

    pygame.draw.circle(
        screen,
        YELLOW,
        (450, int(flame)),
        10
    )

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()