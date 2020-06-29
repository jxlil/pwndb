#!/usr/bin/env python3

import texttable as tt


class Printer(object):
    def __init__(self, resp: dict):
        self.resp = resp

    def print_resp(self):
        tab = tt.Texttable()
        tab.set_cols_dtype(["t", "t"])
        tab.header(["Email", "Password"])

        for _, item in self.resp.items():
            tab.add_row((item["email"], item["password"]))

        print(tab.draw())

