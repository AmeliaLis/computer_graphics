import pygame
import math
import time

pygame.init()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Serce z równania")

# kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def put_pixel(surface, x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        surface.set_at((x, y), color)

def draw_equation_heart():
    scale = 100  # Skala, by lepiej dopasować do okna
    offset_x = WIDTH // 2
    offset_y = HEIGHT // 2

    for raw_x in range(-300, 301):  # Zakres w pikselach
        x = raw_x / scale  # Przeliczenie na współrzędne matematyczne

        # Wyliczamy wartości y z równania
        under_sqrt = 3 - x**2
        if under_sqrt >= 0:
            sqrt_val = math.sqrt(under_sqrt)
            for y_val in [sqrt_val, -sqrt_val]:
                # y = y_val + sqrt(|x|)
                y = y_val + math.sqrt(abs(x))

                # Zamiana współrzędnych matematycznych na ekranowe
                px = int(x * scale + offset_x)
                py = int(-y * scale + offset_y)  # "-" bo oś Y rośnie w dół

                put_pixel(screen, px, py, RED)
                pygame.display.flip()
                time.sleep(0.002)

# Pętla gry
running = True
while running:
    screen.fill(WHITE)
    draw_equation_heart()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
