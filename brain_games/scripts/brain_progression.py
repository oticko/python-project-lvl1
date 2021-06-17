from brain_games.engine import games_engine
from brain_games.games import brain_progression


def main():
    games_engine.play_game(brain_progression.make_problem_with_solution,
                           brain_progression.GAMES_QUESTION)


if __name__ == '__main__':
    main()
