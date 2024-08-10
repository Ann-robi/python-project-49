from random import randint
from math import sqrt

MIN_LIMIT = 2
MAX_LIMIT = 150
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game():
    """Создает и возвращает вопрос со случайным числом и верный ответ для одного раунда."""
    random_number = randint(MIN_LIMIT, MAX_LIMIT)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    question = random_number
    return question, correct_answer

def is_prime(random_number):
    """Возвращает True, если число простое, False - если составное или 0 или 1."""
    i = 2
    while i <= sqrt(random_number):
        if random_number % i == 0:
                return False
        i += 1
        if random_number > 1:
            return True
