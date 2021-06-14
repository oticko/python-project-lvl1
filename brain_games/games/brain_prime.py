import random
from brain_games.engine import games_engine
MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB = 2, 3572


def is_number_prime():
    problems_number = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    correct_answer = "yes"
    if problems_number != 2 and problems_number % 2 == 0 or problems_number < 2:
        correct_answer = "no"
    for divider in range(3, problems_number - 1, 2):
        if problems_number % divider == 0:
            correct_answer = "no"
            break
    return problems_number, correct_answer


games_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    games_engine.handler(is_number_prime, games_question)


if __name__ == '__main__':
    main()
