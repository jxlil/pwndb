#!/usr/bin/env python3.8

from yaspin import yaspin, Spinner
from requests import Session

from pwndb import parser


class Requester(object):
    def __init__(self, args):
        self.session = Session()
        self.args = args

        self.url = "http://pwndb2am4tzkvold.onion/"
        self.__set_proxy(self.args.tor_proxy)

        self.spinner = Spinner(["[ ]", "[.]", "[:]", "[.]", "[ ]"], 200)

    def __get_data(self, password: str, target: str) -> dict:

        if password:
            return {"submitform": "pw", "password": target}

        else:
            localpart, domain = parser.parse_email(target)

            return {
                "luser": localpart,
                "domain": domain,
                "luseropr": 1,
                "domainopr": 1,
                "submitform": "em",
            }

    def __set_proxy(self, proxy):

        self.session.proxies = {
            "http": f"socks5h://{proxy}",
            "https": f"socks5h://{proxy}",
        }

    def make_request(self) -> list:

        with yaspin(self.spinner, text="Downloading information") as spinner:

            try:
                data = self.__get_data(
                    password=self.args.password, target=self.args.target
                )

                response = self.session.post(self.url, data=data, timeout=15).text
                spinner.ok("[+]")

                return parser.parse_response(response)

            except Exception as e:
                spinner.fail("[-]")
                raise e
