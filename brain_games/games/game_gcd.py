from random import randint
import math

MIN_LIMIT = 1
MAX_LIMIT = 100
RULES = 'Find the greatest common divisor of given numbers.'


def get_game():
    """Создает и возвращает вопрос с двумя случайными числами и верный ответ для одного раунда."""
    num_one = randint(MIN_LIMIT, MAX_LIMIT)
    num_two = randint(MIN_LIMIT, MAX_LIMIT)
    correct_answer = math.gcd(num_one, num_two)
    question = f'{num_one} {num_two}'
    return question, correct_answer
