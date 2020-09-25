#!/usr/bin/env python3.8

import json


class Saved(object):
    def __init__(self, path):
        self.path = path

    def write_file(self, text):

        output = [item for _, item in text.items()]
        output = json.dumps(output, indent=2)

        with open(self.path, "w") as f:
            f.write(output)

        print(f"[+] The file {self.path} was created.")
