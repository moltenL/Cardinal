import json
import random


def read_json():
    with open("cardinal/api/teams.json") as file:
        return json.load(file)


def get_name():
    names, _weights = zip(*read_json())
    one, two = random.sample(names, 2)
    return f"{one}{two}"
