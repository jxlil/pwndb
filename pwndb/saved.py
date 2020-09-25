#!/usr/bin/env python3.8

import json
import time


class Saved(object):
    def __init__(self, filename: str):
        self.filename = (
            filename if filename else f"{time.strftime('%d%m%y-%H%M%S')}.json"
        )

    def write_file(self, response: dict):

        output = [item for _, item in response.items()]
        output = json.dumps(output, indent=2)

        with open(self.filename, "w") as f:
            f.write(output)

        print(f"[+] The file '{self.filename}' was created")
