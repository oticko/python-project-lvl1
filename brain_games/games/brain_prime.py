import random


MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB = 2, 3572
GAMES_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(number):
    if number != 2 and number % 2 == 0 or number < 2:
        return False
    for divider in range(3, number - 1, 2):
        if number % divider == 0:
            return False
    return True


def make_problem_with_solution():
    problem = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    correct_answer = 'no'
    if is_number_prime(problem):
        correct_answer = 'yes'
    return problem, correct_answer
