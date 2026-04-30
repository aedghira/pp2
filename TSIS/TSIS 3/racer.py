import pygame
import random
import sys
import os
from persistence import load_settings

# ===================== КОНСТАНТЫ =====================
WIDTH, HEIGHT = 400, 600
FPS           = 60

# Полосы дороги (3 lanes)
LANE_XS    = [80, 200, 320]
LANE_W     = 80
ROAD_LEFT  = 30
ROAD_RIGHT = 370

# Цвета
WHITE    = (240, 240, 240)
BLACK    = (0,   0,   0)
GRAY     = (150, 150, 160)
DARK     = (20,  20,  30)
RED      = (220, 60,  60)
GREEN    = (80,  200, 120)
YELLOW   = (255, 220, 40)
ORANGE   = (255, 150, 30)
BLUE     = (100, 160, 255)
CYAN     = (0,   220, 220)
PURPLE   = (160, 80,  220)
ROAD_CLR = (50,  50,  60)
LANE_CLR = (80,  80,  90)

CAR_COLORS = {
    "default": GREEN,
    "red":     RED,
    "blue":    BLUE,
    "yellow":  YELLOW,
}

# ===================== АССЕТЫ =====================
def _try_load(path, fallback_size, fallback_color):
    try:
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, fallback_size)
    except Exception:
        s = pygame.Surface(fallback_size, pygame.SRCALPHA)
        s.fill(fallback_color)
        return s

def load_assets():
    assets = {}
    assets["road"]   = _try_load("assets/background.jpg", (WIDTH, HEIGHT), ROAD_CLR)
    assets["player"] = _try_load("assets/player.png",     (60, 100),       GREEN)
    assets["enemy"]  = _try_load("assets/enemy.png",      (60, 100),       RED)
    assets["coin1"]  = _try_load("assets/coin1.png",      (28, 28),        YELLOW)
    assets["coin2"]  = _try_load("assets/coin2.png",      (28, 28),        ORANGE)
    assets["coin3"]  = _try_load("assets/coin3.png",      (28, 28),        CYAN)
    return assets


# ===================== РИСОВАЛКИ =====================
def _draw_road(screen):
    pygame.draw.rect(screen, ROAD_CLR, (ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, HEIGHT))
    # разделители полос (пунктир)
    for lx in [140, 260]:
        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, LANE_CLR, (lx - 2, y, 4, 22))


def _car_surface(w, h, color):
    s = pygame.Surface((w, h), pygame.SRCALPHA)
    # кузов
    pygame.draw.rect(s, color, (w//4, 0, w//2, h), border_radius=8)
    pygame.draw.rect(s, color, (0, h//3, w, h//2), border_radius=6)
    # окна
    wc = (200, 230, 255)
    pygame.draw.rect(s, wc, (w//4+2, h//8, w//2-4, h//4), border_radius=4)
    # колёса
    wh = (40, 40, 40)
    pygame.draw.ellipse(s, wh, (0,      h//3,    w//4, h//5))
    pygame.draw.ellipse(s, wh, (3*w//4, h//3,    w//4, h//5))
    pygame.draw.ellipse(s, wh, (0,      2*h//3,  w//4, h//5))
    pygame.draw.ellipse(s, wh, (3*w//4, 2*h//3,  w//4, h//5))
    return s


def _obstacle_surface(kind):
    if kind == "oil":
        s = pygame.Surface((50, 30), pygame.SRCALPHA)
        pygame.draw.ellipse(s, (30, 20, 60, 200), (0, 0, 50, 30))
        return s
    elif kind == "barrier":
        s = pygame.Surface((60, 18), pygame.SRCALPHA)
        pygame.draw.rect(s, (255, 80, 20), (0, 0, 60, 18), border_radius=4)
        for i in range(0, 60, 12):
            pygame.draw.rect(s, (255, 220, 0), (i, 0, 6, 18))
        return s
    else:  # pothole
        s = pygame.Surface((36, 22), pygame.SRCALPHA)
        pygame.draw.ellipse(s, (40, 35, 25, 220), (0, 0, 36, 22))
        return s


# ===================== КЛАСС: POWERUP =====================
POWERUP_TYPES = ["nitro", "shield", "repair"]
POWERUP_COLORS = {"nitro": ORANGE, "shield": CYAN, "repair": GREEN}
POWERUP_ICONS  = {"nitro": "⚡", "shield": "🛡", "repair": "🔧"}
POWERUP_LIFETIME = 8000   # мс до исчезновения
POWERUP_DURATION = 4000   # мс действия


class PowerUp:
    SIZE = 32

    def __init__(self, kind, x, y):
        self.kind   = kind
        self.rect   = pygame.Rect(x - self.SIZE//2, y, self.SIZE, self.SIZE)
        self.born   = pygame.time.get_ticks()
        self._surf  = self._make()

    def _make(self):
        s = pygame.Surface((self.SIZE, self.SIZE), pygame.SRCALPHA)
        pygame.draw.circle(s, POWERUP_COLORS[self.kind], (self.SIZE//2, self.SIZE//2), self.SIZE//2)
        pygame.draw.circle(s, WHITE, (self.SIZE//2, self.SIZE//2), self.SIZE//2, 2)
        return s

    def update(self, speed):
        self.rect.y += speed

    def draw(self, screen, font):
        screen.blit(self._surf, self.rect)
        lbl = font.render(POWERUP_ICONS[self.kind], True, BLACK)
        screen.blit(lbl, lbl.get_rect(center=self.rect.center))

    def expired(self):
        return pygame.time.get_ticks() - self.born > POWERUP_LIFETIME

    def off_screen(self):
        return self.rect.top > HEIGHT


# ===================== КЛАСС: RACER GAME =====================
class RacerGame:
    DIFF = {
        "easy":   {"enemy_start": 4, "enemy_inc": 0.5, "obs_freq": 180, "traffic_max": 2},
        "normal": {"enemy_start": 6, "enemy_inc": 1.0, "obs_freq": 120, "traffic_max": 3},
        "hard":   {"enemy_start": 9, "enemy_inc": 1.5, "obs_freq": 80,  "traffic_max": 4},
    }

    def __init__(self, screen, assets):
        self.screen   = screen
        self.assets   = assets
        self.settings = load_settings()
        self.clock    = pygame.time.Clock()

        diff_key  = self.settings.get("difficulty", "normal")
        self.diff = self.DIFF.get(diff_key, self.DIFF["normal"])

        self.font_sm  = pygame.font.SysFont("Arial", 15)
        self.font_md  = pygame.font.SysFont("Arial", 20)
        self.font_lg  = pygame.font.SysFont("Arial", 28, bold=True)

        # --- машина игрока ---
        car_clr = CAR_COLORS.get(self.settings.get("car_color", "default"), GREEN)
        self.player_surf = _car_surface(60, 100, car_clr)
        self.player_rect = self.player_surf.get_rect(center=(WIDTH // 2, HEIGHT - 100))

        # --- скорость ---
        self.base_speed   = self.diff["enemy_start"]
        self.speed        = self.base_speed
        self.player_speed = 6

        # --- прокрутка дороги ---
        self.road_y  = 0

        # --- счёт ---
        self.score         = 0
        self.coins         = 0
        self.distance      = 0
        self.distance_px   = 0

        # --- трафик ---
        self.traffic: list[dict] = []
        self._spawn_traffic(2)

        # --- монеты ---
        self.coin_objs: list[dict] = []
        for _ in range(3):
            self.coin_objs.append(self._new_coin())

        # --- препятствия ---
        self.obstacles: list[dict] = []
        self.obs_timer = 0

        # --- полосовые опасности (static lane events) ---
        self.hazards: list[dict] = []
        self.hazard_timer = 0

        # --- powerup ---
        self.powerup_obj: PowerUp | None = None
        self.powerup_timer  = 0
        self.active_powerup = None
        self.powerup_end    = 0
        self.shield_active  = False
        self.nitro_active   = False

        # --- дорожные события (nitro strip, speed bump) ---
        self.road_events: list[dict] = []
        self.event_timer = 0

        # --- флаги ---
        self.tick = 0

    # -------- СПАВН --------
    def _safe_x(self):
        """X не над игроком."""
        while True:
            x = random.choice(LANE_XS)
            if abs(x - self.player_rect.centerx) > 60:
                return x

    def _spawn_traffic(self, count=1):
        for _ in range(count):
            x = self._safe_x()
            surf = _car_surface(60, 100, RED)
            rect = surf.get_rect(center=(x, random.randint(-300, -50)))
            self.traffic.append({"surf": surf, "rect": rect})

    def _new_coin(self):
        x = random.choice(LANE_XS)
        weights = [0.6, 0.3, 0.1]
        value   = random.choices([1, 2, 3], weights)[0]
        img_key = f"coin{value}"
        img     = self.assets[img_key]
        rect    = img.get_rect(center=(x, random.randint(-600, -50)))
        return {"img": img, "rect": rect, "value": value}

    def _new_obstacle(self):
        kind = random.choice(["oil", "barrier", "pothole"])
        x    = random.choice(LANE_XS)
        surf = _obstacle_surface(kind)
        rect = surf.get_rect(center=(x, -40))
        return {"surf": surf, "rect": rect, "kind": kind}

    def _new_hazard(self):
        """Опасная зона на полосе — замедляет."""
        lane = random.choice(LANE_XS)
        rect = pygame.Rect(lane - 35, -80, 70, 80)
        return {"rect": rect, "lane": lane, "active": False}

    def _new_road_event(self):
        kind = random.choice(["nitro_strip", "speed_bump"])
        x    = random.choice(LANE_XS)
        if kind == "nitro_strip":
            rect = pygame.Rect(x - 20, -60, 40, 60)
        else:
            rect = pygame.Rect(x - 35, -20, 70, 20)
        return {"kind": kind, "rect": rect}

    # -------- POWERUP --------
    def _try_spawn_powerup(self):
        if self.powerup_obj is None and random.random() < 0.004:
            x    = random.choice(LANE_XS)
            kind = random.choice(POWERUP_TYPES)
            self.powerup_obj = PowerUp(kind, x, -40)

    def _apply_powerup(self, kind):
        now = pygame.time.get_ticks()
        self.active_powerup = kind
        self.powerup_end    = now + POWERUP_DURATION
        if kind == "nitro":
            self.nitro_active = True
            self.speed        = self.base_speed + 6
        elif kind == "shield":
            self.shield_active = True
        elif kind == "repair":
            self.active_powerup = None  # мгновенный эффект

    # -------- UPDATE --------
    def update(self):
        now  = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        # движение игрока
        if keys[pygame.K_LEFT]  and self.player_rect.left  > ROAD_LEFT + 5:
            self.player_rect.x -= self.player_speed
        if keys[pygame.K_RIGHT] and self.player_rect.right < ROAD_RIGHT - 5:
            self.player_rect.x += self.player_speed

        # прокрутка дороги
        self.road_y = (self.road_y + self.speed) % HEIGHT

        # расстояние
        self.distance_px += self.speed
        self.distance     = self.distance_px // 60

        # счёт от дистанции
        self.score = self.coins * 10 + self.distance

        # --- powerup эффект истёк ---
        if self.active_powerup and now >= self.powerup_end:
            self.nitro_active  = False
            self.active_powerup = None
            self.speed = self.base_speed

        # --- скорость растёт с дистанцией ---
        inc = (self.distance // 100) * self.diff["enemy_inc"]
        self.base_speed = self.diff["enemy_start"] + inc
        if not self.nitro_active:
            self.speed = self.base_speed

        # --- трафик ---
        for t in self.traffic:
            t["rect"].y += self.speed
            if t["rect"].top > HEIGHT:
                t["rect"].center = (self._safe_x(), random.randint(-400, -80))

        # максимальное количество трафика
        while len(self.traffic) < min(2 + self.distance // 150, self.diff["traffic_max"]):
            self._spawn_traffic()

        # --- монеты ---
        for c in self.coin_objs:
            c["rect"].y += self.speed
            if c["rect"].top > HEIGHT:
                c["rect"].center = (random.choice(LANE_XS), random.randint(-400, -50))
                c["value"]  = random.choices([1,2,3], [0.6,0.3,0.1])[0]

        # --- препятствия ---
        self.obs_timer += 1
        if self.obs_timer >= self.diff["obs_freq"]:
            self.obstacles.append(self._new_obstacle())
            self.obs_timer = 0

        for obs in self.obstacles:
            obs["rect"].y += self.speed
        self.obstacles = [o for o in self.obstacles if o["rect"].top <= HEIGHT]

        # --- полосовые опасности ---
        self.hazard_timer += 1
        if self.hazard_timer >= 200:
            self.hazards.append(self._new_hazard())
            self.hazard_timer = 0
        for h in self.hazards:
            h["rect"].y += self.speed
        self.hazards = [h for h in self.hazards if h["rect"].top <= HEIGHT]

        # --- дорожные события ---
        self.event_timer += 1
        if self.event_timer >= 250:
            self.road_events.append(self._new_road_event())
            self.event_timer = 0
        for e in self.road_events:
            e["rect"].y += self.speed
        self.road_events = [e for e in self.road_events if e["rect"].top <= HEIGHT]

        # --- powerup ---
        self._try_spawn_powerup()
        if self.powerup_obj:
            self.powerup_obj.update(self.speed)
            if self.powerup_obj.off_screen() or self.powerup_obj.expired():
                self.powerup_obj = None

        self.tick += 1

    # -------- СТОЛКНОВЕНИЯ --------
    def check_collisions(self) -> str:
        """Возвращает 'ok' | 'dead'."""

        # монеты
        for c in self.coin_objs:
            if self.player_rect.colliderect(c["rect"]):
                self.coins += c["value"]
                c["rect"].center = (random.choice(LANE_XS), random.randint(-400, -50))
                c["value"] = random.choices([1,2,3],[0.6,0.3,0.1])[0]

        # трафик
        for t in self.traffic:
            if self.player_rect.colliderect(t["rect"]):
                if self.shield_active:
                    self.shield_active  = False
                    self.active_powerup = None
                    t["rect"].center = (self._safe_x(), random.randint(-400, -80))
                else:
                    return "dead"

        # препятствия
        for obs in self.obstacles[:]:
            if self.player_rect.colliderect(obs["rect"]):
                if obs["kind"] == "oil":
                    # замедление
                    self.speed = max(2, self.speed - 2)
                    self.obstacles.remove(obs)
                elif obs["kind"] == "barrier":
                    if self.shield_active:
                        self.shield_active  = False
                        self.active_powerup = None
                        self.obstacles.remove(obs)
                    else:
                        return "dead"
                else:  # pothole
                    self.speed = max(2, self.speed - 1)
                    self.obstacles.remove(obs)

        # дорожные события
        for e in self.road_events:
            if self.player_rect.colliderect(e["rect"]):
                if e["kind"] == "nitro_strip":
                    self.speed = min(self.base_speed + 8, 25)
                elif e["kind"] == "speed_bump":
                    self.speed = max(2, self.speed - 3)

        # powerup
        if self.powerup_obj and self.player_rect.colliderect(self.powerup_obj.rect):
            self._apply_powerup(self.powerup_obj.kind)
            self.powerup_obj = None

        return "ok"

    # -------- ОТРИСОВКА --------
    def draw(self):
        self.screen.fill(DARK)

        # дорога с прокруткой
        self.screen.blit(self.assets["road"], (0, self.road_y - HEIGHT))
        self.screen.blit(self.assets["road"], (0, self.road_y))
        _draw_road(self.screen)

        # полосовые опасности
        for h in self.hazards:
            s = pygame.Surface((h["rect"].w, h["rect"].h), pygame.SRCALPHA)
            s.fill((160, 30, 200, 70))
            self.screen.blit(s, h["rect"])
            lbl = self.font_sm.render("SLOW", True, (200, 100, 255))
            self.screen.blit(lbl, lbl.get_rect(center=h["rect"].center))

        # дорожные события
        for e in self.road_events:
            if e["kind"] == "nitro_strip":
                s = pygame.Surface((e["rect"].w, e["rect"].h), pygame.SRCALPHA)
                s.fill((255, 180, 0, 120))
                self.screen.blit(s, e["rect"])
                lbl = self.font_sm.render("NITRO", True, YELLOW)
                self.screen.blit(lbl, lbl.get_rect(center=e["rect"].center))
            else:
                pygame.draw.rect(self.screen, (100, 80, 50), e["rect"], border_radius=3)
                lbl = self.font_sm.render("BUMP", True, WHITE)
                self.screen.blit(lbl, lbl.get_rect(center=e["rect"].center))

        # препятствия
        for obs in self.obstacles:
            self.screen.blit(obs["surf"], obs["rect"])

        # монеты
        for c in self.coin_objs:
            self.screen.blit(c["img"], c["rect"])

        # трафик
        for t in self.traffic:
            self.screen.blit(t["surf"], t["rect"])

        # powerup
        if self.powerup_obj:
            self.powerup_obj.draw(self.screen, self.font_sm)

        # игрок
        self.screen.blit(self.player_surf, self.player_rect)

        # HUD
        self._draw_hud()

        pygame.display.update()

    def _draw_hud(self):
        pygame.draw.rect(self.screen, (20, 20, 30, 200), (0, 0, WIDTH, 50))
        sc  = self.font_md.render(f"Счёт: {self.score}", True, WHITE)
        dist = self.font_md.render(f"{self.distance}м", True, GREEN)
        cn  = self.font_md.render(f"🪙{self.coins}", True, YELLOW)
        self.screen.blit(sc,   (10,  14))
        self.screen.blit(dist, (160, 14))
        self.screen.blit(cn,   (270, 14))

        # активный powerup
        if self.active_powerup:
            now  = pygame.time.get_ticks()
            left = max(0, (self.powerup_end - now) // 1000)
            icon = POWERUP_ICONS.get(self.active_powerup, "?")
            color = POWERUP_COLORS.get(self.active_powerup, WHITE)
            pu = self.font_sm.render(f"{icon} {self.active_powerup.upper()} {left}s", True, color)
            self.screen.blit(pu, (10, HEIGHT - 30))

        # щит индикатор
        if self.shield_active:
            sh = self.font_sm.render("🛡 SHIELD", True, CYAN)
            self.screen.blit(sh, (WIDTH - 100, HEIGHT - 30))

    # -------- ЗАПУСК --------
    def run(self) -> dict:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

            self.update()
            result = self.check_collisions()
            self.draw()

            if result == "dead":
                return {
                    "score":    self.score,
                    "distance": self.distance,
                    "coins":    self.coins,
                }

            self.clock.tick(FPS)