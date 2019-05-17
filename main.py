#!/usr/bin/python

import model.firefox as fox_db
import controller.firefox as fox


def to_list(data):
    """
    given a sqlite cursor, return the list of data

    parameters
    ----------
    data: sqlite.cursor
        a sqlite.cursor of data from sql db

    returns
    -------
    list
        a list of given data iterated from the cursor
    """

    formatted_data = []
    for row in data:
        formatted_data.append(list(str(x) for x in row))
    return formatted_data


def extract_data(firefox=True, chrome=True):
    """
    extract data from local sqlite file

    parameters
    ----------
    firefox: boolean
        if true, extract data from firefox
    chrome: boolean
        if true, extract data from chrome

    returns
    -------
    list
        contains data for firefox
    list
        contains data for chrome

    """
    if chrome is True:
        # TODO implement codes to extract data from chrome
        chrome_data = []
    if firefox is True:
        fox_path = fox.get_path()
        fox_data = fox_db.load_data(fox_path[0])
        fox_data = to_list(fox_data)

    return fox_data, chrome_data


if __name__ == "__main__":
    fox_data, chrome_data = extract_data()
    print(len(fox_data))
