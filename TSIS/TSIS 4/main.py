import pygame
import sys
import json

from config import *
from game   import SnakeGame, load_settings, save_settings
import db


# ===================== ИНИЦИАЛИЗАЦИЯ =====================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake — TSIS 3")
clock  = pygame.time.Clock()

# шрифты
F_SM  = pygame.font.SysFont("Arial", 16)
F_MD  = pygame.font.SysFont("Arial", 22)
F_LG  = pygame.font.SysFont("Arial", 32, bold=True)
F_XL  = pygame.font.SysFont("Arial", 48, bold=True)


# ===================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =====================
def txt(font, text, color):
    return font.render(text, True, color)


def centered(surf, y):
    return (WIDTH // 2 - surf.get_width() // 2, y)


def draw_bg():
    screen.fill(DARKER)
    for y in range(0, HEIGHT, CELL_SIZE):
        for x in range(0, WIDTH, CELL_SIZE):
            if (x // CELL_SIZE + y // CELL_SIZE) % 2 == 0:
                pygame.draw.rect(screen, (28, 28, 36), (x, y, CELL_SIZE, CELL_SIZE))


def btn_rect(cx, y, w=220, h=44):
    return pygame.Rect(cx - w // 2, y, w, h)


def draw_btn(rect, label, active=False, hover=False):
    color = ACCENT if active else ((80, 120, 80) if hover else (55, 60, 70))
    pygame.draw.rect(screen, color, rect, border_radius=8)
    pygame.draw.rect(screen, GRAY, rect, 1, border_radius=8)
    lbl = F_MD.render(label, True, BLACK if active else WHITE)
    screen.blit(lbl, lbl.get_rect(center=rect.center))


# ===================== ЭКРАН: ВВОД ИМЕНИ =====================
def screen_username() -> str:
    username  = ""
    cursor_on = True
    cursor_t  = pygame.time.get_ticks()

    while True:
        draw_bg()
        mx, my = pygame.mouse.get_pos()

        title = F_XL.render("🐍 SNAKE", True, ACCENT)
        screen.blit(title, centered(title, 80))

        prompt = F_MD.render("Введите имя игрока:", True, GRAY)
        screen.blit(prompt, centered(prompt, 200))

        # поле ввода
        box = pygame.Rect(WIDTH // 2 - 150, 240, 300, 44)
        pygame.draw.rect(screen, (60, 65, 75), box, border_radius=8)
        pygame.draw.rect(screen, ACCENT2, box, 2, border_radius=8)

        now = pygame.time.get_ticks()
        if now - cursor_t > 500:
            cursor_on = not cursor_on
            cursor_t  = now
        display = username + ("|" if cursor_on else "")
        utext = F_MD.render(display, True, WHITE)
        screen.blit(utext, (box.x + 10, box.y + 10))

        hint = F_SM.render("Нажмите Enter чтобы начать", True, (120, 120, 140))
        screen.blit(hint, centered(hint, 310))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username.strip():
                    return username.strip()
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif len(username) < 20 and event.unicode.isprintable():
                    username += event.unicode

        pygame.display.update()
        clock.tick(60)


# ===================== ЭКРАН: ГЛАВНОЕ МЕНЮ =====================
def screen_main_menu(username: str) -> str:
    """Возвращает: 'play' | 'leaderboard' | 'settings' | 'quit'"""
    buttons = {
        "play":        btn_rect(WIDTH // 2, 200),
        "leaderboard": btn_rect(WIDTH // 2, 260),
        "settings":    btn_rect(WIDTH // 2, 320),
        "quit":        btn_rect(WIDTH // 2, 380),
    }
    labels = {
        "play":        "▶  Играть",
        "leaderboard": "🏆  Таблица лидеров",
        "settings":    "⚙  Настройки",
        "quit":        "✖  Выйти",
    }

    while True:
        draw_bg()
        mx, my = pygame.mouse.get_pos()

        title = F_XL.render("🐍 SNAKE", True, ACCENT)
        screen.blit(title, centered(title, 80))

        user_lbl = F_MD.render(f"Игрок: {username}", True, ACCENT2)
        screen.blit(user_lbl, centered(user_lbl, 150))

        for key, rect in buttons.items():
            draw_btn(rect, labels[key], hover=rect.collidepoint(mx, my))

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
def screen_game_over(score: int, level: int, personal_best: int) -> str:
    """Возвращает: 'retry' | 'menu'"""
    buttons = {
        "retry": btn_rect(WIDTH // 2 - 120, 380),
        "menu":  btn_rect(WIDTH // 2 + 120, 380),
    }

    while True:
        draw_bg()
        mx, my = pygame.mouse.get_pos()

        go = F_XL.render("GAME OVER", True, RED)
        screen.blit(go, centered(go, 80))

        sc_lbl  = F_LG.render(f"Счёт: {score}",         True, WHITE)
        lv_lbl  = F_LG.render(f"Уровень: {level}",       True, ACCENT)
        pb_lbl  = F_MD.render(f"Личный рекорд: {personal_best}", True, ACCENT2)

        screen.blit(sc_lbl,  centered(sc_lbl,  200))
        screen.blit(lv_lbl,  centered(lv_lbl,  250))
        screen.blit(pb_lbl,  centered(pb_lbl,  305))

        draw_btn(buttons["retry"], "🔄  Ещё раз", hover=buttons["retry"].collidepoint(mx, my))
        draw_btn(buttons["menu"],  "🏠  Меню",    hover=buttons["menu"].collidepoint(mx, my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for key, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        return key

        pygame.display.update()
        clock.tick(60)


# ===================== ЭКРАН: ТАБЛИЦА ЛИДЕРОВ =====================
def screen_leaderboard():
    rows    = db.get_leaderboard(10)
    back    = btn_rect(WIDTH // 2, HEIGHT - 60)
    headers = ["#", "Игрок", "Счёт", "Уровень", "Дата"]
    col_x   = [30, 70, 260, 360, 450]

    while True:
        draw_bg()
        mx, my = pygame.mouse.get_pos()

        title = F_LG.render("🏆 Таблица лидеров", True, YELLOW)
        screen.blit(title, centered(title, 20))

        # заголовок таблицы
        for i, h in enumerate(headers):
            hl = F_SM.render(h, True, ACCENT2)
            screen.blit(hl, (col_x[i], 80))
        pygame.draw.line(screen, GRAY, (20, 100), (WIDTH - 20, 100), 1)

        for row in rows:
            y   = 108 + (row["rank"] - 1) * 30
            clr = YELLOW if row["rank"] == 1 else WHITE
            vals = [str(row["rank"]), row["name"], str(row["score"]),
                    str(row["level"]), row["date"]]
            for i, v in enumerate(vals):
                screen.blit(F_SM.render(v, True, clr), (col_x[i], y))

        if not rows:
            msg = F_MD.render("Нет записей. Сыграйте первым!", True, GRAY)
            screen.blit(msg, centered(msg, 200))

        draw_btn(back, "◀  Назад", hover=back.collidepoint(mx, my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(event.pos):
                    return

        pygame.display.update()
        clock.tick(60)


# ===================== ЭКРАН: НАСТРОЙКИ =====================
def screen_settings():
    settings = load_settings()

    color_options = [
        ("Зелёный",   [80,  200, 120]),
        ("Синий",     [100, 160, 255]),
        ("Оранжевый", [255, 140, 30]),
        ("Розовый",   [255, 105, 180]),
        ("Белый",     [240, 240, 240]),
    ]
    selected_color = tuple(settings.get("snake_color", [80, 200, 120]))

    back = btn_rect(WIDTH // 2, HEIGHT - 60)

    while True:
        draw_bg()
        mx, my = pygame.mouse.get_pos()

        title = F_LG.render("⚙ Настройки", True, ACCENT2)
        screen.blit(title, centered(title, 30))

        # --- цвет змейки ---
        screen.blit(F_MD.render("Цвет змейки:", True, WHITE), (50, 110))
        for i, (name, rgb) in enumerate(color_options):
            rx = 50 + i * 120
            rect = pygame.Rect(rx, 145, 100, 36)
            active = tuple(rgb) == selected_color
            pygame.draw.rect(screen, tuple(rgb), rect, border_radius=6)
            pygame.draw.rect(screen, WHITE if active else GRAY, rect, 2 if active else 1, border_radius=6)
            lbl = F_SM.render(name, True, BLACK)
            screen.blit(lbl, lbl.get_rect(center=rect.center))
            if event_click := (pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
                pass  # обработка ниже

        # --- сетка ---
        grid_rect = pygame.Rect(50, 220, 300, 40)
        grid_on   = settings.get("grid", False)
        pygame.draw.rect(screen, (55, 65, 75), grid_rect, border_radius=8)
        pygame.draw.rect(screen, ACCENT if grid_on else GRAY, grid_rect, 2, border_radius=8)
        screen.blit(F_MD.render(f"Сетка: {'ВКЛ' if grid_on else 'ВЫКЛ'}", True, WHITE),
                    (grid_rect.x + 15, grid_rect.y + 8))

        # --- звук ---
        snd_rect = pygame.Rect(50, 280, 300, 40)
        snd_on   = settings.get("sound", False)
        pygame.draw.rect(screen, (55, 65, 75), snd_rect, border_radius=8)
        pygame.draw.rect(screen, ACCENT if snd_on else GRAY, snd_rect, 2, border_radius=8)
        screen.blit(F_MD.render(f"Звук: {'ВКЛ' if snd_on else 'ВЫКЛ'}", True, WHITE),
                    (snd_rect.x + 15, snd_rect.y + 8))

        draw_btn(back, "💾  Сохранить и выйти", hover=back.collidepoint(mx, my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                # цвет змейки
                for i, (name, rgb) in enumerate(color_options):
                    rx   = 50 + i * 120
                    rect = pygame.Rect(rx, 145, 100, 36)
                    if rect.collidepoint(pos):
                        selected_color = tuple(rgb)
                        settings["snake_color"] = list(rgb)

                # сетка
                if grid_rect.collidepoint(pos):
                    settings["grid"] = not settings.get("grid", False)

                # звук
                if snd_rect.collidepoint(pos):
                    settings["sound"] = not settings.get("sound", False)

                # назад / сохранить
                if back.collidepoint(pos):
                    save_settings(settings)
                    return

        pygame.display.update()
        clock.tick(60)


# ===================== ГЛАВНЫЙ ПОТОК =====================
def main():
    # БД
    db_ok = db.init_db()
    if not db_ok:
        print("[WARN] База данных недоступна — прогресс не сохранится.")

    # имя игрока
    username  = screen_username()
    player_id = db.get_or_create_player(username) if db_ok else None

    while True:
        action = screen_main_menu(username)

        if action == "quit":
            pygame.quit(); sys.exit()

        elif action == "leaderboard":
            screen_leaderboard()

        elif action == "settings":
            screen_settings()

        elif action == "play":
            while True:
                settings     = load_settings()
                personal_best = db.get_personal_best(player_id) if player_id else 0

                game   = SnakeGame(screen, personal_best, settings)
                result = game.run()

                # сохраняем в БД
                if player_id:
                    db.save_session(player_id, result["score"], result["level"])
                    new_best = db.get_personal_best(player_id)
                else:
                    new_best = max(personal_best, result["score"])

                choice = screen_game_over(result["score"], result["level"], new_best)
                if choice == "menu":
                    break
                # 'retry' — заново


if __name__ == "__main__":
    main()