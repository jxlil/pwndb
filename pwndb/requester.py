#!/usr/bin/env python3.8

from yaspin import yaspin, Spinner
from pwndb.parser import Parser
import requests
import sys


class Requester(object):
    def __init__(self, proxy):
        self.url = "http://pwndb2am4tzkvold.onion/"
        self.session = requests.session()
        self.__set_proxies(proxy)
        self.parser = Parser()
        self.spinner = Spinner(["[ ]", "[.]", "[:]", "[.]", "[ ]"], 200)

    def __set_proxies(self, proxy):
        self.session.proxies = {
            "http": f"socks5h://{proxy}",
            "https": f"socks5h://{proxy}",
        }

    def request(self, data):

        with yaspin(self.spinner, text="Downloading information") as spinner:
            try:
                resp = self.session.post(self.url, data=data, timeout=15)
                spinner.ok("[+]")

            except Exception as identifier:
                spinner.fail("[-]")
                print("Error:", identifier)
                sys.exit(3)

        return self.parser.response_parse(resp.text)
