import pygame
import sys
import math
import collections
from datetime import datetime

# ===================== ИНИЦИАЛИЗАЦИЯ =====================
pygame.init()

WIDTH, HEIGHT = 1000, 700
PANEL_HEIGHT = 90

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint — TSIS 2")

# ===================== ХОЛСТ =====================
canvas = pygame.Surface((WIDTH, HEIGHT - PANEL_HEIGHT))
canvas.fill((255, 255, 255))

# Preview surface (for live shape previews — not saved to canvas)
preview = pygame.Surface((WIDTH, HEIGHT - PANEL_HEIGHT), pygame.SRCALPHA)

# ===================== ЦВЕТА =====================
COLORS = {
    "black":  (0,   0,   0),
    "red":    (255, 0,   0),
    "green":  (0,   200, 0),
    "blue":   (0,   0,   255),
    "yellow": (255, 220, 0),
    "orange": (255, 140, 0),
    "purple": (160, 0,   200),
    "white":  (255, 255, 255),
    "cyan":   (0,   200, 220),
    "pink":   (255, 100, 180),
}

current_color = COLORS["black"]

# ===================== ИНСТРУМЕНТЫ =====================
tools = ["pencil", "line", "brush", "rect", "circle",
         "square", "triangle", "rhombus", "fill", "text", "eraser"]
tool = "pencil"

# ===================== РАЗМЕР КИСТИ =====================
BRUSH_SIZES = {"small": 2, "medium": 5, "large": 10}
brush_size = BRUSH_SIZES["small"]

# ===================== ШРИФТЫ =====================
font_ui   = pygame.font.SysFont("Arial", 15)
font_text = pygame.font.SysFont("Arial", 22)

clock = pygame.time.Clock()

# ===================== UI — КНОПКИ =====================
UI_BG   = (50,  50,  60)
UI_BTN  = (80,  80,  95)
UI_ACT  = (100, 180, 255)
UI_TXT  = (230, 230, 230)

PANEL_Y = HEIGHT - PANEL_HEIGHT

def make_btn(x, y, w, h, label):
    return {"rect": pygame.Rect(x, y, w, h), "label": label}

color_buttons = {}
x = 10
for name in COLORS:
    color_buttons[name] = pygame.Rect(x, PANEL_Y + 8, 28, 28)
    x += 32

size_buttons = {}
size_x = 10
for sname in BRUSH_SIZES:
    size_buttons[sname] = pygame.Rect(size_x, PANEL_Y + 50, 56, 24)
    size_x += 62

tool_buttons = {}
x = 330
y = PANEL_Y + 8
for t in tools:
    w = font_ui.render(t, True, UI_TXT).get_width() + 20
    if x + w > WIDTH - 10:
        x = 330
        y += 34
    tool_buttons[t] = pygame.Rect(x, y, w, 28)
    x += w + 6

# ===================== СОСТОЯНИЕ =====================
drawing    = False
start_pos  = None
prev_pos   = None   # для pencil (соединение точек)

# ---- Текстовый инструмент ----
text_active   = False
text_pos      = None
text_buffer   = ""

# ===================== FLOOD FILL =====================
def flood_fill(surface, x, y, fill_color):
    """BFS flood fill прямо по пикселям поверхности."""
    if x < 0 or y < 0 or x >= surface.get_width() or y >= surface.get_height():
        return

    target_color = surface.get_at((x, y))[:3]
    fill_rgb     = fill_color[:3]

    if target_color == fill_rgb:
        return  # уже нужный цвет

    queue = collections.deque()
    queue.append((x, y))
    visited = set()
    visited.add((x, y))

    W = surface.get_width()
    H = surface.get_height()

    while queue:
        cx, cy = queue.popleft()
        if surface.get_at((cx, cy))[:3] != target_color:
            continue
        surface.set_at((cx, cy), fill_rgb)

        for nx, ny in ((cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)):
            if 0 <= nx < W and 0 <= ny < H and (nx,ny) not in visited:
                if surface.get_at((nx, ny))[:3] == target_color:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

# ===================== РИСОВАНИЕ ФИГУР =====================
def draw_shape(surface, shape, color, start, end, size):
    x1, y1 = start
    x2, y2 = end

    left   = min(x1, x2)
    top    = min(y1, y2)
    width  = abs(x2 - x1)
    height = abs(y2 - y1)

    if shape == "line":
        pygame.draw.line(surface, color, start, end, size)

    elif shape == "rect":
        pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height), size)

    elif shape == "circle":
        r = int(min(width, height) / 2)
        cx = left + width  // 2
        cy = top  + height // 2
        if r > 0:
            pygame.draw.circle(surface, color, (cx, cy), r, size)

    elif shape == "square":
        side = min(width, height)
        pygame.draw.rect(surface, color, pygame.Rect(left, top, side, side), size)

    elif shape == "triangle":
        if width > 0 and height > 0:
            pts = [
                (left,            top),
                (left + width,    top),
                (left + width//2, top + height),
            ]
            pygame.draw.polygon(surface, color, pts, size)

    elif shape == "rhombus":
        if width > 0 and height > 0:
            cx = left + width  // 2
            cy = top  + height // 2
            pts = [(cx, top), (left+width, cy), (cx, top+height), (left, cy)]
            pygame.draw.polygon(surface, color, pts, size)

# ===================== ОТРИСОВКА UI =====================
def draw_ui():
    pygame.draw.rect(screen, UI_BG, (0, PANEL_Y, WIDTH, PANEL_HEIGHT))
    pygame.draw.line(screen, (100, 100, 120), (0, PANEL_Y), (WIDTH, PANEL_Y), 2)

    # --- цвета ---
    for name, rect in color_buttons.items():
        pygame.draw.rect(screen, COLORS[name], rect)
        pygame.draw.rect(screen, (200, 200, 200), rect, 1)
        if COLORS[name] == current_color:
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            pygame.draw.rect(screen, (0,   0,   0),   rect.inflate(2,2), 1)

    # --- текущий цвет (крупный квадрат) ---
    cc_rect = pygame.Rect(WIDTH - 55, PANEL_Y + 8, 44, 44)
    pygame.draw.rect(screen, current_color, cc_rect)
    pygame.draw.rect(screen, (200,200,200), cc_rect, 2)
    lbl = font_ui.render("color", True, UI_TXT)
    screen.blit(lbl, (WIDTH - 55, PANEL_Y + 56))

    # --- размеры кисти ---
    size_names = list(BRUSH_SIZES.keys())
    for i, (sname, rect) in enumerate(size_buttons.items()):
        active = BRUSH_SIZES[sname] == brush_size
        pygame.draw.rect(screen, UI_ACT if active else UI_BTN, rect, border_radius=4)
        lbl = font_ui.render(f"{sname[0].upper()} [{i+1}]", True, (0,0,0) if active else UI_TXT)
        screen.blit(lbl, lbl.get_rect(center=rect.center))

    # --- инструменты ---
    for t, rect in tool_buttons.items():
        active = t == tool
        pygame.draw.rect(screen, UI_ACT if active else UI_BTN, rect, border_radius=4)
        lbl = font_ui.render(t, True, (0,0,0) if active else UI_TXT)
        screen.blit(lbl, lbl.get_rect(center=rect.center))

    # --- подсказки ---
    hints = font_ui.render("Ctrl+S = сохранить  |  1/2/3 = размер кисти  |  Esc = отменить текст", True, (150,150,170))
    screen.blit(hints, (330, PANEL_Y + 68))

# ===================== ГЛАВНЫЙ ЦИКЛ =====================
while True:
    screen.fill((30, 30, 35))
    screen.blit(canvas, (0, 0))

    # ---- live preview для линий и фигур ----
    preview.fill((0, 0, 0, 0))
    if drawing and start_pos and tool in ("line","rect","circle","square","triangle","rhombus"):
        cur = pygame.mouse.get_pos()
        if cur[1] < PANEL_Y:
            draw_shape(preview, tool, current_color + (180,), start_pos, cur, brush_size)
    screen.blit(preview, (0, 0))

    # ---- текстовый курсор ----
    if text_active and text_pos:
        rendered = font_text.render(text_buffer + "|", True, current_color)
        screen.blit(rendered, text_pos)

    draw_ui()

    # ===================== СОБЫТИЯ =====================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---- клавиатура ----
        if event.type == pygame.KEYDOWN:

            # размер кисти
            if event.key == pygame.K_1:
                brush_size = BRUSH_SIZES["small"]
            elif event.key == pygame.K_2:
                brush_size = BRUSH_SIZES["medium"]
            elif event.key == pygame.K_3:
                brush_size = BRUSH_SIZES["large"]

            # сохранение
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                fname = f"canvas_{ts}.png"
                pygame.image.save(canvas, fname)
                pygame.display.set_caption(f"Paint — сохранено: {fname}")

            # текстовый инструмент
            elif text_active:
                if event.key == pygame.K_RETURN:
                    # зафиксировать текст на холсте
                    rendered = font_text.render(text_buffer, True, current_color)
                    canvas.blit(rendered, text_pos)
                    text_active  = False
                    text_buffer  = ""
                    text_pos     = None
                elif event.key == pygame.K_ESCAPE:
                    text_active  = False
                    text_buffer  = ""
                    text_pos     = None
                elif event.key == pygame.K_BACKSPACE:
                    text_buffer = text_buffer[:-1]
                else:
                    if event.unicode and event.unicode.isprintable():
                        text_buffer += event.unicode

        # ---- нажатие мыши ----
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # цвет
            for name, rect in color_buttons.items():
                if rect.collidepoint(pos):
                    current_color = COLORS[name]
                    break

            # размер кисти
            for sname, rect in size_buttons.items():
                if rect.collidepoint(pos):
                    brush_size = BRUSH_SIZES[sname]
                    break

            # инструмент
            for t, rect in tool_buttons.items():
                if rect.collidepoint(pos):
                    tool = t
                    text_active = False
                    break

            # рисование на холсте
            else:
                if pos[1] < PANEL_Y:
                    # flood fill — сразу
                    if tool == "fill":
                        flood_fill(canvas, pos[0], pos[1], current_color)

                    # текстовый инструмент
                    elif tool == "text":
                        text_active = True
                        text_pos    = pos
                        text_buffer = ""

                    # начало рисования
                    else:
                        drawing   = True
                        start_pos = pos
                        prev_pos  = pos

        # ---- движение мыши (pencil / brush / eraser) ----
        if event.type == pygame.MOUSEMOTION and drawing:
            pos = event.pos
            if pos[1] < PANEL_Y:

                if tool == "pencil":
                    if prev_pos:
                        pygame.draw.line(canvas, current_color, prev_pos, pos, brush_size)
                    prev_pos = pos

                elif tool == "brush":
                    pygame.draw.circle(canvas, current_color, pos, brush_size * 2)

                elif tool == "eraser":
                    pygame.draw.circle(canvas, (255, 255, 255), pos, brush_size * 3 + 4)

        # ---- отпускание мыши ----
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                end = event.pos

                if tool in ("line","rect","circle","square","triangle","rhombus"):
                    draw_shape(canvas, tool, current_color, start_pos, end, brush_size)

            drawing   = False
            start_pos = None
            prev_pos  = None

    pygame.display.update()
    clock.tick(60)