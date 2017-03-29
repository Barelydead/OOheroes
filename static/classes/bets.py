#!usr/bin/env python3

"""bets module"""
from base import Base
from sqlalchemy import Column, String, Integer

class Bets(Base):
    """forum db"""
    __tablename__ = "Bets"

    id = Column(Integer, primary_key=True)
    quest_name = Column(String)
    balance = Column(Integer)
    bet = Column(Integer)
    outcome = Column(String)

    def __init__(self, quest_name, balance, bet, outcome):
        """ init method """
        self.quest_name = quest_name
        self.balance = balance
        self.bet = bet
        self.outcome = outcome

    def __str__(self):
        """ """
        return """quest_name: {n}, balance: {b}, bet: {bet}, outcome: {o}
        """.format(n=self.quest_name, b=self.balance, bet=self.bet, o=self.outcome)
