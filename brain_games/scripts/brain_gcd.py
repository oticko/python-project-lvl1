from brain_games.engine import games_engine
from brain_games.games import brain_gcd


def main():
    games_engine.handler(brain_gcd.make_problem_with_solve,
                         brain_gcd.GAMES_QUESTION)


if __name__ == '__main__':
    main()
