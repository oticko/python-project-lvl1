import random


MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN = 5, 10
MIN_PROGRESSION_ELEMENT, MAX_PROGRESSION_ELEMENT = 0, 100
MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP = 1, 10
GAMES_QUESTION = 'What number is missing in the progression?'


def make_progression(len, first_numb, step):
    progression = [first_numb]
    for elements in range(1, len):
        first_numb += step
        progression.append(first_numb)
    return progression


def make_progression_with_dots(progression):
    random_dots = random.randint(0, len(progression) - 1)
    missing_number = progression[random_dots]
    progression[random_dots] = '..'
    return progression, missing_number


def make_problem_with_solve():
    progression_len = random.randint(MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN)
    progression_number = (random.randint(MIN_PROGRESSION_ELEMENT,
                                         MAX_PROGRESSION_ELEMENT))
    progression_step = (random.randint(MIN_PROGRESSION_STEP,
                                       MAX_PROGRESSION_STEP))
    progression = make_progression(progression_len,
                                   progression_number, progression_step)
    modify_progression, missing_number = make_progression_with_dots(progression)
    problem = ''
    for elem in modify_progression:
        problem += str(elem) + ' '
    return problem[:len(problem) - 1], missing_number
