#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from os import path

import sys

BASE_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, BASE_DIR)

try:
    from pwndb import __version__
    from pwndb import main
except ModuleNotFoundError as identifier:
    print("Error:", identifier)
    sys.exit(1)

if __name__ == "__main__":
    parser = ArgumentParser(description="Leaked password finder")
    parser.add_argument(
        "-t",
        "--target",
        metavar=("EMAIL"),
        type=str,
        help="Set target email.",
        required=True,
    )
    parser.add_argument(
        "--password",
        dest="password",
        action="store_true",
        default=False,
        help="Search by password.",
    )
    parser.add_argument(
        "-V",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Display results on screen.",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar=("NAME_FILE"),
        type=str,
        help="Save output in JSON format.",
    )
    parser.add_argument(
        "--tor-proxy", type=str, default="localhost:9050", help="Set Tor proxy."
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s " + __version__
    )

    args = parser.parse_args()
    main.Init(args)
