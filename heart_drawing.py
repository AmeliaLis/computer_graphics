import pygame
import math
import time


pygame.init()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Serduszko w Pygame")

# colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def put_pixel(surface, x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        surface.set_at((x, y), color)

# Funkcja rysująca serduszko piksel po pikselu
def draw_heart():
    prev_x, prev_y = None, None
    for t in range(0, 360, 1):  # Zakres kątów 0-360 stopni
        angle = math.radians(t)
        x = int(16 * math.sin(angle) ** 3 * 20 + WIDTH // 2)
        y = int(- (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 20 + HEIGHT // 2)
        
        if prev_x is not None and prev_y is not None:
            dx = abs(x - prev_x)
            dy = abs(y - prev_y)
            sx = 1 if prev_x < x else -1
            sy = 1 if prev_y < y else -1
            err = dx - dy
            
            while prev_x != x or prev_y != y:
                put_pixel(screen, prev_x, prev_y, RED)
                e2 = 2 * err
                if e2 > -dy:
                    err -= dy
                    prev_x += sx
                if e2 < dx:
                    err += dx
                    prev_y += sy
        
        put_pixel(screen, x, y, RED)
        prev_x, prev_y = x, y
        pygame.display.flip()
        time.sleep(0.01)  # Opóźnienie dla efektu animacji

# Pętla gry
running = True
while running:
    screen.fill(WHITE)
    draw_heart()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()