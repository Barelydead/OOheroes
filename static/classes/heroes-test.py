#!/usr/bin/env python3
""" Module for unittests """


import unittest
from heros import Hero
from villans import Villan

class Testcase(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    first = Hero(
        name="Punisher",
        hp=400,
        damage=40.0,
        armor=25.2,
        image="img",
        critical_blow=0.4)

    second = Hero(
        name="Coolio",
        hp=200,
        damage=22.2,
        armor=15.1,
        image="col.jpg",
        critical_blow=0.8)

    vil = Villan(
        name="second Vil",
        hp=300,
        damage=20,
        armor=15.1,
        image="pic",
        critical_blow=0.1)

    def test_attribute(self):
        """ return true if values are the same """

        self.assertEqual(self.first.name, "Punisher")
        self.assertEqual(self.second.name, "Coolio")
        self.assertEqual(self.first.hp, 400)
        self.assertEqual(self.second.image, "col.jpg")
        self.assertEqual(self.second.critical_blow, 0.8)

    def test_if_instance_notequal(self):
        """ Return true if instance is not same """
        self.assertIsNot(self.first, self.second)

    def test_if_instance_equal(self):
        """ Return true if instance is same """
        self.assertIs(self.first, self.first)

    def test_type(self):
        """ Return true if value is correct type """
        self.assertTrue(isinstance(self.second.critical_blow, float))
        self.assertTrue(isinstance(self.second.image, str))
        self.assertTrue(isinstance(self.first.damage, float))


    def test_combat_function(self):
        """ return true if function subracats HP """
        self.assertEqual(self.first.hp, 400)

        self.first.combat(self.vil)

        self.assertTrue(self.first.hp < 400)


if __name__ == '__main__':
    unittest.main()
