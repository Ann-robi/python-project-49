import prompt

GAMES = 3


def start(game):
    """Приветствует игрока и реализует логику игр, в случае неправильного ответа - игра завершается, 
    для победы необходимо правильно ответить в трех раундах.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    index = 1

    while index <= GAMES:
        question, correct_answer = game.get_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        index = index + 1

    print(f'Congratulations, {name}!')
