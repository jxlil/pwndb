#!/usr/bin/env python3.8

from string import ascii_uppercase, digits
from pwndb import __version__
from pwndb import __author__
from pwndb import __name__

from random import randint, sample
from time import sleep


def _get_random_char_line(num_chars: int) -> list:
    return sample(ascii_uppercase + digits, k=num_chars)


def _shuffle_line(line: list) -> None:

    for _ in range(randint(1, 8)):
        aux_line = _get_random_char_line(len(line) + 3)
        print(f"\t{' '.join(aux_line)}", end="\r")
        sleep(0.05)

    print(f"\t{' '.join(line)}")


def display() -> None:

    print("\n")

    project_name = __name__
    for char_name in project_name.upper():

        line = _get_random_char_line(len(project_name) + 3)
        random_index = randint(0, len(line) - 1)

        line[random_index] = f"\033[1;92m{char_name}\033[0m"
        _shuffle_line(line)

    print(f"\n\n\tversion: {__version__}\n\tauthor: {__author__}\n\n")
