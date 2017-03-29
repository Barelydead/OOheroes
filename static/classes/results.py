#!usr/bin/env python3

"""Result module"""
from base import Base
from sqlalchemy import Column, String, Integer

class Result(Base):
    """forum db"""
    __tablename__ = "Result"

    id = Column(Integer, primary_key=True)
    quest_name = Column(String)
    heroes = Column(String)
    villans = Column(String)
    winner = Column(String)

    def __init__(self, quest_name, heroes, villans, winner):
        """ init method """
        self.quest_name = quest_name
        self.heroes = heroes
        self.villans = villans
        self.winner = winner

    def print_all(self):
        """ print all """
        html = ""
        html += """
            <h2>{n}</h2>
            <p>Winning team: <span class="winner">{w}</span></p>
        """.format(n=self.quest_name, w=self.winner)


        return html

    def __str__(self):
        """ Print """
        return "quest_name: {n}, heroes: {h}, villans: {v}, winner: {w}" \
        .format(n=self.quest_name, h=self.heroes, v=self.villans, w=self.winner)
