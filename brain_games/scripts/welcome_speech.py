import prompt


def welcome_speech():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def main():
    welcome_speech()


if __name__ == '__mane__':
    main()
