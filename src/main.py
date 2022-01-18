<<<<<<< HEAD
from time import sleep
import pygame
import random

pygame.init()

screen = pygame.display.set_mode([500,500])
running = True                      
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    x = random.randint(100,400)
    y = random.randint(100,400)
    pygame.draw.circle(screen,(0,100,155),(x,y),25)
   

    pygame.display.flip()

pygame.quit()
=======
import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 40)

    pygame.display.flip()


pygame.quit()
>>>>>>> c0bc6bf851973193a91ef78d7132005b77f49d51
