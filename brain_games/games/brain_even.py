import random
from brain_games.games import games_engine


def is_number_even():
    min_problems_number, max_problems_number = 1, 100
    problems_number = random.randint(min_problems_number, max_problems_number)
    correct_answer = 'yes' if int(problems_number) % 2 == 0 else 'no'
    return [problems_number], correct_answer


games_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    games_engine.handler(is_number_even, games_question)


if __name__ == '__main__':
    main()
