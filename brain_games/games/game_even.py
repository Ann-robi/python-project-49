from random import randint

MIN_LIMIT = 1
MAX_LIMIT = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    random_number = randint(MIN_LIMIT, MAX_LIMIT)
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = random_number
    return question, correct_answer


def is_even(random_number):
    return random_number % 2 == 0
