import random
from brain_games.games import games_engine


def find_progression_elem():
    min_progression_len, max_progression_len = 5, 10
    min_progression_element, max_progression_element = 0, 100
    min_progression_step, max_progression_step = 1, 10
    progression_len = random.randint(min_progression_len, max_progression_len)
    progression_first_number = (random.randint(min_progression_element,
                                               max_progression_element))
    progression_step = (random.randint(min_progression_step,
                                       max_progression_step))
    progression = [progression_first_number]
    progression_current_position = 1
    while progression_current_position < progression_len:
        progression_first_number += progression_step
        progression.append(progression_first_number)
        progression_current_position += 1
    random_dots = random.randint(0, progression_len - 1)
    correct_answer = progression[random_dots]
    progression[random_dots] = '..'
    return progression, correct_answer


games_question = 'What number is missing in the progression?'


def main():
    games_engine.counter(find_progression_elem, games_question)


if __name__ == '__main__':
    main()
