def counter(question, name):
    count = 0
    while count < 3:
        result = question()
        if result is True:
            print('Correct!')
            count += 1
        else:
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
    else:
        (print('{} is wrong answer ;(. Correct answer was {}'.
               format(result[1], result[0])))
        print("Let's try again, {}!".format(name))


def main():
    counter()


if __name__ == '__main__':
    main()
