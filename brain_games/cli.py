import prompt


def welcome_greet():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


def main():
    welcome_greet()


if __name__ == '__main__':
    main()
