#!usr/bin/env python3

"""Quest module"""
from base import Base
from sqlalchemy import Column, String, Integer

class Quest(Base):
    """forum db"""
    __tablename__ = "Quest"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    villans = Column(String)

    def __init__(self, name):
        """ init method """
        self.name = name
        self.villans = ""


    def __str__(self):
        return "Name: {n}, villans: {v}".format(n=self.name, v=str(self.villans))
