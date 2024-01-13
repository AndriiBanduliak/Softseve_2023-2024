import unittest
from task3 import count_chars


class TestCountChars(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_chars(""), {})

    def test_unique_chars(self):
        self.assertEqual(count_chars("abc"), {'a': 1, 'b': 1, 'c': 1})

    def test_repeating_chars(self):
        self.assertEqual(count_chars("aabbcc"), {'a': 2, 'b': 2, 'c': 2})

    def test_mixed_chars(self):
        self.assertEqual(count_chars("abc123"), {
                         'a': 1, 'b': 1, 'c': 1, '1': 1, '2': 1, '3': 1})

    def test_special_chars(self):

        self.assertEqual(count_chars("a b!c"), {
                         'a': 1, ' ': 1, 'b': 1, '!': 1, 'c': 1})

    def test_numerical_string(self):
        self.assertEqual(count_chars("112233"), {'1': 2, '2': 2, '3': 2})

    def test_case_sensitivity(self):
        self.assertEqual(count_chars("aAbBcC"), {
                         'a': 1, 'A': 1, 'b': 1, 'B': 1, 'c': 1, 'C': 1})


if __name__ == '__main__':
    unittest.main()
