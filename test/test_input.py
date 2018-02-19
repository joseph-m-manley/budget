import unittest
import json
from unittest import TestCase as Test
from budget.Classes import Data, Input


@unittest.skip('Requires user input')
class TestInput(Test):
    def test_ask_for_category(self):
        expected = 'hello'
        print(expected)
        actual = Input().ask_for_category()

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
