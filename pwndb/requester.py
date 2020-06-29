#!/usr/bin/env python3

import requests
import re

from pwndb.parser import Parser


class Requester(object):
    def __init__(self, proxy):
        self.url = "http://pwndb2am4tzkvold.onion/"
        self.session = requests.session()
        self._set_proxies(proxy)

    def _set_proxies(self, proxy):
        self.session.proxies = {
            "http": f"socks5h://{proxy}",
            "https": f"socks5h://{proxy}",
        }

    def request(self, data):

        try:
            resp = self.session.post(self.url, data=data)
            parser = Parser(resp.text)
            return parser.response_parse()

        except Exception as e:
            raise e

