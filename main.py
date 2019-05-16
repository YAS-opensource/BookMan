#!/usr/bin/python

import model.db_handler as db
import controller.get_firefox_db as fox_path

if __name__ == "__main__":
    fox_path = fox_path.get_path()
    data = db.load_data(fox_path)
