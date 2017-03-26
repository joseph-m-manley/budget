import unittest
import summarizer


class HelpersTest(unittest.TestCase):
    def test_invert_dict(self):
        dict_to_invert = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9]}
        expected = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3}

        actual = summarizer.invert_dict(dict_to_invert)

        self.assertEqual(list(expected.keys()), list(actual.keys()))
        for key in expected:
            self.assertEqual(expected[key], actual[key])


if __name__ == '__main__':
    unittest.main()
