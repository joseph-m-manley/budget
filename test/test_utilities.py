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

    def test_filter_noise_always_strips_whitespace(self):
        words = [' 1hello1 ', ' 2world2 ', ' 3its3 ', ' 4me4 ']
        noise = ["\\d+"]

        expected = {'hello', 'world', 'its', 'me'}
        actual = util.filter_noise(words, noise)

        self.assertEqual(expected, actual)

    def test_filter_noise_returns_original_if_noise_is_empty(self):
        words = ['hello xxxx1234', 'foo world', 'its#9999', '    me   ']
        noise = []

        expected = {'hello xxxx1234', 'foo world', 'its#9999', 'me'}
        actual = util.filter_noise(words, noise)

        self.assertEqual(expected, actual)

    def test_remove_matches(self):
        words = ['xxxhelloxxx', 'xxxworldxxx', 'its', 'me']
        matches = ['hello', 'world']

        expected = {'its', 'me'}
        actual = util.remove_matches(words, matches)

        self.assertEqual(expected, actual)

    def test_remove_matches_should_ignore_empty_list(self):
        words = ['hello', 'world', 'its', 'me']
        dupes = []

        expected = {'hello', 'world', 'its', 'me'}
        actual = util.remove_matches(words, dupes)

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


class TestContainsNone(Test):
    def test_returns_true_if_any_word_matches(self):
        phrase = 'hello world its me'
        words_to_find = ['its', 'a', 'beautiful', 'world']

        self.assertFalse(util.contains_none(phrase, words_to_find))

    def test_returns_true_if_word_contains_none_substring(self):
        phrase = 'zim zam BORKBIRK.important-stuff-obfuscated-hereXXXX9990'
        words_to_find = ['important-stuff']

        self.assertFalse(util.contains_none(phrase, words_to_find))

    def test_should_ignore_empty_set(self):
        phrase = 'hello world'
        words_to_match = []

        self.assertTrue(util.contains_none(phrase, words_to_match))


class TestFileHelpers(Test):
    def test_try_get_json_with_bad_path_returns_empty_dict(self):
        noise = util.try_get_json("a path that obviously does not exist", 'arbitrary key')
        self.assertDictEqual(noise, dict())


if __name__ == '__main__':
    unittest.main()
