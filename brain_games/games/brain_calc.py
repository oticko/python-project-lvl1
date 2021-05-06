import prompt
import random
from brain_games.scripts import counter_answer
from brain_games.scripts import welcome_speech


def random_calc():
    first_random_numb = random.randint(0, 100)
    second_random_numb = random.randint(0, 100)
    numb_sum = first_random_numb + second_random_numb
    numb_diff = first_random_numb - second_random_numb
    numb_multi = first_random_numb * second_random_numb
    answer = random.choice([numb_sum, numb_diff, numb_multi])
    if answer == numb_sum:
        operation = '+'
    elif answer == numb_diff:
        operation = '-'
    else:
        operation = '*'
    print('Question:', first_random_numb, operation, second_random_numb)
    user_answer = prompt.string('Your answer: ')
    if str(answer) == user_answer:
        return True
    return str(answer), user_answer


def main():
    name = welcome_speech.welcome_speech()
    print('What is the result of the expression?')
    counter_answer.counter(random_calc, name)


if __name__ == '__main__':
    main()
