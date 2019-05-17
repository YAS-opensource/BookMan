#!/usr/bin/python

import model.firefox as fox_db
import controller.firefox as fox


def to_list(data):
    formatted_data = []
    for row in data:
        formatted_data.append(list(str(x) for x in row))
    return formatted_data


def extract_data(firefox=True, chrome=False):
    if chrome is True:
        # TODO implement codes for chrome
        pass
    if firefox is True:
        fox_path = fox.get_path()
        fox_data = fox_db.load_data(fox_path[0])
        fox_data = to_list(fox_data)
        return fox_data


if __name__ == "__main__":
    data = extract_data()
    print(len(data))
