import prompt
import random
from brain_games.scripts import counter_answer
from brain_games.scripts import welcome_speech


def find_progression_elem():
    len_progression = random.randint(5, 10)
    first_number = random.randint(0, 100)
    progressions_step = random.randint(1, 10)
    progression = [first_number]
    for elem in range(1, len_progression):
        first_number += progressions_step
        progression.append(first_number)
    random_dots = random.randint(0, len_progression - 1)
    correct_answer = progression[random_dots]
    progression[random_dots] = '..'
    print('Question:', *progression)
    user_answer = prompt.string('Your answer: ')
    if str(correct_answer) == user_answer:
        return True
    return str(correct_answer), user_answer


def main():
    name = welcome_speech.welcome_speech()
    print('What number is missing in the progression?')
    counter_answer.counter(find_progression_elem, name)


if __name__ == '__main__':
    main()
