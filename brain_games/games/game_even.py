from random import randint

MIN_LIMIT = 1
MAX_LIMIT = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    """Создает и возвращает вопрос со случайным числом
    и верный ответ для одного раунда.
    """
    random_number = randint(MIN_LIMIT, MAX_LIMIT)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    question = random_number
    return question, correct_answer


def is_even(random_number):
    """Возвращает True, если число четное,
    False - если нечетное.
    """
    return random_number % 2 == 0
