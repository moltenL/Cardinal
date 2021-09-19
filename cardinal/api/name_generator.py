import json
import random


def read_json():
    with open("teams.json") as file:
        return json.load(file)


def get_name():
    names, weights = zip(*read_json())
    one, two = random.choices(names, weights=weights, k=2)
    return f"{one}{two}"
