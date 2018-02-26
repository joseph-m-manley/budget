import json
import unittest

from budget.Input import Input
from unittest import TestCase as Test


class TestInputAskForKeyword(Test):
    def test_asks_for_key_for_descriptions_longer_than_15_char(self):
        expected = 'STRING'
        actual = Input().ask_for_key('what you need to type is \'%s\'' % expected)

        self.assertEqual(expected, actual)

    def test_does_not_ask_for_key_for_descriptions_shorter_than_15_char(self):
        expected = 'SHORT'
        actual = Input().ask_for_key(expected)

        self.assertEqual(expected, actual)

    def test_defaults_to_description_when_no_input_is_given(self):
        expected = 'JUST PRESS ENTER'
        actual = Input().ask_for_key(expected)

        self.assertEqual(expected, actual)


class TestInputAskForCategory(Test):
    def test_ask_for_category(self):
        expected = 'HELLO'
        actual = Input().ask_for_category(expected)

        self.assertEqual(expected, actual)


class TestCaseSensitivity(Test):
    def test_ask_for_category_returns_upper_case(self):
        expected = "UPPERCASE"
        actual = Input().ask_for_category(expected)

        self.assertEqual(expected, actual)
           
    def test_ask_for_key_returns_upper_case(self):
        expected = "UPPERCASE CATEGORY"
        actual = Input().ask_for_key(expected)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
