import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Serce z równania z ułamkiem")

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def put_pixel(surface, x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        surface.set_at((x, y), color)

def draw_fractional_heart():
    scale = 80  # Skala dopasowana do zakresu
    offset_x = WIDTH // 2
    offset_y = HEIGHT // 2

    for px in range(WIDTH):
        for py in range(HEIGHT):
            # Zamiana na układ matematyczny
            x = (px - offset_x) / scale
            y = -(py - offset_y) / scale

            denom = (x**2 + abs(x) + 2)
            if denom != 0:
                shift = (2/3) * (x**2 + abs(x) - 6) / denom
                lhs = x**2 + (y - shift) ** 2

                # Sprawdzenie czy blisko 36
                if abs(lhs - 36) < 0.03:
                    put_pixel(screen, px, py, RED)
        
        # Mniejsze flipy co 5 linii dla płynności i szybkości
        if px % 5 == 0:
            pygame.display.flip()


# Pętla gry
running = True
while running:
    screen.fill(WHITE)
    draw_fractional_heart()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
