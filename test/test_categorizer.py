import unittest
from unittest import TestCase as Test
from collections import OrderedDict
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


class TestMakeMenu(Test):
    def runTest(self):
        d = {
            'one': ['some descriptions'],
            'two': ['some descriptions'],
            'three': ['some descriptions']
            }

        expected = OrderedDict([(1, 'one'), (2, 'two'), (3, 'three')])
        actual = categorizer.make_menu(d)

        self.assertDictEqual(expected, actual)


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
            'a': ['hello'],
            'b': ['its'],
            'c': ['husband']
            }

        expected = {
            'a': ['hello', 'honey'],
            'b': ['its', 'me'],
            'c': ['your', 'husband'],
            'd': ['ralph']
            }

        print("honey: a,  me: b,  your: c,  ralph: d")
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
        expected = {'a': ['HELLO'], 'b': ['WORLD']}

        for k, v in expected.items():
            print('{0}: {1}'.format(k, v))
        actual = categorizer.merge_categories(newKeys, existing)

        self.assertDictEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
