import unittest
import summarizer


class HelpersTest(unittest.TestCase):
    def test_invert_dict(self):
        dict_to_invert = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9]}
        expected = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3}

        actual = summarizer.invert_dict(dict_to_invert)

        self.assertEqual(list(expected.keys()), list(actual.keys()))
        for key in expected:
            self.assertEqual(expected[key], actual[key])

    def test_get_transaction_amount(self):
        withdrawal = {'Withdrawals': '45.0', 'Deposits': ''}
        deposit = {'Withdrawals': '', 'Deposits': '30.0'}
        error_case = {'Withdrawals': '', 'Deposits': ''}

        self.assertAlmostEqual(
            45.0, summarizer.get_transaction_amount(withdrawal))
        self.assertAlmostEqual(
            30.0, summarizer.get_transaction_amount(deposit))
        self.assertEqual(
            0.0, summarizer.get_transaction_amount(error_case))


class SummarizerTest(unittest.TestCase):
    def test_summarize(self):
        categories = {
            'food': ['kroger', 'grocery', 'jimmy johns'],
            'gas': ['marathon'],
            'bill': ['electric', 'water'],
            'income': ['paycheck']
            }
        activity = [
            {'Description': 'kroger #450', 'Withdrawals': '10.0', 'Deposits': ''},
            {'Description': 'local grocery store', 'Withdrawals': '10.0', 'Deposits': ''},
            {'Description': 'jimmy johns - downtown', 'Withdrawals': '5.0', 'Deposits': ''},
            {'Description': 'marathon', 'Withdrawals': '15.5', 'Deposits': '30.0'},
            {'Description': 'electric company', 'Withdrawals': '25.25', 'Deposits': ''},
            {'Description': 'water utility co', 'Withdrawals': '25.0', 'Deposits': ''},
            {'Description': 'paycheck from work', 'Withdrawals': '', 'Deposits': '100.0'}
        ]

        expected = {'food': 25.0, 'gas': 15.5, 'bill': 50.25, 'income': 100.0}
        actual = summarizer.summarize(categories, activity)

        self.assertEqual(len(expected.keys()), len(actual.keys()))
        for k in expected:
            self.assertAlmostEqual(expected[k], actual[k])


if __name__ == '__main__':
    unittest.main()
