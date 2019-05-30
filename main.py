#!/usr/bin/python

import model.firefox as fox_db
import controller.firefox as fox
import os
import random


class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'


loaded = False
bookMan_logo = '''
██████░░  ████████░░ ████████░░ ██░░██░░
██░░ ██░░ ██░░  ██░░ ██░░  ██░░ ██░██░░
███████░░ ██░░  ██░░ ██░░  ██░░ ████░░
██░░ ██░░ ██░░  ██░░ ██░░  ██░░ ██░██░░
██████░░  ████████░░ ████████░░ ██░░██░░

    ██░░  ██░░ ████████░░ ███░░ ██░░
    ███░░███░░ ██░░  ██░░ ███░░ ██░░
    ████████░░ ████████░░ ██░██░██░░
    ██░░  ██░░ ██░░  ██░░ ██░░ ███░░
    ██░░  ██░░ ██░░  ██░░ ██░░ ███░░'''

options = '''
{1} Search by name
{2} Search by URL
{3} Show Firefox Bookmarks
{4} Show Google Chrome Bookmarks
{5} Quit
'''


def print_logo():
    print(color.RED + bookMan_logo)


def clearScr():
    os.system('clear')


def yesOrNo():
    return (raw_input("Continue Y / N: ") in yes)


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


def run():
    print_logo()
    if not loaded:
        fox_data, chrome_data = extract_data()
    print(color.OKBLUE + options)
    choice = input()
    if choice == "5":
        exit()
    elif choice == "1":
        pass
        # TODO implement searching by bookmark name
    elif choice == "2":
        pass
        # TODO implement searching by bookmark url
    elif choice == "3":
        pass
        # TODO implement utility to browse bookmarks from Firefox
    elif choice == "4":
        pass
        # TODO implement utility to browse bookmarks from Chrome
    clearScr()
    run()


if __name__ == "__main__":
    run()
