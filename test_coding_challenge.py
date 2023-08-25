import unittest
from coding_challenge import count_sum_pairs


class TestCountSumPairs(unittest.TestCase):
    def test_no_pairs(self):
        self.assertEqual(count_sum_pairs([3, 4, 5, 6], 1), 0)
        self.assertEqual(count_sum_pairs([-10, 0, 13, 17, 25], 1), 0)

    def test_one_pair(self):
        self.assertEqual(count_sum_pairs([0, 15, 32, 2000, 15000], 15), 1)
        self.assertEqual(count_sum_pairs([1, 4, 6, 8, 11], 10), 1)

    def test_multiple_pairs(self):
        self.assertEqual(count_sum_pairs([1, 1, 10, 32, 41], 42), 2)
        self.assertEqual(count_sum_pairs([3, 3, 16, 16, 35], 19), 2)
        self.assertEqual(count_sum_pairs([3, 3, 16, 16, 16, 35], 19), 2)
        self.assertEqual(count_sum_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 4)

    def test_negative_target(self):
        self.assertEqual(count_sum_pairs([0, 10, 13, 17, 25], -10), 0)
        self.assertEqual(count_sum_pairs([-10, 0, 13, 17, 25], -10), 1)
        self.assertEqual(count_sum_pairs([-25, -10, -7, 0, 8, 17, 25], -17), 2)
        self.assertEqual(count_sum_pairs([-25, -10, -7, 0, 8, 17, 25], 0), 1)

    def test_raises_type_error_when_string_in_array_1(self):
        with self.assertRaises(TypeError):
            count_sum_pairs([3, 4, "5", 6], 1)

    def test_raises_type_error_when_string_in_array_2(self):
        with self.assertRaises(TypeError):
            count_sum_pairs(["3", "4", "5", "6"], 1)

    def test_raises_type_error_when_float_in_array_1(self):
        with self.assertRaises(TypeError):
            count_sum_pairs([3, 4.0, 5, 6], 1)

    def test_raises_type_error_when_float_in_array_2(self):
        with self.assertRaises(TypeError):
            count_sum_pairs([0.25, 4.0, 10000.5, 15007], 10004.5)

    def test_raises_type_error_when_target_string(self):
        with self.assertRaises(TypeError):
            count_sum_pairs([3, 4, 5, 6], "4")

    def test_raises_type_error_when_target_float(self):
        with self.assertRaises(TypeError):
            count_sum_pairs([3, 4, 5, 6], 9.0)


if __name__ == '__main__':
    unittest.main()
