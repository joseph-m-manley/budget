import json
import unittest

from budget.Input import Input
from unittest import TestCase as Test


class TestInput(Test):
    def test_ask_for_category(self):
        expected = 'hello'
        print(expected)
        actual = Input().ask_for_category('expected: \'hello\'')

        self.assertEqual(expected, actual)


    def test_ask_for_key_for_descriptions_longer_than_15_char(self):
        expected = 'string'
        print(expected)
        actual = Input().ask_for_key('what you need to type is \'string\'')

        self.assertEqual(expected, actual)

    def test_does_not_ask_for_key_for_descriptions_shorter_than_15_char(self):
        expected = 'short'
        actual = Input().ask_for_key('short')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
