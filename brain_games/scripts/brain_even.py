from brain_games.engine import games_engine
from brain_games.games import brain_even


def main():
    games_engine.handler(brain_even.make_problem_with_solve,
                         brain_even.GAMES_QUESTION)


if __name__ == '__main__':
    main()