import pygame
import sys
from persistence import load_leaderboard, save_settings, load_settings

# ===================== ЦВЕТА =====================
BG       = (15,  15,  25)
PANEL    = (30,  30,  45)
WHITE    = (240, 240, 240)
GRAY     = (150, 150, 160)
ACCENT   = (80,  200, 120)
ACCENT2  = (100, 160, 255)
RED      = (220, 60,  60)
YELLOW   = (255, 220, 40)
ORANGE   = (255, 150, 30)
BLACK    = (0,   0,   0)

WIDTH, HEIGHT = 400, 600


def _fonts():
    return {
        "sm":  pygame.font.SysFont("Arial", 16),
        "md":  pygame.font.SysFont("Arial", 22),
        "lg":  pygame.font.SysFont("Arial", 30, bold=True),
        "xl":  pygame.font.SysFont("Arial", 46, bold=True),
    }


def _draw_bg(screen):
    screen.fill(BG)
    # декоративные полосы дороги
    for i in range(0, HEIGHT, 60):
        alpha = 15
        s = pygame.Surface((WIDTH, 2))
        s.set_alpha(alpha)
        s.fill((255, 255, 255))
        screen.blit(s, (0, i))


def _btn(screen, font, rect, label, hover=False, active=False):
    color = ACCENT if active else (60, 120, 70) if hover else PANEL
    pygame.draw.rect(screen, color, rect, border_radius=8)
    pygame.draw.rect(screen, GRAY, rect, 1, border_radius=8)
    lbl = font.render(label, True, BLACK if (hover or active) else WHITE)
    screen.blit(lbl, lbl.get_rect(center=rect.center))


def _brect(cx, y, w=220, h=44):
    return pygame.Rect(cx - w // 2, y, w, h)


# ===================== ЭКРАН: ИМЯ =====================
def screen_username(screen, clock) -> str:
    F    = _fonts()
    name = ""
    cur  = True
    ct   = pygame.time.get_ticks()

    while True:
        _draw_bg(screen)
        mx, my = pygame.mouse.get_pos()

        t = F["xl"].render("🏎 RACER", True, YELLOW)
        screen.blit(t, t.get_rect(center=(WIDTH // 2, 100)))

        p = F["md"].render("Введите имя:", True, GRAY)
        screen.blit(p, p.get_rect(center=(WIDTH // 2, 220)))

        box = pygame.Rect(WIDTH // 2 - 130, 250, 260, 44)
        pygame.draw.rect(screen, PANEL, box, border_radius=8)
        pygame.draw.rect(screen, ACCENT2, box, 2, border_radius=8)

        now = pygame.time.get_ticks()
        if now - ct > 500:
            cur = not cur
            ct  = now
        display = name + ("|" if cur else "")
        nl = F["md"].render(display, True, WHITE)
        screen.blit(nl, (box.x + 10, box.y + 10))

        h = F["sm"].render("Enter — начать", True, (110, 110, 130))
        screen.blit(h, h.get_rect(center=(WIDTH // 2, 320)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    return name.strip()
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 18 and event.unicode.isprintable():
                    name += event.unicode

        pygame.display.update()
        clock.tick(60)


# ===================== ЭКРАН: МЕНЮ =====================
def screen_main_menu(screen, clock, username: str) -> str:
    F = _fonts()
    buttons = {
        "play":        _brect(WIDTH // 2, 200),
        "leaderboard": _brect(WIDTH // 2, 258),
        "settings":    _brect(WIDTH // 2, 316),
        "quit":        _brect(WIDTH // 2, 374),
    }
    labels = {
        "play":        "▶  Играть",
        "leaderboard": "🏆  Таблица лидеров",
        "settings":    "⚙  Настройки",
        "quit":        "✖  Выйти",
    }

    while True:
        _draw_bg(screen)
        mx, my = pygame.mouse.get_pos()

        t = F["xl"].render("🏎 RACER", True, YELLOW)
        screen.blit(t, t.get_rect(center=(WIDTH // 2, 90)))

        u = F["md"].render(f"Гонщик: {username}", True, ACCENT2)
        screen.blit(u, u.get_rect(center=(WIDTH // 2, 155)))

        for key, rect in buttons.items():
            _btn(screen, F["md"], rect, labels[key], hover=rect.collidepoint(mx, my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for key, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        return key

        pygame.display.update()
        clock.tick(60)


# ===================== ЭКРАН: GAME OVER =====================
def screen_game_over(screen, clock, score, distance, coins) -> str:
    F = _fonts()
    buttons = {
        "retry": _brect(WIDTH // 2 - 75, 460, 130),
        "menu":  _brect(WIDTH // 2 + 75, 460, 130),
    }

    while True:
        _draw_bg(screen)
        mx, my = pygame.mouse.get_pos()

        go = F["xl"].render("GAME OVER", True, RED)
        screen.blit(go, go.get_rect(center=(WIDTH // 2, 90)))

        for lbl, val, color in [
            (f"Счёт: {score}",          None, WHITE),
            (f"Дистанция: {distance} м", None, ACCENT),
            (f"Монет: {coins}",          None, YELLOW),
        ]:
            s = F["lg"].render(lbl, True, color)
            y = 190 + [WHITE, ACCENT, YELLOW].index(color) * 60
            screen.blit(s, s.get_rect(center=(WIDTH // 2, y)))

        _btn(screen, F["md"], buttons["retry"], "🔄 Ещё раз",  hover=buttons["retry"].collidepoint(mx, my))
        _btn(screen, F["md"], buttons["menu"],  "🏠 Меню",     hover=buttons["menu"].collidepoint(mx, my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for key, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        return key

        pygame.display.update()
        clock.tick(60)


# ===================== ЭКРАН: ЛИДЕРБОРД =====================
def screen_leaderboard(screen, clock):
    F       = _fonts()
    entries = load_leaderboard()
    back    = _brect(WIDTH // 2, HEIGHT - 60)

    col_x = [20, 50, 170, 280, 360]

    while True:
        _draw_bg(screen)
        mx, my = pygame.mouse.get_pos()

        t = F["lg"].render("🏆 Таблица лидеров", True, YELLOW)
        screen.blit(t, t.get_rect(center=(WIDTH // 2, 30)))

        headers = ["#", "Имя", "Счёт", "Дист.", "Монет"]
        for i, h in enumerate(headers):
            hl = F["sm"].render(h, True, ACCENT2)
            screen.blit(hl, (col_x[i], 75))
        pygame.draw.line(screen, GRAY, (10, 95), (WIDTH - 10, 95), 1)

        for rank, e in enumerate(entries, 1):
            y   = 100 + (rank - 1) * 34
            clr = YELLOW if rank == 1 else WHITE
            vals = [str(rank), e["name"][:12], str(e["score"]),
                    f'{e["distance"]}м', str(e["coins"])]
            for i, v in enumerate(vals):
                screen.blit(F["sm"].render(v, True, clr), (col_x[i], y))

        if not entries:
            msg = F["md"].render("Пока нет записей!", True, GRAY)
            screen.blit(msg, msg.get_rect(center=(WIDTH // 2, 250)))

        _btn(screen, F["md"], back, "◀ Назад", hover=back.collidepoint(mx, my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    return

        pygame.display.update()
        clock.tick(60)


# ===================== ЭКРАН: НАСТРОЙКИ =====================
def screen_settings(screen, clock):
    F        = _fonts()
    settings = load_settings()
    back     = _brect(WIDTH // 2, HEIGHT - 60)

    difficulties = ["easy", "normal", "hard"]
    car_colors   = ["default", "red", "blue", "yellow"]
    car_color_rgb = {
        "default": (80,  200, 120),
        "red":     (220, 60,  60),
        "blue":    (100, 160, 255),
        "yellow":  (255, 220, 40),
    }

    while True:
        _draw_bg(screen)
        mx, my = pygame.mouse.get_pos()

        t = F["lg"].render("⚙ Настройки", True, ACCENT2)
        screen.blit(t, t.get_rect(center=(WIDTH // 2, 35)))

        # --- звук ---
        sr = pygame.Rect(30, 90, 340, 42)
        son = settings.get("sound", False)
        pygame.draw.rect(screen, PANEL, sr, border_radius=8)
        pygame.draw.rect(screen, ACCENT if son else GRAY, sr, 2, border_radius=8)
        screen.blit(F["md"].render(f"Звук: {'ВКЛ' if son else 'ВЫКЛ'}", True, WHITE), (sr.x + 14, sr.y + 10))

        # --- сложность ---
        screen.blit(F["md"].render("Сложность:", True, GRAY), (30, 148))
        for i, d in enumerate(difficulties):
            dr = pygame.Rect(30 + i * 115, 178, 105, 38)
            active = settings.get("difficulty") == d
            pygame.draw.rect(screen, ACCENT if active else PANEL, dr, border_radius=6)
            pygame.draw.rect(screen, GRAY, dr, 1, border_radius=6)
            screen.blit(F["sm"].render(d.upper(), True, BLACK if active else WHITE),
                        F["sm"].render(d.upper(), True, WHITE).get_rect(center=dr.center))

        # --- цвет машины ---
        screen.blit(F["md"].render("Цвет машины:", True, GRAY), (30, 232))
        for i, cc in enumerate(car_colors):
            cr = pygame.Rect(30 + i * 85, 262, 75, 38)
            active = settings.get("car_color") == cc
            pygame.draw.rect(screen, car_color_rgb[cc], cr, border_radius=6)
            pygame.draw.rect(screen, WHITE if active else GRAY, cr, 2 if active else 1, border_radius=6)
            lbl = F["sm"].render(cc[:3].upper(), True, BLACK)
            screen.blit(lbl, lbl.get_rect(center=cr.center))

        _btn(screen, F["md"], back, "💾 Сохранить", hover=back.collidepoint(mx, my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if sr.collidepoint(pos):
                    settings["sound"] = not settings.get("sound", False)
                for i, d in enumerate(difficulties):
                    dr = pygame.Rect(30 + i * 115, 178, 105, 38)
                    if dr.collidepoint(pos):
                        settings["difficulty"] = d
                for i, cc in enumerate(car_colors):
                    cr = pygame.Rect(30 + i * 85, 262, 75, 38)
                    if cr.collidepoint(pos):
                        settings["car_color"] = cc
                if back.collidepoint(pos):
                    save_settings(settings)
                    return

        pygame.display.update()
        clock.tick(60)