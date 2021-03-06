"""
CS-362 Assignment 5
Adam Wright

Unit test file
"""


import unittest
import task
from datetime import date


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

    def test_first_last(self):
        test_list = [1, 5, 3, 6, 8, 9, 24, 56]

        test_1 = task.first_last(test_list)

        self.assertEqual(test_1, [1, 56])

    def test_two_dates(self):
        date1 = date(2020, 1, 20)
        date2 = date(2020, 2, 15)

        test = task.two_dates(date1, date2)

        self.assertEqual(test, 26)


if __name__ == '__main__':
    unittest.main()
