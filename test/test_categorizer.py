import unittest
import budget.categorizer as categorizer


class AssignKeyTest(unittest.TestCase):
    @unittest.skip('requires user input')
    def test_categorize_to_existing_keymap(self):
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
