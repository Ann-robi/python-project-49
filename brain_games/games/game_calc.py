from random import randint
from random import choice

MIN_LIMIT = 1
MAX_LIMIT = 30
RULES = 'What is the result of the expression?'


def get_game():
    num_one = randint(MIN_LIMIT, MAX_LIMIT)
    num_two = randint(MIN_LIMIT, MAX_LIMIT)
    operator = choice(['+', '-', '*'])
    correct_answer = str(is_calculator(num_one, num_two, operator))
    question = f'{num_one} {operator} {num_two}'
    return question, correct_answer


def is_calculator(num_one, num_two, operator):
    if operator == '+':
        result = num_one + num_two
    elif operator == '-':
        result = num_one - num_two
    elif operator == '*':
        result = num_one * num_two
    return result
