import random


MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB = 0, 100
GAMES_QUESTION = 'What is the result of the expression?'


def calc(first_numb, operation, second_numb):
    if operation == '+':
        result = first_numb + second_numb
    elif operation == '-':
        result = first_numb - second_numb
    elif operation == '*':
        result = first_numb * second_numb
    else:
        return 'Error'
    return result


def make_problem_with_solution():
    first_problem_numb = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    second_problem_numb = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    operation = random.choice(['+', '-', '*'])
    problem = ("{} {} {}".format(first_problem_numb,
                                 operation, second_problem_numb))
    correct_answer = calc(first_problem_numb, operation, second_problem_numb)
    return problem, correct_answer
