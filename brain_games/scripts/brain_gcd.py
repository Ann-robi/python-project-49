#!/usr/bin/env python3

from brain_games.games import game_gcd
from brain_games.logic_games import start


def main():
    """Запускает игру."""
    start(game_gcd)


if __name__ == '__main__':
    main()
