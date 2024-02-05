import unittest
from functions_with_errors import greeting_by_name, get_symbol_position, merge

class TestFuncWithErrors(unittest.TestCase):

    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name("Alice"), "Hello Alice!")
        self.assertEqual(greeting_by_name("Bob"), "Hello Bob!")

    def test_get_symbol_position(self):
        # Test single-letter symbol
        self.assertEqual(get_symbol_position("Hello, world!", ","), 6)
        self.assertEqual(get_symbol_position("Python is fun", "i"), 8)
        self.assertEqual(get_symbol_position("No symbol here", "?"), "Not found")

        # Test multi-letter symbol
        self.assertEqual(get_symbol_position("Hello, world!", "ello"), "Error! Symbol can be string with only one letter")

    def test_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected_result = {'a': 1, 'b': 3, 'c': 4}

        self.assertEqual(merge(dict1, dict2), expected_result)

if __name__ == '__main__':
    unittest.main()
