#!/usr/bin/env python3
"""Module that defines functions and classes."""


import csv
import json


def convert_csv_to_json(filename_csv):
    """Convert Csv To Json.

    Args:
        filename_csv (type): Description of filename_csv.
    """
    try:
        with open(filename_csv, "r", encoding="utf-8") as fcsv:
            reader = csv.DictReader(fcsv)
            liste = []
            for row in reader:
                liste.append(row)
            with open("data.json", "w", encoding="utf-8") as fjson:
                json.dump(liste, fjson)
        return True
    except (FileNotFoundError):
        return False
