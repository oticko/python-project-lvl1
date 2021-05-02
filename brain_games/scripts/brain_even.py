import prompt, random


def is_number_even(number):
    if int(number) % 2 == 0:
        return 'yes'
    return 'no'


def asking_question():
    counter = 0
    while counter < 3:
        random_number = random.randint(1, 100)
        print('Question: {}'.format(random_number))
        answer = prompt.string('Your answer: ')
        if answer == is_number_even(random_number):
            print('Correct!')
            counter +=1
            print(counter)
        else:
            print('{} is wrong answer ;(. Correct answer was {}'.format(answer, is_number_even(random_number)))
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if asking_question() is True:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()