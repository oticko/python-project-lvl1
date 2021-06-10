import prompt


def welcome_speech(games_question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(games_question)
    return name


def handler(game, games_question):
    name = welcome_speech(games_question)
    current_round = 0
    number_of_rounds = 3
    while current_round < number_of_rounds:
        game_results = game()
        problem = game_results[0]
        correct_answer = str(game_results[1])
        print('Question: ', *problem)
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            (print('{!r} is wrong answer ;(. Correct answer was {!r}.'.
                   format(user_answer, correct_answer)))
            print("Let's try again, {}!".format(name))
            break
        print('Correct!')
        current_round += 1
    if current_round == number_of_rounds:
        print('Congratulations, {}!'.format(name))


def main():
    handler()


if __name__ == '__main__':
    main()
