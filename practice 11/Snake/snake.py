import pygame, random, sys

pygame.init()

# ===================== НАСТРОЙКИ =====================
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Advanced")

clock = pygame.time.Clock()

# ===================== ЦВЕТА =====================
WHITE = (255, 255, 255)
SOFT_PINK = (255, 182, 193)   # нежно-розовый (тело)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 105, 180)        # еда value=3
BLACK = (0, 0, 0)

# ===================== ЗМЕЙКА =====================
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# ===================== ЕДА =====================
foods = []
FOOD_LIFETIME = 10000  # 10 секунд

def spawn_food():
    """Создаёт еду с весом и временем появления"""
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            break

    value = random.choice([1, 2, 3])

    foods.append({
        "pos": (x, y),
        "value": value,
        "spawn_time": pygame.time.get_ticks()
    })

# старт — несколько еды
for _ in range(4):
    spawn_food()

# ===================== ПЕРЕМЕННЫЕ =====================
score = 0
speed = 5
tick = 0
foods_eaten = 0
level = 1

font = pygame.font.SysFont("Arial", 20)

# ===================== РИСОВАНИЕ =====================
def draw_head(pos, direction):
    x, y = pos

    pygame.draw.rect(screen,BLACK, (x, y, CELL_SIZE, CELL_SIZE), border_radius=6)

    cx = x + CELL_SIZE // 2
    cy = y + CELL_SIZE // 2

    if direction == (CELL_SIZE, 0):  # вправо
        eyes = [(cx+4, cy-4), (cx+4, cy+4)]
        tongue = (x + CELL_SIZE + 6, cy)
    elif direction == (-CELL_SIZE, 0):  # влево
        eyes = [(cx-4, cy-4), (cx-4, cy+4)]
        tongue = (x - 6, cy)
    elif direction == (0, -CELL_SIZE):  # вверх
        eyes = [(cx-4, cy-4), (cx+4, cy-4)]
        tongue = (cx, y - 6)
    else:  # вниз
        eyes = [(cx-4, cy+4), (cx+4, cy+4)]
        tongue = (cx, y + CELL_SIZE + 6)

    for ex, ey in eyes:
        pygame.draw.circle(screen, WHITE, (ex, ey), 2)

    # язык (мигает)
    if tick % 20 < 10:
        pygame.draw.line(screen, RED, (cx, cy), tongue, 2)


def draw_body(pos):
    pygame.draw.rect(screen, SOFT_PINK, (*pos, CELL_SIZE, CELL_SIZE), border_radius=6)


def draw_food(food):
    x, y = food["pos"]
    value = food["value"]

    if value == 1:
        color = GREEN
    elif value == 2:
        color = RED
    else:
        color = PINK

    pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE), border_radius=4)



# ===================== ЦИКЛ =====================
while True:
    screen.fill((255, 255, 255))

    current_time = pygame.time.get_ticks()

    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # управление
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)

    # движение
    new_head = (snake[0][0] + direction[0],
                snake[0][1] + direction[1])

    # столкновения
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake):
        print("Game Over")
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # ---------- СЪЕДАНИЕ ----------
    eaten = False

    for food in foods[:]:
        if new_head == food["pos"]:
            score += food["value"]
            foods_eaten += 1   # считаем именно количество еды

              
            foods.remove(food)
            spawn_food()
            eaten = True

    # каждые 8 съеденных еды
            if foods_eaten % 8 == 0:
                level += 1
                speed += 2

    if not eaten:
        snake.pop()

    # ---------- УДАЛЕНИЕ ПО ВРЕМЕНИ ----------
    for food in foods[:]:
        if current_time - food["spawn_time"] >= FOOD_LIFETIME:
            foods.remove(food)
            spawn_food()

    # ---------- ОТРИСОВКА ----------
    for segment in snake[1:]:
        draw_body(segment)

    draw_head(snake[0], direction)

    for food in foods:
        draw_food(food)

    # UI
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(speed)

    tick += 1