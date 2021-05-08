import prompt
import random
from brain_games.scripts import counter_answer
from brain_games.scripts import welcome_speech


def is_number_prime():
    number = random.randint(2, 3572)
    correct_answer = "yes"
    if number != 2 and number % 2 == 0:
        correct_answer = "no"
    else:
        divider = 3
        for step in range(1, number // 2 - 1):
            if number % divider == 0:
                correct_answer = "no"
            else:
                divider += 2
    print('Question:', number)
    user_answer = prompt.string('Your answer: ')
    if str(correct_answer) == user_answer:
        return True
    return str(correct_answer), user_answer


def main():
    name = welcome_speech.welcome_speech()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter_answer.counter(is_number_prime, name)


if __name__ == '__main__':
    main()
