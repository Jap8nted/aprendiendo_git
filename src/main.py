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
    pygame.draw.circle(screen,(100,180,155),(x,y),25)
   
   

    pygame.display.flip()

pygame.quit()
