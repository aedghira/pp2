import pygame, random, sys

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Images")


WHITE = (255, 255, 255)

clock = pygame.time.Clock()
import os, pygame

os.chdir(os.path.dirname(__file__))


background = pygame.image.load("background-2.png")
snake_img = pygame.image.load("snake.png")
food_img = pygame.image.load("food.png").convert_alpha()


background = pygame.transform.scale(background, (WIDTH, HEIGHT))
snake_img = pygame.transform.scale(snake_img, (CELL_SIZE, CELL_SIZE))
food_img = pygame.transform.scale(food_img, (20, 20))

snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)


def random_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

food = random_food()

score = 0
level = 1
speed = 5

font = pygame.font.SysFont("Times New Roman", 24)

running = True
while running:
    screen.blit(background, (0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        print("Game Over! Snake hit the wall.")
        pygame.quit()
        sys.exit()


    if new_head in snake:
        print("Game Over! Snake hit itself.")
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

   
    if new_head == food:
        score += 1
        food = random_food()
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    
    for segment in snake:
        screen.blit(snake_img, (segment[0], segment[1]))
    screen.blit(food_img, (food[0], food[1]))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(speed)