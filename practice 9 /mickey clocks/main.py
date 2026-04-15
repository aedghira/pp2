import pygame
import datetime
import os
import sys

WIDTH, HEIGHT = 600, 600
CENTER = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


script_dir = os.path.dirname(os.path.abspath(__file__))

bg = pygame.image.load(os.path.join(script_dir, "mickey.jpg")).convert_alpha()
bg = pygame.transform.smoothscale(bg, (WIDTH, HEIGHT))

sec_hand = pygame.image.load(os.path.join(script_dir, "left.png")).convert_alpha()
min_hand = pygame.image.load(os.path.join(script_dir, "right.png")).convert_alpha()

sec_hand = pygame.transform.smoothscale(sec_hand, (110, 195))
min_hand = pygame.transform.smoothscale(min_hand, (110, 180))

sec_pivot = pygame.math.Vector2(100, 188)
min_pivot = pygame.math.Vector2(10, 175)


def rotate_around_pivot(image, angle, pivot, target_pos):
    image_center = pygame.math.Vector2(image.get_rect().center)

    offset = pivot - image_center

    rotated_offset = offset.rotate(angle)

    rotated_center = target_pos - rotated_offset

    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect(center=rotated_center)

    return rotated_image, rect


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()

    seconds = now.second + now.microsecond / 1_000_000
    minutes = now.minute + seconds / 60

    sec_angle = (seconds / 60) * 360
    min_angle = (minutes / 60) * 360
    screen.fill((20, 20, 20))
    screen.blit(bg, (0, 0))

    sec_img, sec_rect = rotate_around_pivot(
        sec_hand, sec_angle, sec_pivot, CENTER
    )
    screen.blit(sec_img, sec_rect)
    min_img, min_rect = rotate_around_pivot(
        min_hand, min_angle, min_pivot, CENTER
    )
    screen.blit(min_img, min_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()