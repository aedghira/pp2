import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
ball_r= 25
step = 20 
x = 300
y = 200

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - step - ball_r >= 0: # upper side's boundary
                    y -= step # we go up, but our y is decreases because of the coordinate system in python

            if event.key == pygame.K_DOWN:
                if y + step + ball_r <= 400: # lower side's boundary
                    y += step

            if event.key == pygame.K_LEFT:
                if x - step - ball_r >= 0: # left side's boundary
                    x -= step

            if event.key == pygame.K_RIGHT:
                if x + step + ball_r <= 600: # right side's boundary
                    x += step

    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen, (255, 0, 0), (x, y), ball_r)
    pygame.display.flip()

pygame.quit()
sys.exit()