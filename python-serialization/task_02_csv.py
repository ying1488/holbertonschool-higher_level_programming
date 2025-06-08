#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(CSVfile):
    try:
        with open(CSVfile, encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)
            data = list(csv_reader)

        with open("data.json", encoding="utf-8") as f:
            json.dump(data, f)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
