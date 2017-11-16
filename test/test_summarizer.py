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
        transaction = {'Description': 'hello darkness my old friend'}
        description = 'darkness'
        non_matching_descr = 'sandwich'

        self.assertTrue(summarizer.is_relevant(transaction, description))
        self.assertFalse(summarizer.is_relevant(transaction, non_matching_descr))


class TestSummarizer(Test):
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

    def test_summarize_ignores_noise(self):
        activity = [
            {'Description': 'kroger #450', 'Withdrawals': '$10.0', 'Deposits': ''},
            {'Description': 'paycheck from work', 'Withdrawals': '', 'Deposits': '$1,000.0'},
            {'Description': 'jimmy johns - downtown', 'Withdrawals': '$5.0', 'Deposits': ''},
            {'Description': 'electric company', 'Withdrawals': '25.25', 'Deposits': ''},
            {'Description': 'marathon gas station', 'Withdrawals': '$15.5', 'Deposits': '$30.0'},
            {'Description': 'water utility co', 'Withdrawals': '$25.0', 'Deposits': ''},
            {'Description': 'local grocery store', 'Withdrawals': '$10.0', 'Deposits': ''},
        ]

        expected = {'food': 25.0, 'gas': 15.5, 'bill': 50.25, 'income': 1000.0}
        actual = summarizer.summarize(self.categories, activity)

        self.assertSummariesEqual(expected, actual)

    def test_summarizer_ignores_uknown_activity(self):
        activity = [
            {'Description': 'kroger #450', 'Withdrawals': '$10.0', 'Deposits': ''},
            {'Description': 'who knows', 'Withdrawals': '$5.0', 'Deposits': ''},
            {'Description': 'marathon', 'Withdrawals': '$15.5', 'Deposits': '$30.0'},
            {'Description': 'water utility co', 'Withdrawals': '$25.0', 'Deposits': ''},
            {'Description': 'something', 'Withdrawals': '25.25', 'Deposits': ''},
        ]

        expected = {'food': 10.0, 'gas': 15.5, 'bill': 25.0, 'income': 0.0}
        actual = summarizer.summarize(self.categories, activity)

        self.assertSummariesEqual(expected, actual)


class TestSubtractExpenses(Test):
    def test_correctly_subtracts_expenses(self):
        budget = {'one': 50.5, 'two': 21.7, 'three': 34.7}
        expenses = {'one': 23.5, 'two': 11.3, 'three': 1.0}

        expectedRemaining = {'one': 27.0, 'two': 10.4, 'three': 33.7}
        actualRemaining = summarizer.subtract_expenses(budget, expenses)

        self.assertDictEqual(expectedRemaining, actualRemaining)


class TestCalculateTotals(Test):
    def test_ignores_empty_budget(self):
        expenses = {'one': 1, 'two': 2, 'three': 3}
        budget = summarizer.calculate_totals(dict(), expenses)

        expectedBudget = {'expenses': expenses}

        self.assertDictEqual(budget, expectedBudget)


if __name__ == '__main__':
    unittest.main()
