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
    def add_category_adds_to_list_or_creates_new(self):
        expected = {1: {1, 2}, 2: {3}}
        actual = {1: {1}}

        categorizer.add_category(actual, 1, 2)
        categorizer.add_category(actual, 2, 3)

        self.assertDictEqual(expected, actual)


class InputFake():
    def __init__(self, expected_categorymap):
        self.expected_categorymap = expected_categorymap
        self.known_keys = [key for values in expected_categorymap.values() for key in values]
        
    def ask_for_category(self, key):
        for category in self.expected_categorymap:
            if key in self.expected_categorymap[category]:
                return category
        
        return None  
    
    def ask_for_key(self, unknown):
        if len(unknown) < 15:
            return unknown
        for key in self.known_keys:
            if key in unknown:
                return key
        
        return None

class TestMergeWithCategories(Test):
    def test_should_ignore_duplicate_descriptions(self):
        all_descriptions = [
            'hello',
            'honey',
            'its',
            'me',
            'your',
            'husband',
            'ralph',
            'honey xyz',
            'your xyz',
            'ralph xyz'
        ]

        known_categories = {
            'a': ['hello'],
            'b': ['its'],
            'c': ['husband']
        }

        known_keys = ['hello', 'its', 'husband']

        expected = {
            'a': ['hello', 'honey'],
            'b': ['its', 'me'],
            'c': ['your', 'husband'],
            'd': ['ralph']
        }

        actual = categorizer.merge_with_categories(
                    known_categories, 
                    known_keys, 
                    all_descriptions, 
                    InputFake(expected))

        for key in expected:
            self.assertListEqual(sorted(expected[key]), sorted(actual[key]))

    def test_should_ignore_known_descriptions(self):
        all_descriptions = [
            'bing bang boom hello',
            'its me your husband ralph',
            'the world is so very big',
        ]

        known_categories = {
            'a': ['hello'],
            'b': ['husband']
        }

        known_keys = ['hello', 'husband']

        expected = {
            'a': ['hello'],
            'b': ['husband'],
            'c': ['world']
        }

        actual = categorizer.merge_with_categories(
                    known_categories,
                    known_keys,
                    all_descriptions,
                    InputFake(expected))

        for key in expected:
            self.assertListEqual(sorted(expected[key]), sorted(actual[key]))


if __name__ == '__main__':
    unittest.main()
