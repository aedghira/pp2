# ===================== КОНФИГУРАЦИЯ =====================

# Размер окна и сетки
WIDTH      = 700
HEIGHT     = 500
CELL_SIZE  = 20
PANEL_H    = 50          # верхняя панель HUD

# Игровая область (без панели)
GRID_W = WIDTH // CELL_SIZE
GRID_H = (HEIGHT - PANEL_H) // CELL_SIZE

# FPS
BASE_FPS = 8

# Еда
FOOD_LIFETIME    = 10_000   # мс до исчезновения еды
FOOD_COUNT       = 4        # еды на поле одновременно
FOODS_PER_LEVEL  = 8        # сколько съесть для следующего уровня

# Яд
POISON_COUNT     = 1
POISON_SHORTEN   = 2        # укорачивает на 2 сегмента

# Powerup
POWERUP_LIFETIME = 8_000    # мс до исчезновения powerup-а
POWERUP_DURATION = 5_000    # мс действия эффекта
SPEED_BOOST_ADD  = 4
SLOW_MOTION_SUB  = 3

# Препятствия (с уровня 3)
OBSTACLE_PER_LEVEL = 5      # блоков за каждый новый уровень >= 3

# ===================== ЦВЕТА =====================
BLACK      = (0,   0,   0)
WHITE      = (255, 255, 255)
GRAY       = (180, 180, 180)
DARK_GRAY  = (40,  40,  50)
DARKER     = (25,  25,  33)
ACCENT     = (80,  200, 120)
ACCENT2    = (100, 180, 255)
RED        = (220, 50,  50)
ORANGE     = (255, 160, 30)
YELLOW     = (255, 230, 50)
PINK       = (255, 105, 180)
SOFT_PINK  = (255, 182, 193)
PURPLE     = (160, 80,  220)
DARK_RED   = (140, 0,   0)
CYAN       = (0,   220, 220)
GREEN      = (0, 200, 0)

# Цвета еды по весу
FOOD_COLORS = {1: ACCENT, 2: ORANGE, 3: PINK}

# Цвета powerup
POWERUP_COLORS = {
    "speed":  YELLOW,
    "slow":   CYAN,
    "shield": PURPLE,
}

# DB
DB_CONFIG = {
    "host":     "localhost",
    "port":     5432,
    "dbname":   "postgres",
    "user":     "algida",
    "password": "",
}