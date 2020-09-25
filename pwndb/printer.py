#!/usr/bin/env python3

import texttable as tt


class Printer(object):
    def __init__(self):

        # create texttable
        self.texttable = tt.Texttable()
        self.texttable.set_cols_dtype(["t", "t"])
        self.texttable.header(["Email", "Password"])

    def print_response(self, response: dict):

        for _, item in response.items():
            self.texttable.add_row((item["email"], item["password"]))

        print(self.texttable.draw())
