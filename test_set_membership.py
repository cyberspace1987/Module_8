"""
Program: set_membership.py
Author: Cara Krug, 10/19/2020 cjkrug@dmacc.edu
Purpose: demonstrate the basic use of sets
"""

import unittest
from more_fun_with_collections import set_membership as set_mem


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        # create a set
        test_set = {1, 8, 4, 3, 6, 5, 7, 2}
        # test to see if the set contains an element
        self.assertTrue(set_mem.in_set(test_set, 3))

    def test_in_set_false(self):
        # create a set
        test_set = {1, 8, 4, 3, 6, 5, 7, 2}
        # test to see if the set contains an element
        self.assertFalse(set_mem.in_set(test_set, 0))


if __name__ == '__main__':
    unittest.TestCase()
