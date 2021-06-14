import random
from brain_games.games import games_engine
MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN = 5, 10
MIN_PROGRESSION_ELEMENT, MAX_PROGRESSION_ELEMENT = 0, 100
MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP = 1, 10


def find_progression_elem():
    progression_len = random.randint(MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN)
    progression_number = (random.randint(MIN_PROGRESSION_ELEMENT,
                                         MAX_PROGRESSION_ELEMENT))
    progression_step = (random.randint(MIN_PROGRESSION_STEP,
                                       MAX_PROGRESSION_STEP))
    progression = [progression_number]
    for progression_current_position in range(1, progression_len):
        progression_number += progression_step
        progression.append(progression_number)
    random_dots = random.randint(0, progression_len - 1)
    correct_answer = progression[random_dots]
    progression[random_dots] = '..'
    problem = ''
    for elem in progression:
        problem += str(elem) + ' '
    return problem[:len(problem) - 1], correct_answer


games_question = 'What number is missing in the progression?'


def main():
    games_engine.handler(find_progression_elem, games_question)


if __name__ == '__main__':
    main()
