import prompt
import random
from brain_games.scripts import counter_answer
from brain_games.scripts import welcome_speech


def gcd():
    first_rand_numb = random.randint(0, 100)
    sec_rand_numb = random.randint(0, 100)
    print('Question:', first_rand_numb, sec_rand_numb)
    user_answer = prompt.string('Your answer: ')
    if first_rand_numb == 0 or sec_rand_numb == 0:
        first_rand_numb = first_rand_numb + sec_rand_numb
    else:
        while first_rand_numb != sec_rand_numb:
            if first_rand_numb > sec_rand_numb:
                first_rand_numb = first_rand_numb - sec_rand_numb
            else:
                sec_rand_numb = sec_rand_numb - first_rand_numb
    if str(first_rand_numb) == user_answer:
        return True
    return str(first_rand_numb), user_answer


def main():
    name = welcome_speech.welcome_speech()
    print('Find the greatest common divisor of given numbers.')
    counter_answer.counter(gcd, name)


if __name__ == '__main__':
    main()
