#!/usr/bin/env python3

import re
import time

from pwndb import banner
from pwndb.requester import Requester
from pwndb.parser import Parser
from pwndb.printer import Printer
from pwndb.saved import Saved


class Init(object):
    def __init__(self, args):
        banner.print_banner()

        print("[~] Starting ...")
        proxy = args.tor_proxy
        data = self._set_data(args.password, args.target)
        req = Requester(proxy)

        print("[~] Waiting for request ...")
        resp = req.request(data)

        if args.verbose:
            print("[~] Print response")
            printer = Printer(resp)
            printer.print_resp()

        print(f"[+] {len(resp)} emails found.")

        print("[~] Create file with data.")
        if args.output:
            saved = Saved(args.output)
        else:
            filename = f"{time.strftime('%d%m%y-%H%M%S')}.json"
            saved = Saved(filename)

        saved.write_file(resp)

    def _set_data(self, password, target) -> dict:

        if password:
            return {"submitform": "pw", "password": target}
        else:
            parser = Parser(target)
            localpart, domain = parser.target_parse()
            return {
                "luser": localpart,
                "domain": domain,
                "luseropr": 1,
                "domainopr": 1,
                "submitform": "em",
            }

