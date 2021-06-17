from brain_games.engine import games_engine
from brain_games.games import brain_prime


def main():
    games_engine.play_game(brain_prime.make_problem_with_solution,
                           brain_prime.GAMES_QUESTION)


if __name__ == '__main__':
    main()
