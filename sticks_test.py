import unittest
from sticks import *

class SticksTest(unittest.TestCase):

    test_dict = {key: [1, 2, 3] for key in range(1, 101)}


    def test_adjust_rem_sticks(self):
        guess = 2
        self.assertEqual(adjust_rem_sticks(30, guess), 28)
        self.assertEqual(adjust_rem_sticks(3, 2), 1)

    def test_get_max_guess(self):
        self.assertEqual(get_max_guess(30), 3)
        self.assertEqual(get_max_guess(2), 2)

    def test_print_board(self):
        output = print_board(30)
        self.assertEqual(output, "There are 30 sticks on the board.")

    def test_is_loser(self):
        self.assertFalse(is_loser(30))
        self.assertTrue(is_loser(0))

    def test_is_valid_number(self):
        self.assertTrue(is_valid_number(30, 100))
        self.assertFalse(is_valid_number('a', 100))
        self.assertFalse(is_valid_number(300, 100))
        self.assertTrue(is_valid_number(11, 100, 10))
        self.assertFalse(is_valid_number('abc', 3))

    def test_get_version(self):
        output = get_version()
        self.assertTrue(output == '1' or output == '2')

    def test_make_a_guess(self):
        guess = make_a_guess(5, self.test_dict)
        self.assertTrue(guess in self.test_dict[5])

    def test_add_guess_to_hat(self):
        new_dict = add_guess_to_hat(4, 5, self.test_dict)
        self.assertEqual(new_dict[5], [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
