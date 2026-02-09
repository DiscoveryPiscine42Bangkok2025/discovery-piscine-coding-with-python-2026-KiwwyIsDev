#!/usr/bin/env python3


def array_of_names(names: dict):
    return [f"{k} {v}".title() for k, v in names.items()]


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))