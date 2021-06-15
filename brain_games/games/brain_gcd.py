import random


MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB = 0, 100
GAMES_QUESTION = 'Find the greatest common divisor of given numbers.'


def gcd_finder(first_number, second_number):
    if first_number == 0 or second_number == 0:
        first_number = first_number + second_number
        return first_number
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return first_number


def make_problem_with_solve():
    first_problem_numb = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    second_problem_numb = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    problem = ("{} {}". format(first_problem_numb, second_problem_numb))
    correct_answer = gcd_finder(first_problem_numb, second_problem_numb)
    return problem, correct_answer
