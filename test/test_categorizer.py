from budget.Categorizer import Categorizer
from budget.CategoryMap import CategoryMap
from unittest import TestCase as Test, main


class InputFake():
    def __init__(self, expected_categorymap):
        self.categorymap = expected_categorymap
        self.known_keys = [key for category in self.categorymap for key in self.categorymap[category]]
        
    def determine_key_and_category(self, description):
        key = self.ask_for_key(description)
        category = self.ask_for_category(key)
        return (key, category)

    def ask_for_category(self, key):
        for category in self.categorymap:
            if key in self.categorymap[category]:
                return category        
        return None  
    
    def ask_for_key(self, unknown):
        if len(unknown) < 15:
            return unknown
        for key in self.known_keys:
            if key in unknown:
                return key        
        return None

class TestCategorize(Test):
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

        expected = CategoryMap({
            'a': ['hello', 'honey'],
            'b': ['its', 'me'],
            'c': ['your', 'husband'],
            'd': ['ralph']
        })

        c = Categorizer(CategoryMap(known_categories), InputFake(expected))
        actual = c.categorize(all_descriptions)
    
        self.assertEqual(expected, actual)

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

        expected = CategoryMap({
            'a': ['hello'],
            'b': ['husband'],
            'c': ['world']
        })

        c = Categorizer(CategoryMap(known_categories), InputFake(expected))
        actual = c.categorize(all_descriptions)

        self.assertEqual(expected, actual)

    def test_with_realistic_data(self):
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

        known_categories = {
            'food': ['apples', 'coffee'],
            'bills': ['electricity', 'gas'],
            'home': ['bar soap']
        }

        expected = CategoryMap({
            'food': ['apples', 'coffee', 'sandwich meat'],
            'bills': ['electricity', 'gas', 'school', 'water'],
            'home': ['bar soap', 'razor blades', 'pipe tobacco', 'shoes']    
        })

        c = Categorizer(CategoryMap(known_categories), InputFake(expected))
        actual = c.categorize(all_descriptions)
            
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
