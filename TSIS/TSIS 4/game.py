import pygame
import random
import json
from config import *
import sounds


# ===================== УТИЛИТЫ =====================
def load_settings() -> dict:
    try:
        with open("settings.json") as f:
            return json.load(f)
    except Exception:
        return {"snake_color": list(ACCENT), "grid": False, "sound": False}


def save_settings(s: dict):
    with open("settings.json", "w") as f:
        json.dump(s, f, indent=4)


def rand_cell(exclude: set) -> tuple:
    """Случайная свободная ячейка."""
    while True:
        x = random.randint(0, GRID_W - 1) * CELL_SIZE
        y = random.randint(0, GRID_H - 1) * CELL_SIZE + PANEL_H
        if (x, y) not in exclude:
            return (x, y)


# ===================== РИСОВАНИЕ =====================
font_ui   = None
font_big  = None

def init_fonts():
    global font_ui, font_big
    font_ui  = pygame.font.SysFont("Arial", 18)
    font_big = pygame.font.SysFont("Arial", 26, bold=True)


def draw_cell(surface, color, pos, radius=5):
    pygame.draw.rect(surface, color, (*pos, CELL_SIZE, CELL_SIZE), border_radius=radius)


def draw_snake(surface, snake, snake_color, direction, tick):
    for seg in snake[1:]:
        draw_cell(surface, snake_color, seg, radius=6)

    # голова
    hx, hy = snake[0]
    pygame.draw.rect(surface, BLACK, (hx, hy, CELL_SIZE, CELL_SIZE), border_radius=6)
    cx = hx + CELL_SIZE // 2
    cy = hy + CELL_SIZE // 2

    if direction == (CELL_SIZE, 0):
        eyes = [(cx+4, cy-4), (cx+4, cy+4)]
        tongue_end = (hx + CELL_SIZE + 6, cy)
    elif direction == (-CELL_SIZE, 0):
        eyes = [(cx-4, cy-4), (cx-4, cy+4)]
        tongue_end = (hx - 6, cy)
    elif direction == (0, -CELL_SIZE):
        eyes = [(cx-4, cy-4), (cx+4, cy-4)]
        tongue_end = (cx, hy - 6)
    else:
        eyes = [(cx-4, cy+4), (cx+4, cy+4)]
        tongue_end = (cx, hy + CELL_SIZE + 6)

    for ex, ey in eyes:
        pygame.draw.circle(surface, WHITE, (ex, ey), 2)
    if tick % 20 < 10:
        pygame.draw.line(surface, RED, (cx, cy), tongue_end, 2)


def draw_food(surface, food):
    color = FOOD_COLORS.get(food["value"], GREEN)
    draw_cell(surface, color, food["pos"], radius=4)
    # вес
    lbl = font_ui.render(str(food["value"]), True, BLACK)
    surface.blit(lbl, (food["pos"][0] + 4, food["pos"][1] + 2))


def draw_poison(surface, poison):
    draw_cell(surface, DARK_RED, poison["pos"], radius=4)
    lbl = font_ui.render("☠", True, WHITE)
    surface.blit(lbl, (poison["pos"][0] + 2, poison["pos"][1] + 1))


def draw_powerup(surface, pu):
    color = POWERUP_COLORS.get(pu["type"], PURPLE)
    draw_cell(surface, color, pu["pos"], radius=8)
    icons = {"speed": "⚡", "slow": "❄", "shield": "🛡"}
    lbl = font_ui.render(icons.get(pu["type"], "?"), True, BLACK)
    surface.blit(lbl, (pu["pos"][0] + 2, pu["pos"][1] + 1))


def draw_obstacles(surface, obstacles):
    for pos in obstacles:
        draw_cell(surface, GRAY, pos, radius=3)
        pygame.draw.rect(surface, DARK_GRAY, (*pos, CELL_SIZE, CELL_SIZE), 1, border_radius=3)


def draw_grid(surface):
    for gx in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, (230, 230, 230), (gx, PANEL_H), (gx, HEIGHT), 1)
    for gy in range(PANEL_H, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, (230, 230, 230), (0, gy), (WIDTH, gy), 1)


def draw_hud(surface, score, level, personal_best, active_effect, effect_end):
    pygame.draw.rect(surface, DARKER, (0, 0, WIDTH, PANEL_H))
    pygame.draw.line(surface, GRAY, (0, PANEL_H), (WIDTH, PANEL_H), 1)

    sc  = font_big.render(f"Score: {score}", True, WHITE)
    lv  = font_big.render(f"Level: {level}", True, ACCENT)
    pb  = font_ui.render(f"Best: {personal_best}", True, GRAY)
    surface.blit(sc, (10, 8))
    surface.blit(lv, (160, 8))
    surface.blit(pb, (310, 16))

    if active_effect:
        now  = pygame.time.get_ticks()
        left = max(0, (effect_end - now) // 1000)
        color = POWERUP_COLORS.get(active_effect, WHITE)
        eff = font_ui.render(f"⚡ {active_effect.upper()} {left}s", True, color)
        surface.blit(eff, (450, 16))


# ===================== ЛОГИКА СПАВНА =====================
def spawn_food_item(occupied: set) -> dict:
    return {
        "pos":        rand_cell(occupied),
        "value":      random.choice([1, 2, 3]),
        "spawn_time": pygame.time.get_ticks(),
    }


def spawn_poison(occupied: set) -> dict:
    return {
        "pos":        rand_cell(occupied),
        "spawn_time": pygame.time.get_ticks(),
    }


def spawn_powerup(occupied: set) -> dict:
    return {
        "pos":        rand_cell(occupied),
        "type":       random.choice(["speed", "slow", "shield"]),
        "spawn_time": pygame.time.get_ticks(),
    }


def occupied_set(snake, foods, poisons, powerup, obstacles) -> set:
    s = set(snake)
    s |= {f["pos"] for f in foods}
    s |= {p["pos"] for p in poisons}
    if powerup:
        s.add(powerup["pos"])
    s |= set(obstacles)
    return s


def place_obstacles(level: int, snake: list, existing: set) -> list:
    """Расставляет блоки препятствий. Голова змеи + соседи защищены."""
    count   = (level - 2) * OBSTACLE_PER_LEVEL
    blocked = set(snake) | existing
    # защита вокруг головы
    hx, hy = snake[0]
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            blocked.add((hx + dx * CELL_SIZE, hy + dy * CELL_SIZE))

    new_obs = []
    attempts = 0
    while len(new_obs) < count and attempts < 1000:
        attempts += 1
        x = random.randint(0, GRID_W - 1) * CELL_SIZE
        y = random.randint(0, GRID_H - 1) * CELL_SIZE + PANEL_H
        if (x, y) not in blocked:
            blocked.add((x, y))
            new_obs.append((x, y))
    return new_obs


# ===================== ИГРА =====================
class SnakeGame:
    def __init__(self, screen, personal_best: int, settings: dict):
        global font_ui, font_big
        font_ui  = pygame.font.SysFont("Arial", 18)
        font_big = pygame.font.SysFont("Arial", 26, bold=True)

        self.screen       = screen
        self.settings     = settings
        self.personal_best = personal_best

        snake_color = tuple(settings.get("snake_color", list(ACCENT)))
        self.snake_color = snake_color

        # Змейка
        cx = (GRID_W // 2) * CELL_SIZE
        cy = (GRID_H // 2) * CELL_SIZE + PANEL_H
        self.snake     = [(cx, cy), (cx - CELL_SIZE, cy), (cx - CELL_SIZE*2, cy)]
        self.direction = (CELL_SIZE, 0)
        self.next_dir  = (CELL_SIZE, 0)

        # Счёт
        self.score        = 0
        self.level        = 1
        self.foods_eaten  = 0
        self.speed        = BASE_FPS

        # Поля объектов
        self.foods    = []
        self.poisons  = []
        self.powerup  = None
        self.obstacles= []

        # Powerup-эффект
        self.active_effect = None   # "speed" | "slow" | "shield"
        self.effect_end    = 0
        self.shield_ready  = False

        # Инициализация еды
        occ = occupied_set(self.snake, [], [], None, [])
        for _ in range(FOOD_COUNT):
            self.foods.append(spawn_food_item(occ))
            occ = occupied_set(self.snake, self.foods, [], None, [])
        self.poisons.append(spawn_poison(occ))
        occ = occupied_set(self.snake, self.foods, self.poisons, None, [])
        self.powerup = spawn_powerup(occ)

        self.tick = 0
        self.clock = pygame.time.Clock()
        sounds.set_enabled(settings.get("sound", False))

    # ---- Обработка ввода ----
    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            d = self.direction
            if event.key == pygame.K_UP    and d != (0, CELL_SIZE):
                self.next_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN  and d != (0, -CELL_SIZE):
                self.next_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT  and d != (CELL_SIZE, 0):
                self.next_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and d != (-CELL_SIZE, 0):
                self.next_dir = (CELL_SIZE, 0)

    # ---- Один шаг ----
    def step(self) -> str:
        """Возвращает 'ok' | 'dead'."""
        now = pygame.time.get_ticks()
        self.direction = self.next_dir

        new_head = (
            self.snake[0][0] + self.direction[0],
            self.snake[0][1] + self.direction[1],
        )

        # --- столкновения ---
        wall = (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < PANEL_H or new_head[1] >= HEIGHT)
        self_hit = new_head in self.snake
        obs_hit  = new_head in self.obstacles

        if (wall or self_hit or obs_hit):
            if self.shield_ready:
                self.shield_ready  = False
                self.active_effect = None
                # телепорт на безопасную позицию не делаем — просто игнорируем
                return "ok"
            return "dead"

        self.snake.insert(0, new_head)

        # --- powerup-эффект истёк ---
        if self.active_effect and now >= self.effect_end:
            self._reset_effect()

        # --- съедание еды ---
        eaten = False
        for food in self.foods[:]:
            if new_head == food["pos"]:
                self.score       += food["value"]
                self.foods_eaten += 1
                self.foods.remove(food)
                sounds.eat()
                occ = occupied_set(self.snake, self.foods, self.poisons, self.powerup, self.obstacles)
                self.foods.append(spawn_food_item(occ))
                eaten = True

                if self.foods_eaten % FOODS_PER_LEVEL == 0:
                    self._level_up()
                break

        # --- яд ---
        for poison in self.poisons[:]:
            if new_head == poison["pos"]:
                self.poisons.remove(poison)
                sounds.poison()
                # укоротить
                for _ in range(POISON_SHORTEN):
                    if len(self.snake) > 1:
                        self.snake.pop()
                if len(self.snake) <= 1:
                    return "dead"
                eaten = True
                occ = occupied_set(self.snake, self.foods, self.poisons, self.powerup, self.obstacles)
                self.poisons.append(spawn_poison(occ))
                break

        # --- powerup ---
        if self.powerup and new_head == self.powerup["pos"]:
            self._apply_powerup(self.powerup["type"], now)
            sounds.powerup()
            occ = occupied_set(self.snake, self.foods, self.poisons, None, self.obstacles)
            self.powerup = spawn_powerup(occ)
            eaten = True

        if not eaten:
            self.snake.pop()

        # --- истечение еды ---
        for food in self.foods[:]:
            if now - food["spawn_time"] >= FOOD_LIFETIME:
                self.foods.remove(food)
                occ = occupied_set(self.snake, self.foods, self.poisons, self.powerup, self.obstacles)
                self.foods.append(spawn_food_item(occ))

        for poison in self.poisons[:]:
            if now - poison["spawn_time"] >= FOOD_LIFETIME:
                self.poisons.remove(poison)
                occ = occupied_set(self.snake, self.foods, self.poisons, self.powerup, self.obstacles)
                self.poisons.append(spawn_poison(occ))

        if self.powerup and now - self.powerup["spawn_time"] >= POWERUP_LIFETIME:
            occ = occupied_set(self.snake, self.foods, self.poisons, None, self.obstacles)
            self.powerup = spawn_powerup(occ)

        self.tick += 1
        return "ok"

    def _level_up(self):
        self.level += 1
        self.speed  = min(BASE_FPS + (self.level - 1) * 2, 25)
        sounds.levelup()
        if self.level >= 3:
            occ = occupied_set(self.snake, self.foods, self.poisons, self.powerup, self.obstacles)
            new_obs = place_obstacles(self.level, self.snake, set(self.obstacles))
            self.obstacles.extend(new_obs)

    def _apply_powerup(self, ptype: str, now: int):
        self._reset_effect()
        self.active_effect = ptype
        self.effect_end    = now + POWERUP_DURATION
        if ptype == "speed":
            self.speed = min(self.speed + SPEED_BOOST_ADD, 30)
        elif ptype == "slow":
            self.speed = max(self.speed - SLOW_MOTION_SUB, 2)
        elif ptype == "shield":
            self.shield_ready = True
            sounds.shield()

    def _reset_effect(self):
        if self.active_effect == "speed":
            self.speed = BASE_FPS + (self.level - 1) * 2
        elif self.active_effect == "slow":
            self.speed = BASE_FPS + (self.level - 1) * 2
        elif self.active_effect == "shield":
            self.shield_ready = False
        self.active_effect = None

    # ---- Отрисовка ----
    def draw(self):
        self.screen.fill(WHITE)

        if self.settings.get("grid"):
            draw_grid(self.screen)

        draw_obstacles(self.screen, self.obstacles)

        for food in self.foods:
            draw_food(self.screen, food)
        for poison in self.poisons:
            draw_poison(self.screen, poison)
        if self.powerup:
            draw_powerup(self.screen, self.powerup)

        draw_snake(self.screen, self.snake, self.snake_color, self.direction, self.tick)
        draw_hud(self.screen, self.score, self.level, self.personal_best,
                 self.active_effect, self.effect_end)
        pygame.display.update()

    # ---- Запуск ----
    def run(self) -> dict:
        """Запускает игровой цикл. Возвращает {'score':..,'level':..}"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    import sys; sys.exit()
                self.handle_keys(event)

            result = self.step()
            self.draw()

            if result == "dead":
                sounds.gameover()
                return {"score": self.score, "level": self.level}

            self.clock.tick(self.speed)