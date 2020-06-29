#!/usr/bin/env python3

import sys
import re


class Parser(object):
    def __init__(self, text):
        self.text = text

    def response_parse(self) -> dict:

        text = re.findall(r"\[(.*)", self.text)
        text = [text[n : n + 4] for n in range(0, len(text), 4)]

        get_data = lambda s: s.split("=>")[1].strip()

        resp = dict()
        for item in text:
            index = get_data(item[0])
            localpart = get_data(item[1])
            domain = get_data(item[2])
            passwd = get_data(item[3])

            resp[index] = {"email": f"{localpart}@{domain}", "password": f"{passwd}"}

        return resp

    def target_parse(self) -> list:

        regex = r"(^[a-zA-Z0-9_.+%-]+@[a-zA-Z0-9%-]+\.[a-zA-Z0-9-.%]+$)"
        if re.match(regex, self.text):
            return self.text.split("@")
        else:
            print(f"[x] Invalid target: {self.text}")
            print("[~] Target email expected: example@domain.com")
            sys.exit(2)
