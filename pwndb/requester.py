#!/usr/bin/env python3.8

from pwndb.parser import Parser

import requests
import re


class Requester(object):
    def __init__(self, proxy):
        self.url = "http://pwndb2am4tzkvold.onion/"
        self.session = requests.session()
        self.__set_proxies(proxy)
        self.parser = Parser()

    def __set_proxies(self, proxy):
        self.session.proxies = {
            "http": f"socks5h://{proxy}",
            "https": f"socks5h://{proxy}",
        }

    def request(self, data):

        try:
            resp = self.session.post(self.url, data=data)
        except Exception as e:
            raise e

        return self.parser.response_parse(resp.text)
