#!/usr/bin/env python3.8

from time import strftime
from json import dump


def write(response: list, filename: str) -> None:

    filename = filename if filename else f"{strftime('%d%m%y-%H%M%S')}.json"
    with open(filename, "w") as f:
        dump(response, f, indent=2)

    print(f"[+] the file '{filename}' was created")
