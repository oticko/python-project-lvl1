import prompt
import random
from brain_games.scripts import counter_answer
from brain_games.scripts import welcome_speech


def is_number_even(number):
    if int(number) % 2 == 0:
        return 'yes'
    return 'no'


def asking_question():
    random_number = random.randint(1, 100)
    print('Question: {}'.format(random_number))
    answer = prompt.string('Your answer: ')
    if answer == is_number_even(random_number):
        return True
    return is_number_even(random_number), answer


def main():
    name = welcome_speech.welcome_speech()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter_answer.counter(asking_question, name)


if __name__ == '__main__':
    main()
