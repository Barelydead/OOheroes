#!usr/bin/env python3

"""Villan module"""
from base import Base
from sqlalchemy import Column, String, Integer, Float

class Villan(Base):
    """forum db"""
    __tablename__ = "Villan"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hp = Column(Float)
    armor = Column(Float)
    damage = Column(Float)
    image = Column(String)
    critical_blow = Column(Float)


    def __init__(self, **kwargs):
        """ init method """
        valid_keys = ["name", "hp", "armor", "damage", "image", "critical_blow"]

        for key in valid_keys:
            self.__dict__[key] = kwargs.get(key)


    def combat(self, hero):
        """ fight """
        while self.hp > 0 or hero.hp > 0:
            self.hp -= hero.damage * (self.armor * 0.01)
            hero.hp -= self.damage * (hero.armor * 0.01)

        if self.hp > hero.hp:
            return hero

        return self


    def __str__(self):
        """ Print """
        return "Name: {n}, HP: {h}, Damge: {d}, Armor: {a}" \
        .format(n=self.name, h=self.hp, d=self.damage, a=self.armor)
