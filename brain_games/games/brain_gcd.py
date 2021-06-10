import random
from brain_games.games import games_engine


def gcd():
    min_problems_number, max_problems_number = 0, 100
    first_problems_number = random.randint(min_problems_number, max_problems_number)
    second_problems_number = random.randint(min_problems_number, max_problems_number)
    problem = [first_problems_number, second_problems_number]
    if first_problems_number == 0 or second_problems_number == 0:
        first_problems_number = first_problems_number + second_problems_number
        return problem, first_problems_number
    while first_problems_number != second_problems_number:
        if first_problems_number > second_problems_number:
            first_problems_number = first_problems_number - second_problems_number
        else:
            second_problems_number = second_problems_number - first_problems_number
    return problem, first_problems_number


games_question = 'Find the greatest common divisor of given numbers.'


def main():
    games_engine.handler(gcd, games_question)


if __name__ == '__main__':
    main()
