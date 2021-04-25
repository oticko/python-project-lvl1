#!/usr/bin/env python
from brain_games import cli


def greet(welcome):
    print(welcome)


def main():
    greet('Welcome to the Brain Games!')
    cli.welcome_greet()


if __name__ == '__main__':
    main()