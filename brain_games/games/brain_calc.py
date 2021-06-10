import random
from brain_games.games import games_engine


def random_calc():
    min_problem_numb, max_problem_numb = 0, 100
    first_problem_numb = random.randint(min_problem_numb, max_problem_numb)
    second_problem_numb = random.randint(min_problem_numb, max_problem_numb)
    numb_sum, numb_diff, numb_multi = '+', '-', '*'
    operation = random.choice([numb_sum, numb_diff, numb_multi])
    problem = [first_problem_numb, operation, second_problem_numb]
    correct_answer = first_problem_numb + second_problem_numb
    if operation == numb_diff:
        correct_answer = first_problem_numb - second_problem_numb
    elif operation == numb_multi:
        correct_answer = first_problem_numb * second_problem_numb
    return problem, correct_answer


games_question = 'What is the result of the expression?'


def main():
    games_engine.handler(random_calc, games_question)


if __name__ == '__main__':
    main()
