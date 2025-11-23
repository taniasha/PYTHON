import pygame
import math

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

h, k = 300, 200  # center
a, b = 200, 100  # axes
theta = 0
speed = 0.02

running = True
while running:
    screen.fill((0, 0, 0))
    
    x = h + a * math.cos(theta)
    y = k + b * math.sin(theta)
    
    pygame.draw.circle(screen, (255, 255, 0), (int(x), int(y)), 10)
    
    theta += speed  # move along ellipse
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
