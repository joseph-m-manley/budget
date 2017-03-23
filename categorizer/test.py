import categorizer
import unittest


class Test(unittest.TestCase):
    def test_filter_noise(self):
        activity = [
            "RECURRING DEBIT CARD  XXXXX1234 NETFLIX.COM               NETFLIX.COM CA ",
            "DEBIT CARD PURCHASE   XXXXX1234 KROGER #959               CITY      ST "]

        noise = [
            "DEBIT CARD",
            "RECURRING",
            "PURCHASE",
            "NETFLIX.COM CA",
            "CITY",
            "ST",
            "#\\d+",
            "X+\\d{4}",
        ]

        actual = categorizer.filter_noise(activity, noise)
        expected = {'NETFLIX.COM', 'KROGER'}
        self.assertEqual(expected, actual)

    @unittest.skip('requires user input')
    def test_categorize_existing(self):
        newKeys = {'hello', 'world', 'its', 'me'}
        expected = {
            '1': {'hello', 'world'},
            '2': {'its'},
            '3': {'me'}
            }

        print('test existing')
        print(expected)
        actual = categorizer.categorize(newKeys)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
