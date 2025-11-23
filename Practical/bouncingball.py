import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

x, y = 300, 200
vx, vy = 5, 3  # velocity
radius = 20

running = True
while running:
    screen.fill((0, 0, 0))
    
    # update position
    x += vx
    y += vy
    
    # collision with walls
    if x - radius < 0 or x + radius > 600:
        vx = -vx
    if y - radius < 0 or y + radius > 400:
        vy = -vy
    
    pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), radius)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
