#!/usr/bin/env python3.8

from re import findall, match


def _split_email(email: list) -> list:

    values = list()
    for item in email:
        values.append(item.split("=>")[1].strip())

    return values


def parse_response(response: str) -> list:

    results = list()

    raw_emails = findall(r"\[(.*)", response)
    raw_emails = [raw_emails[n : n + 4] for n in range(0, len(raw_emails), 4)]

    for raw_email in raw_emails:
        # raw_email: ['id] => 74303', 'luser] => donate', 'domain] => btc.thx', 'password] => 1J1iZ2KRAyPyhXm6xxAyWyVV3FPqAqLHkG']
        _id, localpart, domain, passwd = _split_email(raw_email)

        email = f"{localpart}@{domain}"
        if email == "donate@btc.thx":
            continue

        results.append(
            {
                "id": _id,
                "email": email,
                "password": passwd,
            }
        )

    return results


def parse_email(email: str) -> list:

    regex = r"(^[a-zA-Z0-9_.+%-]+@[a-zA-Z0-9%-]+\.[a-zA-Z0-9-.%]+$)"
    if match(regex, email):
        return email.split("@")

    else:
        raise Exception(f"Invalid email: {email}")
