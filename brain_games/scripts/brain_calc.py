#!/usr/bin/env python3

from brain_games.games import game_calc
from brain_games.logic_games import start


def main():
    """Запускает игру."""
    start(game_calc)


if __name__ == '__main__':
    main()
