import unittest
import json
from unittest import TestCase as Test
from budget.Classes import CategoryMap, Description, Description2, Category, Data, Input


class TestCategoryMap(Test):
    def test_add_and_get(self):
        expected = {
            'a': ['hello', 'world'],
            'b': ['its', 'me']
        }

        c = CategoryMap({'a': ['hello'], 'b': ['its']})
        c.add('a', 'world')
        c.add('b', 'me')

        self.assertListEqual(
            c.get('a'),
            expected['a']
        )

        self.assertListEqual(
            c['a'],
            expected['a']
        )

    def test_eq(self):
        c = CategoryMap({
            'a': ['hello', 'world'],
            'b': ['its', 'me']
        })

        eq = CategoryMap({
            'a': ['hello', 'world'],
            'b': ['its', 'me']
        })

        neq = CategoryMap({
            'a': ['hello', 'me'],
            'b': ['its', 'world']
        })

        self.assertEqual(c, eq)
        self.assertNotEqual(c, neq)

    def test_iterates(self):
        expected = {
            'a': ['hello', 'world'],
            'b': ['its', 'me']
        }
        c = CategoryMap(expected)

        for category in c:
            self.assertListEqual(
                c[category],
                expected[category]
            )

    def test_len(self):
        c = CategoryMap({
            'a': ['hello', 'world'],
            'b': ['its', 'me']
        })

        self.assertEqual(2, len(c))

    def test_contains(self):
        c = CategoryMap({
            'a': ['hello', 'world'],
            'b': ['its', 'me']
        })

        self.assertTrue('a' in c)

class TestCategoryMapKeywordExists(Test):
    def test_keyword_exists(self):
        c = CategoryMap({
            'a': ['hello', 'world'],
            'b': ['its', 'me']
        })

        contains = 'world on fire'
        doesnt = 'rabbit punch'

        self.assertTrue(c.keyword_exists(contains))
        self.assertFalse(c.keyword_exists(doesnt))

    def test_finds_keyword_among_noise(self):
        c = CategoryMap({
            'a': ['hello', 'world'],
            'b': ['its', 'important-stuff']
        })
        
        description = 'zim zam BORKBIRK.important-stuff-obfuscated-hereXXXX9990'

        self.assertTrue(c.keyword_exists(description))


class TestDescription(Test):
    def test_removes_noise(self):
        description = 'noise xxxx1234 activity city state'
        noise = ['noise', 'x+\\d+', 'city', 'state']

        expected = 'activity'
        actual = Description(description, noise)
        self.assertEqual(expected, actual)


class TestDescription2(Test):
    def test(self):
        d = Description2("hello darkness my old friend")
        d.contains_any("darkness")
        d.contains_none("world")


class TestCategory(Test):
    def test_belongs(self):
        food = Category(['aldi', 'kroger', 'marsh'])
        does = 'debit card purchase aldi xxxxx1234 city state'
        doesnt = 'noise xxxx1234 activity city state'

        self.assertTrue(food.belongs(does))
        self.assertFalse(food.belongs(doesnt))


class TestData(Test):
    def setUp(self):
        self.path = 'test_paths.json'
        test_paths = {
            "activity": "user/checking/february.csv",
            "categories": "user/categories.json",
            "noise": "user/noise.json",
            "budget": "user/budget.json"
        }

        with open(self.path, 'w+') as file:
            json.dump(test_paths, file, indent=4)

    def tearDown(self):
        import os
        os.remove(self.path)

    def test_data(self):
        data = Data(self.path)
        self.assertTrue(isinstance(data.get_descriptions(), (list, set)))
        self.assertTrue(isinstance(data.get_normalized_descriptions(), (list, set)))
        self.assertTrue(isinstance(data.get_noise(), list))
        self.assertTrue(isinstance(data.get_categories(), (CategoryMap, dict)))
        self.assertTrue(isinstance(data.get_budget(), dict))

@unittest.skip('Requires user input')
class TestInput(Test):
    def test_ask_for_category(self):
        expected = 'hello'
        print(expected)
        actual = Input().ask_for_category()

        self.assertEqual(expected, actual)


    def test_ask_for_key_for_descriptions_longer_than_15_char(self):
        expected = 'string'
        print(expected)
        actual = Input().ask_for_key('what you need to type is \'string\'')

        self.assertEqual(expected, actual)

    def test_does_not_ask_for_key_for_descriptions_shorter_than_15_char(self):
        expected = 'short'
        actual = Input().ask_for_key('short')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
