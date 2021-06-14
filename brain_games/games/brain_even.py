import random
MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB = 1, 100
GAMES_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def problems_maker():
    problems_number = random.randint(MIN_PROBLEM_NUMB, MAX_PROBLEM_NUMB)
    correct_answer = is_number_even(problems_number)
    return problems_number, correct_answer


def main():
    GAMES_QUESTION
    problems_maker()


if __name__ == '__main__':
    main()
