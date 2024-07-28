from random import randint
import math

MIN_LIMIT = 1
MAX_LIMIT = 100
RULES = 'Find the greatest common divisor of given numbers.'


def get_game():
    num_one = randint(MIN_LIMIT, MAX_LIMIT)
    num_two = randint(MIN_LIMIT, MAX_LIMIT)
    correct_answer = str(math.gcd(num_one, num_two))
    question = f'{num_one} {num_two}'
    return question, correct_answer
