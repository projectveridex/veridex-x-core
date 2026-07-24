"""
==========================================
VERIDEX X
DATABASE
==========================================
"""

import json
import os

DATABASE_FILE = "veridex_database.json"


def load_database():

    if not os.path.exists(DATABASE_FILE):

        return []

    with open(DATABASE_FILE, "r", encoding="utf-8") as file:

        return json.load(file)


def save_database(data):

    with open(DATABASE_FILE, "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4)


def add_record(record):

    database = load_database()

    database.append(record)

    save_database(database)
