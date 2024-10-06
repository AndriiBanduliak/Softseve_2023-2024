

import json


def find(file, key):
    unique_values = set()  # To store unique values of the key

    def search_for_key(data):
        if isinstance(data, dict):
            for k, v in data.items():
                if k == key:
                    if isinstance(v, list):
                        unique_values.update(v)
                    else:
                        unique_values.add(v)
                elif isinstance(v, (dict, list)):
                    search_for_key(v)
        elif isinstance(data, list):
            for item in data:
                search_for_key(item)

    try:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            search_for_key(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file is not found or invalid JSON

    return list(unique_values)
