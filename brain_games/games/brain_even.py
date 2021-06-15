import random


MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB = 1, 100
GAMES_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    return True if number % 2 == 0 else False


def make_problem_with_solve():
    problem = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    correct_answer = 'no'
    if is_number_even(problem):
        correct_answer = 'yes'
    return problem, correct_answer
