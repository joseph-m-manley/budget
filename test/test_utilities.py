import budget.utilities as util
import unittest


class HelpersTest(unittest.TestCase):
    def test_invert_dict(self):
        dict_to_invert = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9]}
        expected = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3}

        actual = util.invert_dict(dict_to_invert)

        self.assertEqual(list(expected.keys()), list(actual.keys()))
        for key in expected:
            self.assertEqual(expected[key], actual[key])

    def test_filter_noise(self):
        words = ['hello xxxx1234', 'foo world', 'its#9999', '    me   ']
        noise = ["foo", "#\\d+", "X+\\d{4}"]

        expected = {'hello', 'world', 'its', 'me'}
        actual = util.filter_noise(words, noise)

        self.assertEqual(expected, actual)

    def test_flatten(self):
        nested_list = [[1, 2], [3, 4, 5], [6], [], [7, 8, 9]]

        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = util.flatten(nested_list)

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

    def test_contains_any(self):
        word = 'hello world its me'
        possible_duplicates = ['its', 'a', 'beautiful', 'world']

        self.assertTrue(util.contains_any(word, possible_duplicates))

    def test_contains_any_should_ignore_empty_set(self):
        phrase = 'hello world'
        words_to_match = []

        self.assertFalse(util.contains_any(phrase, words_to_match))

if __name__ == '__main__':
    unittest.main()
