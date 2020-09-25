#!/usr/bin/env python3.8


from pwndb.requester import Requester
from pwndb.printer import Printer
from pwndb.parser import Parser
from pwndb.saved import Saved
from pwndb import banner

import time
import re


class Init(object):
    def __init__(self, args):
        banner.print_banner()

        print("[~] Starting ...")
        data = self.__set_data(args.password, args.target)

        print("[~] Waiting for request ...")
        requester = Requester(args.tor_proxy)
        resp = requester.request(data)

        if args.verbose:
            print("[~] Print response")
            printer = Printer()
            printer.print_response(resp)

        print(f"[+] {len(resp)} emails found.")

        print("[~] Create file with data.")
        saved = Saved(args.output)
        saved.write_file(resp)

    def __set_data(self, password, target) -> dict:

        if password:
            return {"submitform": "pw", "password": target}
        else:
            parser = Parser()
            localpart, domain = parser.email_parse(target)
            return {
                "luser": localpart,
                "domain": domain,
                "luseropr": 1,
                "domainopr": 1,
                "submitform": "em",
            }
