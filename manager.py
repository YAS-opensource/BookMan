#!/usr/bin/python

import sqlite3
import os
import sys


def load_data_from_DB():

    # REPLACE THIS WITH YOUR USERNAME
    FOX_NAME = "58um2fba.dev-edition-default"

    FNAME = os.path.join(os.getcwd(), "places.sqlite")

    DB = sqlite3.connect(FNAME)
    try:

        cursor = DB.cursor()
        cursor.execute(
            """
    SELECT DISTINCT
        moz_places.url AS url,
        moz_bookmarks.title AS title,
        moz_bookmarks.parent AS parent

    FROM
        moz_bookmarks
        JOIN moz_places
        ON moz_places.id = moz_bookmarks.fk
    """
        )
    except sqlite3.OperationalError as e:
        print(e)
        exit()


if __name__ == "__main__":
    load_data_from_DB()
