import pygame
import math
import time


pygame.init()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Serduszko w Pygame")

# kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def put_pixel(surface, x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        surface.set_at((x, y), color)

# Funkcja rysująca serduszko piksel po pikselu
# FUnkcja przedstaiwa równania parametryczne które opisuję kształt serca za pomocą zmiennej t (kąta),
# a nie bezpośrednio x czy y
def draw_heart():
    prev_x, prev_y = None, None
    for t in range(0, 360, 1):  # Zakres kątów 0-360 stopni
        angle = math.radians(t)  # zamiana na radiany * 20 - zwiększenie widoczności serca
        x = int(16 * math.sin(angle) ** 3 * 20 + WIDTH // 2) # WIDTH // 2 oraz HEIGHT // 2 przesunięcie aby serce było na środku ekranu
        y = int(- (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 20 + HEIGHT // 2)
        # W pamięci komputerowej obraz jest przechowywany od górnej linii do dolnej, linia po linii — podobnie jak tekst w książce. Dlatego pierwsza linia (y=0) to górna krawędź, a kolejne linie (y=1, y=2, …) to linie niżej, dlatego jest - na początku przy y, żeby szło w górę jak w matematyce
        if prev_x is not None and prev_y is not None:
            dx = abs(x - prev_x) # różnica w poziomie, ile kroków w prawo, lewo
            dy = abs(y - prev_y) # różnica w pionie, ile kroków w dół lub górę
            sx = 1 if prev_x < x else -1 # kierunek rysowania (w prawo w lewo)
            sy = 1 if prev_y < y else -1 # w górę w dół
            err = dx - dy # zmienna kierująca, to licznik "błędu", 
            # czyli odchylenia – pomaga zdecydować, czy przesunąć się poziomo, pionowo, czy ukośnie,
            # by linia była jak najbliżej matematycznego ideału.
            # przechowuje informacje czy jesteśmy bliżej poziomej czy pionowej osi
            # jeśli err jest duży - idziemy w jednym kierunku (np. poziomo)
            # jeśli err się zmniejsza - dodajemy krok w drugim kierunku (np. pionowo)
            
            while prev_x != x or prev_y != y:
                put_pixel(screen, prev_x, prev_y, RED)
                e2 = 2 * err # technika optymalizacji (unikamy dzielenia)
                if e2 > -dy:
                    err -= dy
                    prev_x += sx
                if e2 < dx:
                    err += dx
                    prev_y += sy
            # Decyzja: czy przemieścić się poziomo, pionowo, czy oba na raz, 
            # aby linia była jak najbliżej teoretycznego odcinka.
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