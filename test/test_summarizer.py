import datetime
import unittest
from unittest import TestCase as Test
import budget.summarizer as summarizer


class TestGetTransactionAmount(Test):
    def test_returns_value_of_withdrawal_or_deposit(self):
        withdrawal = {'Withdrawals': '$45.0', 'Deposits': ''}
        deposit = {'Withdrawals': '', 'Deposits': '$30.0'}
        error_case = {'Withdrawals': '', 'Deposits': ''}

        self.assertAlmostEqual(
            45.0, summarizer.get_transaction_amount(withdrawal))
        self.assertAlmostEqual(
            30.0, summarizer.get_transaction_amount(deposit))
        self.assertAlmostEqual(
            0.0, summarizer.get_transaction_amount(error_case))


class TestInvertDict(Test):
    def test_invert_dict(self):
        dict_to_invert = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9]}
        expected = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3}

        actual = summarizer.invert_dict(dict_to_invert)

        self.assertEqual(list(expected.keys()), list(actual.keys()))
        for key in expected:
            self.assertEqual(expected[key], actual[key])


class TestIsRelevant(Test):
    def test_returns_true_if_given_matching_description(self):
        transaction = {'Description': 'hello darkness my old friend', 'Date': '03'}
        description = 'darkness'
        non_matching_descr = 'sandwich'

        self.assertTrue(summarizer.is_relevant(transaction, description, 3))
        self.assertFalse(summarizer.is_relevant(transaction, non_matching_descr, 3))

    def test_returns_true_if_date_is_in_range(self):
        month = '03'
        wrong_month = '06'
        transaction = {'Description': 'hello', 'Date': month}
        description = 'hello'

        self.assertTrue(summarizer.is_relevant(transaction, description, int(month)))
        self.assertFalse(summarizer.is_relevant(transaction, description, int(wrong_month)))


class SummarizerTest(Test):
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

        _month = str(datetime.datetime.now().month)
        if len(_month) == 1:
            _month = ''.join(['0', _month])
        self.month = _month

    def test_summarize_ignores_noise(self):
        activity = [
            {'Description': 'kroger #450', 'Withdrawals': '$10.0', 'Deposits': '', 'Date': self.month},
            {'Description': 'paycheck from work', 'Withdrawals': '', 'Deposits': '$1,000.0', 'Date': self.month},
            {'Description': 'jimmy johns - downtown', 'Withdrawals': '$5.0', 'Deposits': '', 'Date': self.month},
            {'Description': 'electric company', 'Withdrawals': '25.25', 'Deposits': '', 'Date': self.month},
            {'Description': 'marathon gas station', 'Withdrawals': '$15.5', 'Deposits': '$30.0', 'Date': self.month},
            {'Description': 'water utility co', 'Withdrawals': '$25.0', 'Deposits': '', 'Date': self.month},
            {'Description': 'local grocery store', 'Withdrawals': '$10.0', 'Deposits': '', 'Date': self.month},
        ]

        expected = {'food': 25.0, 'gas': 15.5, 'bill': 50.25, 'income': 1000.0}
        actual = summarizer.summarize(self.categories, activity)

        self.assertSummariesEqual(expected, actual)

    def test_summarizer_ignores_uknown_activity(self):
        activity = [
            {'Description': 'kroger #450', 'Withdrawals': '$10.0', 'Deposits': '', 'Date': self.month},
            {'Description': 'who knows', 'Withdrawals': '$5.0', 'Deposits': '', 'Date': self.month},
            {'Description': 'marathon', 'Withdrawals': '$15.5', 'Deposits': '$30.0', 'Date': self.month},
            {'Description': 'water utility co', 'Withdrawals': '$25.0', 'Deposits': '', 'Date': self.month},
            {'Description': 'something', 'Withdrawals': '25.25', 'Deposits': '', 'Date': self.month},
        ]

        expected = {'food': 10.0, 'gas': 15.5, 'bill': 25.0, 'income': 0.0}
        actual = summarizer.summarize(self.categories, activity)

        self.assertSummariesEqual(expected, actual)

    def test_summarizer_ignores_entries_from_out_of_range_months(self):
        previous_months = ('02', '01')
        activity = [
            {'Description': 'kroger', 'Withdrawals': '$10.0', 'Deposits': '', 'Date': self.month},
            {'Description': 'paycheck', 'Withdrawals': '', 'Deposits': '$1,000.0', 'Date': self.month},
            {'Description': 'jimmy johns', 'Withdrawals': '$5.0', 'Deposits': '', 'Date': previous_months[0]},
            {'Description': 'electric', 'Withdrawals': '25.25', 'Deposits': '', 'Date': previous_months[0]},
            {'Description': 'marathon', 'Withdrawals': '$15.5', 'Deposits': '$30.0', 'Date': previous_months[1]},
            {'Description': 'water', 'Withdrawals': '$25.0', 'Deposits': '', 'Date': previous_months[1]}
        ]

        expected = {'food': 10.0, 'gas': 0.0, 'bill': 0.0, 'income': 1000.0}
        actual = summarizer.summarize(self.categories, activity)

        self.assertSummariesEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
