import unittest
import budget.summarizer as summarizer


class HelpersTest(unittest.TestCase):
    def test_get_transaction_amount(self):
        withdrawal = {'Withdrawals': '$45.0', 'Deposits': ''}
        deposit = {'Withdrawals': '', 'Deposits': '$30.0'}
        error_case = {'Withdrawals': '', 'Deposits': ''}

        self.assertAlmostEqual(
            45.0, summarizer.get_transaction_amount(withdrawal))
        self.assertAlmostEqual(
            30.0, summarizer.get_transaction_amount(deposit))
        self.assertAlmostEqual(
            0.0, summarizer.get_transaction_amount(error_case))


class SummarizerTest(unittest.TestCase):
    def assertSummariesEqual(self, expected, actual):
        self.assertEqual(len(expected.keys()), len(actual.keys()))
        for k in expected:
            self.assertAlmostEqual(expected[k], actual[k])

    def setUp(self):
        self.categories = {
            'food': ['kroger', 'grocery', 'jimmy johns'],
            'gas': ['marathon'],
            'bill': ['electric', 'water'],
            'income': ['paycheck']
            }

    def test_summarize_should_summarize(self):
        month = '03'
        activity = [
            {'Description': 'kroger #450', 'Withdrawals': '$10.0', 'Deposits': '', 'Date': month},
            {'Description': 'paycheck from work', 'Withdrawals': '', 'Deposits': '$1,000.0', 'Date': month},
            {'Description': 'jimmy johns - downtown', 'Withdrawals': '$5.0', 'Deposits': '', 'Date': month},
            {'Description': 'electric company', 'Withdrawals': '25.25', 'Deposits': '', 'Date': month},
            {'Description': 'marathon', 'Withdrawals': '$15.5', 'Deposits': '$30.0', 'Date': month},
            {'Description': 'water utility co', 'Withdrawals': '$25.0', 'Deposits': '', 'Date': month},
            {'Description': 'local grocery store', 'Withdrawals': '$10.0', 'Deposits': '', 'Date': month},
        ]

        expected = {'food': 25.0, 'gas': 15.5, 'bill': 50.25, 'income': 1000.0}
        actual = summarizer.summarize(self.categories, activity)

        self.assertSummariesEqual(expected, actual)

    def test_summarizer_should_ignore_uknown_activity(self):
        month = '03'
        activity = [
            {'Description': 'kroger #450', 'Withdrawals': '$10.0', 'Deposits': '', 'Date': month},
            {'Description': 'who knows', 'Withdrawals': '$5.0', 'Deposits': '', 'Date': month},
            {'Description': 'marathon', 'Withdrawals': '$15.5', 'Deposits': '$30.0', 'Date': month},
            {'Description': 'water utility co', 'Withdrawals': '$25.0', 'Deposits': '', 'Date': month},
            {'Description': 'something', 'Withdrawals': '25.25', 'Deposits': '', 'Date': month},
        ]

        expected = {'food': 10.0, 'gas': 15.5, 'bill': 25.0, 'income': 0.0}
        actual = summarizer.summarize(self.categories, activity)

        self.assertSummariesEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
