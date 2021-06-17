import random


MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN = 5, 10
MIN_PROGRESSION_ELEMENT, MAX_PROGRESSION_ELEMENT = 0, 100
MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP = 1, 10
GAMES_QUESTION = 'What number is missing in the progression?'


def make_progression(len, first_numb, step):
    progression = [first_numb]
    for _ in range(1, len):
        first_numb += step
        progression.append(first_numb)
    return progression


def stole_numb_from_progression(progression):
    missing_number_index = random.randint(0, len(progression) - 1)
    missing_number = progression[missing_number_index]
    modified_progression = progression
    modified_progression[missing_number_index] = '..'
    return missing_number


def make_problem_with_solution():
    progression_len = random.randint(MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN)
    progression_number = (random.randint(MIN_PROGRESSION_ELEMENT,
                                         MAX_PROGRESSION_ELEMENT))
    progression_step = (random.randint(MIN_PROGRESSION_STEP,
                                       MAX_PROGRESSION_STEP))
    progression = make_progression(progression_len,
                                   progression_number, progression_step)
    missing_number = stole_numb_from_progression(progression)
    problem = ' '.join(map(str, progression))
    return problem, missing_number
