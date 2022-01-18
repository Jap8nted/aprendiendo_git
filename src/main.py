from time import sleep
import pygame
import random

pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True

red = (180, 50, 50)
size = (0, 0, 250, 200)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    x = random.randint(180, 440)
    y = random.randint(180, 440)
    pygame.draw.circle(screen, (100, 180, 155), (x, y), 25)

    pygame.draw.ellipse(screen, red, size)

    pygame.display.flip()

pygame.quit()
