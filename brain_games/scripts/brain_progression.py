import random
from brain_games.games import all_games
from brain_games.games import games_engine


def find_progression_elem():
    #Длина прогрессии по условиям задачи от 5 до 10 элементов
    len_progression = random.randint(5, 10)
    #Первый элемент прогрессии случайное число от 0 до 100
    first_number = random.randint(0, 100)
    #Шаг прогрессии от 1 до 10
    progressions_step = random.randint(1, 10)
    #Заполняем первый элемент прогрессии
    progression = [first_number]
    #Шагаем по прогресси, начиная с первого элемента
    steps = 1
    while steps < len_progression:
        first_number += progressions_step
        progression.append(first_number)
        steps += 1
    #Определяем случайно место пропущенного элемента последовательности
    random_dots = random.randint(0, len_progression - 1)
    correct_answer = progression[random_dots]
    progression[random_dots] = '..'
    return correct_answer, progression


def main():
    games_question = 'What number is missing in the progression?'
    games_engine.counter(find_progression_elem, games_question)


if __name__ == '__main__':
    main()
