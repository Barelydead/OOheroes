#!usr/bin/env python3

"""Hero module"""
from base import Base
import random
from sqlalchemy import Column, String, Integer, Float


class Hero(Base):
    """forum db"""
    __tablename__ = "Hero"

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

    def combat(self, villan):
        """ fight """
        while self.hp > 0 and villan.hp > 0:
            rand = random.randint(0, 100)

            if rand*0.01 > self.critical_blow:
                villan.hp -= self.damage * (villan.armor * 0.01)
            else:
                villan.hp -= self.damage



            if rand*0.01 > self.critical_blow:
                self.hp -= villan.damage * (self.armor * 0.01)
            else:
                self.hp -= villan.damage



            if self.hp < 0:
                self.hp = 0

            if villan.hp < 0:
                villan.hp = 0


        if self.hp > villan.hp:
            return villan

        return self

    def print_box(self):
        """ Print hero card """
        html = ""
        html += '''<div class="character hero">
            <img src="{img}" class="hero-icon" alt="hero-icon">
            <h2>{name}</h2>
            <p>Damage: {dmg}</p>
            <p>HP: {hp}</p>
            <p>Armor: {armor}</p>
            <p>critical blow: {c}</p>
        </div>'''.format(img=self.image, name=self.name, dmg=self.damage, \
        hp=self.hp, armor=self.armor, c=self.critical_blow)

        return html


    def __str__(self):
        """ Print """
        return "Name: {n}, HP: {h}, Damge: {d}, Armor: {a}" \
        .format(n=self.name, h=self.hp, d=self.damage, a=self.armor)
