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
        nested_list = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]

        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = categorizer.flatten(nested_list)

        self.assertEqual(expected, actual)

    def test_filter_duplicates_should_remove_duplicates(self):
        words = ['hello', 'world', 'its', 'me']
        dupes = ['hello', 'world']

        expected = {'its', 'me'}
        actual = reghelpers.filter_duplicates(words, dupes)

        self.assertEqual(expected, actual)

    def test_filter_duplicates_should_ignore_empty_dupes(self):
        words = ['hello', 'world', 'its', 'me']
        dupes = []

        expected = {'hello', 'world', 'its', 'me'}
        actual = reghelpers.filter_duplicates(words, dupes)

        self.assertEqual(expected, actual)


class CategorizeTest(unittest.TestCase):
    # @unittest.skip('requires user input')
    def test_categorize_existing(self):
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
        actual = categorizer.categorize(newKeys, existing)

        for key in expected:
            self.assertEqual(sorted(expected[key]), sorted(actual[key]))


if __name__ == '__main__':
    unittest.main()
