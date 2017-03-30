import unittest
from unittest import TestCase as Test
import budget.categorizer as categorizer


class TestFlatten(Test):
    def runTest(self):
        nested_list = [[1, 2], [3, 4, 5], [6], [], [7, 8, 9]]

        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = categorizer.flatten(nested_list)

        self.assertEqual(expected, actual)


class TestAddCategory(Test):
    def add_category_adds_to_set_or_creates_new_set(self):
        expected = {1: {1, 2}, 2: {3}}
        actual = {1: {1}}

        categorizer.add_category(actual, 1, 2)
        categorizer.add_category(actual, 2, 3)

        self.assertEqual(len(expected.keys()), len(actual.keys()))
        for k in expected:
            self.assertEqual(expected[k], actual[k])


class TestMergeCategories(Test):
    @unittest.skip('requires user input')
    def test_categorize_should_ignore_duplicates(self):
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
        actual = categorizer.merge_categories(newKeys, existing)

        for key in expected:
            self.assertEqual(sorted(expected[key]), sorted(actual[key]))

    @unittest.skip('requires user input')
    def test_categorize_should_not_ask_if_entry_matches_existing_key(self):
        newKeys = {
            'bing bang boom hello',
            'frazzle hello dazzle',
            'world is so very big',
            'oh what a wonderful world'
            }

        existing = dict()
        expected = {'1': ['HELLO'], '2': ['WORLD']}

        print('hello: 1,  world: 2')
        actual = categorizer.merge_categories(newKeys, existing)

        self.assertEqual(list(expected.keys()), list(actual.keys()))
        for key in expected:
            self.assertEqual(sorted(expected[key]), sorted(actual[key]))


if __name__ == '__main__':
    unittest.main()
