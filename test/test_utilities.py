import unittest
from unittest import TestCase as Test
import budget.utilities as util


class TestFilters(Test):
    def test_filter_noise(self):
        words = ['hello xxxx1234', 'foo world', 'its#9999', '    me   ']
        noise = ["foo", "#\\d+", "X+\\d{4}"]

        expected = ['hello', 'world', 'its', 'me']
        actual = util.filter_noise(words, noise)

        self.assertListEqual(expected, actual)

    def test_filter_noise_always_strips_whitespace(self):
        words = [' 1hello1 ', ' 2world2 ', ' 3its3 ', ' 4me4 ']
        noise = ["\\d+"]

        expected = ['hello', 'world', 'its', 'me']
        actual = util.filter_noise(words, noise)

        self.assertListEqual(expected, actual)

    def test_filter_noise_returns_original_if_noise_is_empty(self):
        words = ['hello xxxx1234', 'foo world', 'its#9999', '    me   ']
        noise = []

        expected = ['hello xxxx1234', 'foo world', 'its#9999', 'me']
        actual = util.filter_noise(words, noise)

        self.assertListEqual(expected, actual)

    def test_remove_known(self):
        words = ['xxxhelloxxx', 'xxxworldxxx', 'its', 'me']
        matches = ['hello', 'world']

        expected = ['its', 'me']
        actual = util.remove_known(words, matches)

        self.assertListEqual(expected, actual)

    def test_remove_known_should_ignore_empty_list(self):
        words = ['hello', 'world', 'its', 'me']
        matches = []

        expected = ['hello', 'world', 'its', 'me']
        actual = util.remove_known(words, matches)

        self.assertListEqual(expected, actual)


class TestContainsAny(Test):
    def test_returns_true_if_any_word_known(self):
        description = 'hello world its me'
        existing_keys = ['its', 'a', 'beautiful', 'world']

        self.assertTrue(util.contains_any(description, existing_keys))

    def test_returns_true_if_word_contains_any_substring(self):
        description = 'zim zam BORKBIRK.important-stuff-obfuscated-hereXXXX9990'
        existing_keys = ['important-stuff']

        self.assertTrue(util.contains_any(description, existing_keys))

    def test_should_ignore_empty_set(self):
        description = 'hello world'
        existing_keys = []

        self.assertFalse(util.contains_any(description, existing_keys))


class TestContainsNone(Test):
    def test_returns_true_if_any_word_known(self):
        description = 'hello world its me'
        existing_keys = ['its', 'a', 'beautiful', 'world']

        self.assertFalse(util.contains_none(description, existing_keys))

    def test_returns_true_if_word_contains_none_substring(self):
        description = 'zim zam BORKBIRK.important-stuff-obfuscated-hereXXXX9990'
        existing_keys = ['important-stuff']

        self.assertFalse(util.contains_none(description, existing_keys))

    def test_should_ignore_empty_set(self):
        description = 'hello world'
        existing_keys = []

        self.assertTrue(util.contains_none(description, existing_keys))


class TestFileHelpers(Test):
    def test_try_get_json_with_bad_path_returns_empty_dict(self):
        noise = util.try_get_json("a path that obviously does not exist", 'arbitrary key')
        self.assertDictEqual(noise, dict())


if __name__ == '__main__':
    unittest.main()
