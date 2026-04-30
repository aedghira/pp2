import pygame, random, sys, os

# ===================== INITIALIZATION =====================
pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Рабочая директория
os.chdir(os.path.dirname(__file__))

# ===================== LOAD ASSETS =====================
road = pygame.image.load("background.jpg")
car = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")

# Монеты разных типов (ценность)
coin1 = pygame.image.load("coin1.png").convert_alpha()  # value = 1
coin2 = pygame.image.load("coin1.png").convert_alpha()  # value = 2
coin3 = pygame.image.load("coin1.png").convert_alpha()  # value = 3

# Масштабирование
car = pygame.transform.scale(car, (70, 110))
enemy = pygame.transform.scale(enemy, (70, 110))
coin1 = pygame.transform.scale(coin1, (60, 60))
coin2 = pygame.transform.scale(coin2, (40, 40))
coin3 = pygame.transform.scale(coin3, (30, 30))
road = pygame.transform.scale(road, (400, 600))


# ===================== GAME OBJECTS =====================

# Игрок
player_rect = car.get_rect(center=(WIDTH//2, HEIGHT-100))

# Враг
enemy_rect = enemy.get_rect(center=(WIDTH//2, -100))
enemy_speed = 5

# Монеты (система типов)
coins_data = [
    {"img": coin1, "value": 1},
    {"img": coin2, "value": 2},
    {"img": coin3, "value": 3}
]

# Функция генерации монеты с вероятностями
def generate_coin():
    weights = [0.6, 0.3, 0.1]  # вероятность выпадения
    chosen = random.choices(coins_data, weights)[0]

    rect = chosen["img"].get_rect(
        center=(random.randint(50, WIDTH-50), -50)
    )
    return {"coin": chosen, "rect": rect}

# Список монет на экране
coins_on_screen = []

# Изначально создаем 3 монеты
for _ in range(2):
    coins_on_screen.append(generate_coin())

coin_speed = 5
coins_collected = 0

# Каждые N монет увеличивается скорость
N = 5

font = pygame.font.SysFont("Times New Roman", 24)

# ===================== GAME LOOP =====================
running = True
while running:
    screen.fill(WHITE)
    screen.blit(road, (0, 0))

    # -------- EVENTS --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # -------- PLAYER MOVEMENT --------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5

    # -------- ENEMY LOGIC --------
    enemy_rect.y += enemy_speed

    if enemy_rect.top > HEIGHT:
        enemy_rect.center = (random.randint(50, WIDTH-50), -100)

    # -------- COINS LOGIC --------
    for coin_obj in coins_on_screen:
        coin_obj["rect"].y += coin_speed

    # Удаление вышедших за экран монет
    for coin_obj in coins_on_screen[:]:
        if coin_obj["rect"].top > HEIGHT:
            coins_on_screen.remove(coin_obj)
            coins_on_screen.append(generate_coin())

    # -------- COLLISIONS --------

    # Столкновение с врагом
    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Столкновение с монетами
    for coin_obj in coins_on_screen[:]:
        if player_rect.colliderect(coin_obj["rect"]):
            coins_collected += coin_obj["coin"]["value"]

            coins_on_screen.remove(coin_obj)
            coins_on_screen.append(generate_coin())

            # Увеличение сложности
            enemy_speed = 5 + (coins_collected // N)

    # -------- DRAW --------
    screen.blit(car, player_rect)
    screen.blit(enemy, enemy_rect)

    for coin_obj in coins_on_screen:
        screen.blit(coin_obj["coin"]["img"], coin_obj["rect"])

    # -------- UI --------
    score_text = font.render(f"COINS: {coins_collected}", True, WHITE)
    rects = score_text.get_rect(topleft=(260, 20))
    pygame.draw.rect(screen, WHITE, rects, 2)
    screen.blit(score_text, (WIDTH-140, 20))

    pygame.display.update()
    clock.tick(60)