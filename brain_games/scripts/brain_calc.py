from brain_games.engine import games_engine
from brain_games.games import brain_calc


def main():
    games_engine.play_game(brain_calc.make_problem_with_solution,
                         brain_calc.GAMES_QUESTION)


if __name__ == '__main__':
    main()
