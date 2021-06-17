import prompt
NUMBER_OF_ROUNDS = 3


def welcome_speech(games_question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(games_question)
    return name


def play_game(game, games_question):
    name = welcome_speech(games_question)
    for _ in range(NUMBER_OF_ROUNDS):
        problem, correct_answer = game()
        correct_answer = str(correct_answer)
        print('Question:', problem)
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            (print('{!r} is wrong answer ;(. Correct answer was {!r}.'.
                   format(user_answer, correct_answer)))
            print("Let's try again, {}!".format(name))
            break
        print('Correct!')
    if correct_answer == user_answer:
        print('Congratulations, {}!'.format(name))
