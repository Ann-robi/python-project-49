from random import randint

MIN_LIMIT = 1
MAX_LIMIT = 20
MIN_STEP = 1
MAX_STEP = 5
MIN_LENGTH = 5
MAX_LENGTH = 10
RULES = 'What number is missing in the progression?'


def get_game():
    """Возвращает вопрос с прогрессией и верный ответ для одного раунда."""
    start = randint(MIN_LIMIT, MAX_LIMIT)
    step = randint(MIN_STEP, MAX_STEP)
    length = randint(MIN_LENGTH, MAX_LENGTH)
    stop = start + (step * length)
    progression = list(range(start, stop, step))
    correct_answer_index = randint(0, (len(progression) - 1))
    correct_answer = progression[correct_answer_index]
    progression[correct_answer_index] = '..'
    str_progression = [str(n) for n in progression]
    question = ' '.join(str_progression)
    return question, correct_answer
