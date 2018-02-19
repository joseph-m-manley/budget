import unittest
from budget.CategoryMap import CategoryMap
from unittest import TestCase as Test, main

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

if __name__ == '__main__':
    unittest.main()
