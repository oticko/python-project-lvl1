import random
from brain_games.games import games_engine


def is_number_prime():
    min_problems_number, max_problems_number = 2, 3572
    problems_number = random.randint(min_problems_number, max_problems_number)
    correct_answer = "yes"
    if problems_number != 2 and problems_number % 2 == 0:
        correct_answer = "no"
    for divider in range(3, problems_number - 1, 2):
        if problems_number % divider == 0:
            correct_answer = "no"
            break
    return [problems_number], correct_answer


games_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    games_engine.handler(is_number_prime, games_question)


if __name__ == '__main__':
    main()
