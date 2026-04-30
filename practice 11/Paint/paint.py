import pygame, sys, math

# ===================== ИНИЦИАЛИЗАЦИЯ =====================
pygame.init()

# Размер окна
WIDTH, HEIGHT = 900, 650
PANEL_HEIGHT = 80  # нижняя панель интерфейса

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint (исправленный масштаб)")

# ===================== ХОЛСТ =====================
# Отдельная поверхность для рисования (чтобы рисунок сохранялся)
canvas = pygame.Surface((WIDTH, HEIGHT - PANEL_HEIGHT))
canvas.fill((255, 255, 255))  # белый фон

# ===================== ЦВЕТА =====================
# Словарь доступных цветов
COLORS = {
    "black": (0, 0, 0),
    "red":   (255, 0, 0),
    "green": (0, 255, 0),
    "blue":  (0, 0, 255)
}

# Текущий выбранный цвет
current_color = COLORS["black"]

# ===================== ИНСТРУМЕНТЫ =====================
tools = ["brush", "rect", "circle", "square", "triangle", "rhombus", "eraser"]
tool = "brush"  # текущий инструмент

# Шрифт для интерфейса
font = pygame.font.SysFont("Arial", 18)

# Часы для FPS
clock = pygame.time.Clock()

# ===================== UI КНОПКИ =====================
color_buttons = {}
tool_buttons = {}

# ---- КНОПКИ ЦВЕТОВ ----
x = 10
for name in COLORS:
    # создаём маленькие квадратные кнопки
    color_buttons[name] = pygame.Rect(x, HEIGHT - 40, 30, 30)
    x += 40

# ---- КНОПКИ ИНСТРУМЕНТОВ (с переносом строки) ----
x = 200
y = HEIGHT - 40

for t in tools:
    # ширина кнопки зависит от текста
    text_width = font.render(t, True, (0, 0, 0)).get_width() + 20

    # если не помещается в экран — перенос строки вверх
    if x + text_width > WIDTH:
        x = 200
        y -= 40

    tool_buttons[t] = pygame.Rect(x, y, text_width, 30)
    x += text_width + 10

# ===================== СОСТОЯНИЕ РИСОВАНИЯ =====================
drawing = False      # идёт ли сейчас рисование
start_pos = None     # начальная точка мыши

# ===================== ГЛАВНЫЙ ЦИКЛ =====================
while True:

    # фон интерфейса
    screen.fill((220, 220, 220))

    # отображаем холст (все рисунки сохраняются здесь)
    screen.blit(canvas, (0, 0))

    # ===================== СОБЫТИЯ =====================
    for event in pygame.event.get():

        # выход из программы
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ===================== НАЖАТИЕ МЫШИ =====================
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos  # координаты клика

            # ---- выбор цвета ----
            for name, rect in color_buttons.items():
                if rect.collidepoint(pos):
                    current_color = COLORS[name]
                    break

            # ---- выбор инструмента ----
            for t, rect in tool_buttons.items():
                if rect.collidepoint(pos):
                    tool = t
                    break

            # ---- начало рисования ----
            else:
                if pos[1] < HEIGHT - PANEL_HEIGHT:
                    drawing = True
                    start_pos = pos

        # ===================== ОТПУСКАНИЕ МЫШИ =====================
        if event.type == pygame.MOUSEBUTTONUP:

            if not drawing:
                continue

            # конечная точка
            x1, y1 = start_pos
            x2, y2 = event.pos

            # ---------------- НОРМАЛИЗАЦИЯ КООРДИНАТ ----------------
            # всегда приводим к "лево-верх + ширина/высота"
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)

            # ===================== ФИГУРЫ =====================

            # ---- прямоугольник ----
            if tool == "rect":
                rect = pygame.Rect(left, top, width, height)
                pygame.draw.rect(canvas, current_color, rect, 2)

            # ---- круг ----
            elif tool == "circle":
                # радиус = половина меньшей стороны
                radius = int(min(width, height) / 2)

                # центр круга
                center = (left + width // 2, top + height // 2)

                pygame.draw.circle(canvas, current_color, center, radius, 2)

            # ---- квадрат ----
            elif tool == "square":
                side = min(width, height)  # равные стороны

                rect = pygame.Rect(left, top, side, side)
                pygame.draw.rect(canvas, current_color, rect, 2)

            # ---- треугольник ----
            elif tool == "triangle":
                # обычный треугольник по bounding box
                points = [
                    (left, top),
                    (left + width, top),
                    (left + width // 2, top + height)
                ]
                pygame.draw.polygon(canvas, current_color, points, 2)

            # ---- ромб ----
            elif tool == "rhombus":
                # центр фигуры
                cx = left + width // 2
                cy = top + height // 2

                # вершины ромба
                points = [
                    (cx, top),           # верх
                    (left + width, cy),  # право
                    (cx, top + height),  # низ
                    (left, cy)           # лево
                ]
                pygame.draw.polygon(canvas, current_color, points, 2)

            # завершение рисования
            drawing = False

    # ===================== КИСТЬ / ЛАСТИК =====================
    if drawing:
        pos = pygame.mouse.get_pos()

        # кисть
        if tool == "brush":
            pygame.draw.circle(canvas, current_color, pos, 4)

        # ластик (рисует белым цветом)
        elif tool == "eraser":
            pygame.draw.circle(canvas, (255, 255, 255), pos, 10)

    # ===================== UI ОТРИСОВКА =====================

    # ---- кнопки цветов ----
    for name, rect in color_buttons.items():
        pygame.draw.rect(screen, COLORS[name], rect)

        # подсветка выбранного цвета
        if COLORS[name] == current_color:
            pygame.draw.rect(screen, (255, 255, 255), rect, 3)

    # ---- кнопки инструментов ----
    for t, rect in tool_buttons.items():
        pygame.draw.rect(screen, (180, 180, 180), rect)

        # текст кнопки
        text = font.render(t, True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

        # подсветка активного инструмента
        if t == tool:
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    # обновление экрана
    pygame.display.update()

    # FPS = 60
    clock.tick(60)