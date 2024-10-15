import unittest
from unittest.mock import mock_open, patch


def file_parser(file_path, find_string, replace_string=None):
    with open(file_path, 'r') as file:
        content = file.read()

    if replace_string is not None:
        content = content.replace(find_string, replace_string)
        with open(file_path, 'w') as file:
            file.write(content)
        return f'Replaced {content.count(replace_string)} strings'

    return f'Found {content.count(find_string)} strings'


class ParserTest(unittest.TestCase):

    @patch('builtins.open', mock_open(read_data='hello world hello'))
    def test_count_occurrences(self):
        result = file_parser('file.txt', 'hello')
        self.assertEqual(result, 'Found 2 strings')

    @patch('builtins.open', mock_open(read_data='hello world hello'))
    def test_replace_strings(self):
        result = file_parser('file.txt', 'hello', 'hi')
        self.assertEqual(result, 'Replaced 2 strings')
