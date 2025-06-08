#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(CSVfile):
    try:
        with open(CSVfile, encoding="utf-8") as f:
            data = list(csv.DictReader(f))

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
