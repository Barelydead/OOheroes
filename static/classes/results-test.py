#!/usr/bin/env python3
""" Module for unittests """


import unittest
from results import Result
class Testcase(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    first = Result("First Quest", "Tom, Punisher", "Magneto, Cyclops", "Heroes")
    second = Result("This_Quest", "Super Mario", "Tom Riddle", "Bad guys")

    def test_attribute(self):
        """ return true if values are the same """

        self.assertEqual(self.first.quest_name, "First Quest")
        self.assertEqual(self.second.quest_name, "This_Quest")
        self.assertEqual(self.first.winner, "Heroes")
        self.assertEqual(self.second.villans, "Tom Riddle")

    def test_if_instance_notequal(self):
        """ Return true if instance is not same """
        self.assertIsNot(self.first, self.second)

    def test_if_instance_equal(self):
        """ Return true if instance is not same """
        self.assertIs(self.first, self.first)

    def test_type(self):
        """ Return true if value is correct type """
        self.assertTrue(isinstance(self.second.villans, str))
        self.assertTrue(isinstance(self.second.heroes, str))
        self.assertTrue(isinstance(self.first.quest_name, str))




if __name__ == '__main__':
    unittest.main()
