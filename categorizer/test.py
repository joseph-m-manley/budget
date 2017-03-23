import categorizer
import unittest


class Test(unittest.TestCase):
    def test_normalize(self):
        activity = [
            "RECURRING DEBIT CARD  XXXXX1234 NETFLIX.COM               NETFLIX.COM CA ",
            "DEBIT CARD PURCHASE   XXXXX1234 KROGER #959               CITY      ST ",]

        noise = [
            "DEBIT CARD",
            "RECURRING",
            "PURCHASE",
            "NETFLIX.COM CA",
            "CITY",
            "ST",
            "#\\d+",
            "X+\\d{4}",
            "\\b\\d+\\b",
        ]

        actual = categorizer.normalize(activity, noise)
        expected = {'NETFLIX.COM', 'KROGER'}
        self.assertEqual(expected, actual)

    def test_flatten(self):
        nested_list = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        actual = categorizer.flatten(nested_list)

        self.assertEqual(expected, actual)

    def test_categorize_new(self):
        newKeys = {'hello', 'world', 'its', 'me'}
        expected = {
            '1': {'hello', 'world'},
            '2': {'its'},
            '3': {'me'}
            }

        print('test new')
        print(expected)
        actual = categorizer.categorize(newKeys)

        self.assertEqual(expected, actual)

    def test_categorize_existing(self):
        newKeys = {'world', 'me'}
        categories = {
            '1': {'hello'},
            '2': {'its'}
            }
        expected = {
            '1': {'hello', 'world'},
            '2': {'its'},
            '3': {'me'}
            }

        print('test existing')
        print(expected)
        actual = categorizer.categorize(newKeys, categories)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
