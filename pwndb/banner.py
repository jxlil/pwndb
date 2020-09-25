#!/usr/bin/env python3.8

from string import ascii_uppercase, digits
from pwndb import __version__
from pwndb import __name__

import random
import time


class Banner(object):
    def __init__(self):
        print("\n")

    def __get_random_char_line(self, num_chars: int) -> list:

        return random.sample(ascii_uppercase + digits, k=num_chars)

    def __shuffle_line(self, line: str):

        for _ in range(0, random.randint(1, 8)):
            tmp_char_line = self.__get_random_char_line(len(line) + 3)
            print(f"\t{' '.join(tmp_char_line)}", end="\r")
            time.sleep(0.05)

        print(f"\t{' '.join(line)}")

    def print_banner(self, author="jxlil"):

        project = __name__
        for char_name in project.upper():
            line = self.__get_random_char_line(len(project) + 3)
            random_line_index = random.randint(0, len(line) - 1)
            line[random_line_index] = f"\033[1;92m{char_name}\033[0m"
            self.__shuffle_line(line)

        print(
            f"""
        
        version: {__version__}
        author: {author}
        
        """
        )
