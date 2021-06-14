import random
from brain_games.engine import games_engine
MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB = 0, 100


def random_calc():
    first_problem_numb = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    second_problem_numb = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    numb_sum, numb_diff, numb_multi = '+', '-', '*'
    operation = random.choice([numb_sum, numb_diff, numb_multi])
    problem = ("{} {} {}".format(first_problem_numb,
                                 operation, second_problem_numb))
    if operation == numb_sum:
        correct_answer = first_problem_numb + second_problem_numb
    elif operation == numb_diff:
        correct_answer = first_problem_numb - second_problem_numb
    elif operation == numb_multi:
        correct_answer = first_problem_numb * second_problem_numb
    return problem, correct_answer


games_question = 'What is the result of the expression?'


def main():
    games_engine.handler(random_calc, games_question)


if __name__ == '__main__':
    main()
