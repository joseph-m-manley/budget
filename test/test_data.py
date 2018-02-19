from budget.CategoryMap import CategoryMap
from budget.Data import Data
from json import dump
from os import remove
from unittest import TestCase as Test
from unittest import main as run_test


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
            dump(test_paths, file, indent=4)

    def tearDown(self):
        remove(self.path)

    def test_data(self):
        data = Data(self.path)
        self.assertTrue(isinstance(data.get_descriptions(), (list, set)))
        self.assertTrue(isinstance(data.get_normalized_descriptions(), (list, set)))
        self.assertTrue(isinstance(data.get_noise(), list))
        self.assertTrue(isinstance(data.get_categories(), (CategoryMap, dict)))
        self.assertTrue(isinstance(data.get_budget(), dict))


if __name__ == '__main__':
    run_test()
