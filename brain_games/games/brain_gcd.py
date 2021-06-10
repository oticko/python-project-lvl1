import random
from brain_games.games import games_engine


def gcd():
    min_problem_numb, max_problem_numb = 0, 100
    first_problem_numb = random.randint(min_problem_numb, max_problem_numb)
    second_problem_numb = random.randint(min_problem_numb, max_problem_numb)
    problem = [first_problem_numb, second_problem_numb]
    if first_problem_numb == 0 or second_problem_numb == 0:
        first_problem_numb = first_problem_numb + second_problem_numb
        return problem, first_problem_numb
    while first_problem_numb != second_problem_numb:
        if first_problem_numb > second_problem_numb:
            first_problem_numb = first_problem_numb - second_problem_numb
        else:
            second_problem_numb = second_problem_numb - first_problem_numb
    return problem, first_problem_numb


games_question = 'Find the greatest common divisor of given numbers.'


def main():
    games_engine.handler(gcd, games_question)


if __name__ == '__main__':
    main()
