import unittest
import json
from unittest import TestCase as Test
from budget.Classes import Description, Category, Data


class TestDescription(Test):
    def test_removes_noise(self):
        description = 'noise xxxx1234 activity city state'
        noise = ['noise', 'x+\\d+', 'city', 'state']

        expected = 'activity'
        actual = Description(description, noise)
        self.assertEqual(expected, actual)


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
        self.assertTrue(isinstance(data.get_noise(), list))
        self.assertTrue(isinstance(data.get_categories(), dict))
        self.assertTrue(isinstance(data.get_budget(), dict))


if __name__ == '__main__':
    unittest.main()
