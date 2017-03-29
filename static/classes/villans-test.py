#!/usr/bin/env python3
""" Module for unittests """


import unittest
from villans import Villan

class Testcase(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    first = Villan(
        name="first Vil",
        hp=200,
        damage=10.1,
        armor=25.2,
        image="img",
        critical_blow=0.1)

    second = Villan(
        name="second Vil",
        hp=300,
        damage=20,
        armor=15.1,
        image="pic",
        critical_blow=0.1)

    def test_attribute(self):
        """ return true if values are the same """

        self.assertEqual(self.first.name, "first Vil")
        self.assertEqual(self.second.name, "second Vil")
        self.assertEqual(self.first.hp, 200)
        self.assertEqual(self.second.image, "pic")
        self.assertEqual(self.second.critical_blow, 0.1)

    def test_if_instance_notequal(self):
        """ Return true if instance is not same """
        self.assertIsNot(self.first, self.second)

    def test_if_instance_equal(self):
        """ Return true if instance is the same """
        instance = self.first
        self.assertIs(self.first, instance)

    def test_type(self):
        """ Return true if value is correct type """
        self.assertTrue(isinstance(self.second.critical_blow, float))
        self.assertTrue(isinstance(self.second.image, str))
        self.assertTrue(isinstance(self.first.name, str))
        self.assertTrue(isinstance(self.first.damage, float))


if __name__ == '__main__':
    unittest.main()
