import categorizer
import unittest


class Test(unittest.TestCase):
    def test_filter_noise(self):
        words = ['hello xxxx1234', 'foo world', 'its#9999', '    me   ']
        noise = ["foo", "#\\d+", "X+\\d{4}"]

        expected = {'hello', 'world', 'its', 'me'}
        actual = categorizer.filter_noise(words, noise)

        self.assertEqual(expected, actual)

    def test_filter_duplicates(self):
        words = ['hello', 'world', 'its', 'me']
        dupes = ['hello', 'world']

        expected = {'its', 'me'}
        actual = categorizer.filter_duplicates(words, dupes)

        self.assertEqual(expected, actual)

    @unittest.skip('requires user input')
    def test_categorize_new(self):
        newKeys = {'hello', 'world', 'its', 'me'}
        expected = {
            '1': ['hello', 'world'],
            '2': ['its'],
            '3': ['me']
            }

        print('test new')
        print(expected)
        actual = categorizer.categorize(newKeys)

        self.assertEqual(expected, actual)

    @unittest.skip('requires user input')
    def test_categorize_existing(self):
        newKeys = {'hello', 'world', 'its', 'me'}
        existing = {
            '1': ['hello'],
            '3': ['me']
            }

        expected = {
            '1': ['hello', 'world'],
            '2': ['its'],
            '3': ['me']
            }

        print('test existing')
        print(expected)
        actual = categorizer.categorize(newKeys)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
