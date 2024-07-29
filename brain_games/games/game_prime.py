from random import randint
from math import sqrt

MIN_LIMIT = 2
MAX_LIMIT = 150
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game():
    random_number = randint(MIN_LIMIT, MAX_LIMIT)
    i = 2
    while i <= sqrt(random_number):
        if random_number % i == 0:
            correct_answer = 'no'
            break
        i += 1
    else:
        correct_answer = 'yes'
    question = random_number
    return question, correct_answer
