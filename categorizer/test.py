import categorizer
import reghelpers
import unittest


class HelpersTest(unittest.TestCase):
    def test_filter_noise(self):
        words = ['hello xxxx1234', 'foo world', 'its#9999', '    me   ']
        noise = ["foo", "#\\d+", "X+\\d{4}"]

        expected = {'hello', 'world', 'its', 'me'}
        actual = categorizer.filter_noise(words, noise)

        self.assertEqual(expected, actual)

    def test_flatten(self):
        nested_list = [[1, 2], [3, 4, 5], [6], [], [7, 8, 9]]

        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = categorizer.flatten(nested_list)

        self.assertEqual(expected, actual)

    def test_filter_duplicates_should_remove_duplicates(self):
        words = ['hello', 'world', 'its', 'me']
        dupes = ['hello', 'world']

        expected = {'its', 'me'}
        actual = reghelpers.filter_duplicates(words, dupes)

        self.assertEqual(expected, actual)

    def test_filter_duplicates_should_ignore_empty_list(self):
        words = ['hello', 'world', 'its', 'me']
        dupes = []

        expected = {'hello', 'world', 'its', 'me'}
        actual = reghelpers.filter_duplicates(words, dupes)

        self.assertEqual(expected, actual)

    def test_contains_any(self):
        word = 'hello world its me'
        possible_duplicates = ['its', 'a', 'beautiful', 'world']

        self.assertTrue(reghelpers.contains_any(word, possible_duplicates))

    def test_contains_any_should_ignore_empty_set(self):
        phrase = 'hello world'
        words_to_match = []

        self.assertFalse(reghelpers.contains_any(phrase, words_to_match))


class AssignKeyTest(unittest.TestCase):
    # @unittest.skip('requires user input')
    def test_assign_keys_to_existing_keymap(self):
        newKeys = {
            'hello', 'honey', 'honey',
            'its', 'me',
            'your', 'your', 'husband',
            'ralph', 'ralph'
            }

        existing = {
            '1': ['hello'],
            '2': ['its'],
            '3': ['husband']
            }

        expected = {
            '1': ['hello', 'honey'],
            '2': ['its', 'me'],
            '3': ['your', 'husband'],
            '4': ['ralph']
            }

        print("honey: 1,  me: 2,  your: 3,  ralph: 4")
        actual = categorizer.assign_keys(newKeys, existing)

        for key in expected:
            self.assertEqual(sorted(expected[key]), sorted(actual[key]))


if __name__ == '__main__':
    unittest.main()
