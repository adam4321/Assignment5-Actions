"""
CS-362 Assignment 5
Adam Wright

Unit test file
"""


import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_circle_area(self):
        test_1 = 1
        test_2 = 5
        test_3 = 11.7

        test_1 = task.circle_area(test_1)
        test_2 = task.circle_area(test_2)
        test_3 = task.circle_area(test_3)

        self.assertEqual(test_1, 3.141593)
        self.assertEqual(test_2, 78.539816)
        self.assertEqual(test_3, 430.052618)


if __name__ == '__main__':
    unittest.main()
