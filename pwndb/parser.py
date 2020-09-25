#!/usr/bin/env python3

import sys
import re


class Parser(object):
    def __init__(self):
        self.result = dict()
        self.get_data = lambda s: s.split("=>")[1].strip()

    def response_parse(self, response: str) -> dict:

        text = re.findall(r"\[(.*)", response)
        text = [text[n : n + 4] for n in range(0, len(text), 4)]

        for item in text:
            index = self.get_data(item[0])
            localpart = self.get_data(item[1])
            domain = self.get_data(item[2])
            passwd = self.get_data(item[3])

            self.result[index] = {
                "email": f"{localpart}@{domain}",
                "password": f"{passwd}",
            }

        return self.result

    def email_parse(self, email: str) -> list:

        regex = r"(^[a-zA-Z0-9_.+%-]+@[a-zA-Z0-9%-]+\.[a-zA-Z0-9-.%]+$)"
        if re.match(regex, email):
            return email.split("@")
        else:
            print(f"[x] Invalid target: {email}")
            print("[~] Target email expected: example@domain.com")
            sys.exit(2)
