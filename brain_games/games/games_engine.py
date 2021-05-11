import prompt


#Приветствие игрока, запрос его имени и вывод правил игры. Функция возвращает имя игрока.
def welcome_speech(games_question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(games_question)
    return name


def counter(game, games_question):
    name = welcome_speech(games_question)
    #Количество верных ответов в перед началом игры.
    current_round = 0
    #Необходимое количество верных ответов для удачного завершения игры
    number_of_rounds = 3
    while current_round < number_of_rounds:
        #Получаем результаты игры
        game_results = game()
        #Распаковываем результаты игры
        correct_answer = game_results[0]
        game_question = game_results[1]
        #Приводим правильный ответ к одному типу с ответом игрока
        correct_answer = str(correct_answer)
        print('Question: ', *game_question)
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            (print('{!r} is wrong answer ;(. Correct answer was {!r}'.
                   format(user_answer, correct_answer)))
            print("Let's try again, {}!".format(name))
            break
        print('Correct!')
        current_round += 1
    if current_round == number_of_rounds:
        print('Congratulations, {}!'.format(name))


def main():
    counter()


if __name__ == '__main__':
    main()
