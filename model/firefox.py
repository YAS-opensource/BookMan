#!/usr/bin/python

import sqlite3
import os
import sys


def load_data(path):
    """
    handles db operations for firefox database 

    parameters
    ----------
    path: String
        local path of the sqlite database file

    returns
    -------
    sqlite.cursor
        a cursor to iterate the data extracted from db : url, title, id, parent_id
    """

    FNAME = path

    DB = sqlite3.connect(FNAME)

    try:
        cursor = DB.cursor()
        cursor.execute(
            """
    SELECT DISTINCT
        moz_places.url AS url,
        moz_bookmarks.title AS title,
        moz_bookmarks.id AS id,
        moz_bookmarks.parent AS parent

    FROM
        moz_bookmarks
        JOIN moz_places
        ON moz_places.id = moz_bookmarks.fk
    """
        )
        return cursor
    except sqlite3.OperationalError as e:
        if "locked" in str(e):
            print("Please shut down Firefox/Chrome before running this application")
        else:
            print(e)
        exit()
