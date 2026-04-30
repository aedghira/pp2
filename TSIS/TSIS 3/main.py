import pygame
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer — TSIS 3")
clock = pygame.time.Clock()

from racer      import RacerGame, load_assets
from ui         import (screen_username, screen_main_menu,
                         screen_game_over, screen_leaderboard,
                         screen_settings)
from persistence import add_entry


def main():
    assets   = load_assets()
    username = screen_username(screen, clock)

    while True:
        action = screen_main_menu(screen, clock, username)

        if action == "quit":
            pygame.quit(); sys.exit()

        elif action == "leaderboard":
            screen_leaderboard(screen, clock)

        elif action == "settings":
            screen_settings(screen, clock)

        elif action == "play":
            while True:
                game   = RacerGame(screen, assets)
                result = game.run()

                add_entry(username, result["score"],
                          result["distance"], result["coins"])

                choice = screen_game_over(
                    screen, clock,
                    result["score"],
                    result["distance"],
                    result["coins"],
                )
                if choice == "menu":
                    break
                # "retry" — играть снова


if __name__ == "__main__":
    main()