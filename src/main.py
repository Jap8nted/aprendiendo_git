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

    screen.fill((55,23,25))
    x = random.randint(100,400)
    y = random.randint(100,400)
    pygame.draw.circle(screen,(0,100,155),(x,y),25)
   

    pygame.display.flip()

pygame.quit()
