import re


def pretty_message(data):
    pattern = r'"([^"]+): ([^,]+), (\d{4})"'
    matches = re.findall(pattern, data)
    return matches
