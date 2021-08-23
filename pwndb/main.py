#!/usr/bin/env python3.8

from texttable import Texttable

from pwndb.requester import Requester
from pwndb import banner
from pwndb import files


class Init(object):
    def __init__(self, args):

        banner.display()

        self.requester = Requester(args)
        response = self.requester.make_request()

        if args.verbose:
            print(self.__generate_table(response).draw())

        print(f"[+] {len(response)} emails found")
        files.write(response=response, filename=args.output)

    def __generate_table(self, response: list) -> Texttable:

        # create table with two columns
        table = Texttable()
        table.set_cols_dtype(["t", "t"])
        table.header(["Email", "Password"])

        for item in response:
            table.add_row((item["email"], item["password"]))

        return table
