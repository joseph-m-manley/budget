import unittest
from unittest import TestCase as Test
import budget.utilities as util


class TestFilters(Test):
    def test_filter_noise(self):
        words = ['hello xxxx1234', 'foo world', 'its#9999', '    me   ']
        noise = ["foo", "#\\d+", "X+\\d{4}"]

        expected = {'hello', 'world', 'its', 'me'}
        actual = util.filter_noise(words, noise)

        self.assertEqual(expected, actual)

    def test_filter_duplicates_should_remove_duplicates(self):
        words = ['hello', 'world', 'its', 'me']
        dupes = ['hello', 'world']

        expected = {'its', 'me'}
        actual = util.filter_duplicates(words, dupes)

        self.assertEqual(expected, actual)

    def test_filter_duplicates_should_ignore_empty_list(self):
        words = ['hello', 'world', 'its', 'me']
        dupes = []

        expected = {'hello', 'world', 'its', 'me'}
        actual = util.filter_duplicates(words, dupes)

        self.assertEqual(expected, actual)


class TestContainsAny(Test):
    def test_returns_true_if_any_word_matches(self):
        phrase = 'hello world its me'
        words_to_find = ['its', 'a', 'beautiful', 'world']

        self.assertTrue(util.contains_any(phrase, words_to_find))

    def test_returns_true_if_word_contains_any_substring(self):
        phrase = 'zim zam BORKBIRK.important-stuff-obfuscated-hereXXXX9990'
        words_to_find = ['important-stuff']

        self.assertTrue(util.contains_any(phrase, words_to_find))

    def test_should_ignore_empty_set(self):
        phrase = 'hello world'
        words_to_match = []

        self.assertFalse(util.contains_any(phrase, words_to_match))

if __name__ == '__main__':
    unittest.main()
