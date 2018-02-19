from budget.CategoryMap import CategoryMap
from budget.Data import Data, filter_noise
from json import dump
from os import remove
from unittest import TestCase as Test
from unittest import main


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
        self.assertTrue(isinstance(data.get_conditioned_descriptions(), (list, set)))
        self.assertTrue(isinstance(data.get_noise(), list))
        self.assertTrue(isinstance(data.get_categories(), (CategoryMap, dict)))
        self.assertTrue(isinstance(data.get_budget(), dict))

    def test_filter_noise(self):
        words = ['hello xxxx1234', 'foo world', 'its#9999', '    me   ']
        noise = ["foo", "#\\d+", "X+\\d{4}"]

        expected = ['hello', 'world', 'its', 'me']
        actual = filter_noise(words, noise)

        self.assertListEqual(expected, actual)

    def test_filter_noise_always_strips_whitespace(self):
        words = [' 1hello1 ', ' 2world2 ', ' 3its3 ', ' 4me4 ']
        noise = ["\\d+"]

        expected = ['hello', 'world', 'its', 'me']
        actual = filter_noise(words, noise)

        self.assertListEqual(expected, actual)

    def test_filter_noise_returns_original_if_noise_is_empty(self):
        words = ['hello xxxx1234', 'foo world', 'its#9999', '    me   ']
        noise = []

        expected = ['hello xxxx1234', 'foo world', 'its#9999', 'me']
        actual = filter_noise(words, noise)

        self.assertListEqual(expected, actual)

    def test_filter_noise(self):
        all_descriptions = [
            "ach debit       xxxxx0987 electricity ",
            "ach debit       1-1abcdef gas ",
            "debit card purchase   xxxxx1234 apples #118            city st ",
            "ach webrecur   xxxxx6161 school ",
            "debit card purchase   xxxxx4321 coffee    city st ",
            "debit card purchase   xxxxx1234 razor blades m5789          city      st ",
            "debit card purchase   xxxxx4321 sandwich meat             city st ",
            "recurring debit card  xxxxx5678 water             xxxxx9622 st ",
            "debit card purchase   xxxxx4321 pipe tobacco           xxxxx4000  st ",
            "debit card purchase   xxxxx1234 bar soap       xxxxx9100 st ",
            "debit card purchase   xxxxx5678 shoes    city      st "
        ]

        noise = [
            "DEBIT CARD PURCHASE\\s+",
            "ACH DEBIT\\s+",
            "RECURRING DEBIT CARD\\s+",
            "X{5}\\d{4}\\s+",
            "\\bCITY\\b",
            "\\bST\\b"
        ]

        expected = [
            'electricity', 
            '1-1abcdef gas', 
            'apples #118', 
            'ach webrecur   school', 
            'coffee',
			'razor blades m5789',
			'sandwich meat',
			'water',
			'pipe tobacco',
			'bar soap',
			'shoes'
        ]

        actual = filter_noise(all_descriptions, noise)
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    main()
