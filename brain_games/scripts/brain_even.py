#!/usr/bin/env python3

from brain_games.games import game_even
from brain_games.logic_games import start


def main():
    """Запускает игру."""
    start(game_even)


if __name__ == '__main__':
    main()
