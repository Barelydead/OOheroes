""" Controller module """

#Import all classes
from static.classes.results import Result
from static.classes.quests import Quest
from static.classes.heros import Hero
from static.classes.villans import Villan
from static.classes.bets import Bets

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from flask import request
import random

class Controller():
    """ Controller class """
    engine = create_engine("sqlite:///db/blackops.sqlite",\
    connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()


    def __init__(self):
        """ init """
        self.heroes = []
        self.villans = []
        self.quests = []
        self.results = []
        self.bets = []

        heroes = Controller.session.query(Hero).all()
        villans = Controller.session.query(Villan).all()
        quests = Controller.session.query(Quest).all()
        results = Controller.session.query(Result).all()
        bets = Controller.session.query(Bets).all()

        for hero in heroes:
            self.heroes.append(hero)
        for villan in villans:
            self.villans.append(villan)
        for quest in quests:
            self.quests.append(quest)
        for result in results:
            self.results.append(result)
        for bet in bets:
            self.bets.append(bet)


    def add_hero(self):
        """ add hero to DB """
        new_hero = Hero(
            name=request.form["name"],
            hp=request.form["hp"],
            armor=request.form["armor"],
            damage=request.form["damage"],
            image="static/uploads/" + str(request.form["image"]),
            critical_blow=request.form["crit"])

        Controller.session.add(new_hero)
        Controller.session.commit()

    def add_villan(self):
        """ add villan to DB """

        new_villan = Villan(
            name=request.form["name"],
            hp=request.form["hp"],
            damage=request.form["damage"],
            armor=request.form["armor"],
            image="static/uploads/" + str(request.form["image"]),
            critical_blow=request.form["crit"])

        Controller.session.add(new_villan)
        Controller.session.commit()


    def init_db(self):
        """ Init db with base characters """
        Controller.session.query(Hero).delete()
        Controller.session.query(Villan).delete()

        villan1 = Villan(
            name="Deadpool",
            hp="150",
            damage="50",
            armor="10",
            image="static/uploads/deadpool.png",
            critical_blow=0.2)

        villan2 = Villan(
            name="Blaster",
            hp="250",
            damage="70",
            armor="30",
            image="static/uploads/blaster.png",
            critical_blow=0.15)

        villan3 = Villan(
            name="Brainiac",
            hp="500",
            damage="5",
            armor="10",
            image="static/uploads/brainiac.png",
            critical_blow=0.25)

        hero1 = Hero(
            name="Cat woman",
            hp="122",
            damage="33",
            armor="15",
            image="static/uploads/catwoman.png",
            critical_blow=0.3)

        hero2 = Hero(
            name="Punisher",
            hp="150",
            damage="40",
            armor="25",
            image="static/uploads/punisher.png",
            critical_blow=0.34)

        hero3 = Hero(
            name="spawn",
            hp="200",
            damage="50",
            armor="50",
            image="static/uploads/spawn.png",
            critical_blow=0.21)


        Controller.session.add_all([villan1, villan2, villan3, hero1, hero2, hero3])
        Controller.session.commit()



    def edit_hero(self):
        """ Edit a hero """
        hero = Controller.session.query(Hero).filter(Hero.id == request.args.get("editId"))
        hero.update({"name": request.args.get("name")})
        hero.update({"hp": request.args.get("hp")})
        hero.update({"damage": request.args.get("damage")})
        hero.update({"armor": request.args.get("armor")})
        hero.update({"critical_blow": request.args.get("crit")})


        Controller.session.commit()

    def edit_villan(self):
        """ Edit a hero """
        villan = Controller.session.query(Villan).filter(Villan.id == request.args.get("editId"))
        villan.update({"name": request.args.get("name")})
        villan.update({"hp": request.args.get("hp")})
        villan.update({"damage": request.args.get("damage")})
        villan.update({"armor": request.args.get("armor")})
        villan.update({"critical_blow": request.args.get("crit")})


        Controller.session.commit()

    def remove_hero(self):
        """ remove hero """
        Controller.session.query(Hero).filter(Hero.id == request.args.get("editId")).delete()

        Controller.session.commit()

    def remove_villan(self):
        """ remove hero """
        Controller.session.query(Villan).filter(Villan.id == request.args.get("editId")).delete()

        Controller.session.commit()

    def add_quest(self, name):
        """ randomize villans for quest """
        random.shuffle(self.villans)

        healty_villans = []
        for vil in self.villans:
            if vil.hp > 0:
                healty_villans.append(vil)

        if len(healty_villans) > 0:
            numberOfVillans = random.randint(1, len(healty_villans))
            numberOfVillans = random.randint(1, numberOfVillans)

            quest = Quest(name)

            for i in range(numberOfVillans):
                quest.villans += str(healty_villans[i].name) + ", "

            quest.villans = quest.villans[:-2]

            Controller.session.add(quest)
            Controller.session.commit()

        else:
            quest = Quest(name)
            quest.villans = ""

            Controller.session.add(quest)
            Controller.session.commit()

    def check_available_chars(self):
        """ Check that hero and vill have HP """
        her = 0
        vil = 0

        for hero in self.heroes:
            if hero.hp > 0:
                her += 1

        for villan in self.villans:
            if villan.hp > 0:
                vil += 1

        if vil > 0 and her > 0:
            return "true"

        return "false"


    def print_quest(self):
        """ Print quest """
        villanList = self.quests[-1].villans.split(", ")

        html = ""

        for villan in villanList:
            for vi in self.villans:
                if str(villan) == vi.name:
                    html += '''<div class="character villan">
                        <img src="{img}" class="hero-icon" alt="hero-icon">
                        <h2>{name}</h2>
                        <p>Damage: {dmg}</p>
                        <p>HP: {hp}</p>
                        <p>Armor: {armor}</p>
                        <p>critical blow: {c}</p>
                    </div>'''.format(img=vi.image, name=vi.name, dmg=vi.damage, \
                    hp=vi.hp, armor=vi.armor, c=vi.critical_blow)

        if html == "":
            return 'No Villans available. Go to characters to edit or add new'


        return html

    def set_fight(self, heroes):
        """ fight """
        quest_name = self.quests[-1].name
        qVillans = self.quests[-1].villans
        villans = []
        i = 0

        for hero in heroes:
            for myHero in self.heroes:
                if str(hero) == myHero.name:
                    heroes[i] = myHero
                    i += 1

        for vil in qVillans.split(", "):
            for myVillan in self.villans:
                if vil == myVillan.name:
                    villans.append(myVillan)

        return [quest_name, villans, heroes]

    def exec_fight(self, questVariables):
        """ Run fight algoritm """
        quest_name = questVariables[0]
        quest_villans = questVariables[1]
        quest_heroes = questVariables[2]
        winner = "Villans"
        beat_villans = []
        beat_heroes = []
        villan = ""
        hero = ""

        while len(quest_heroes) > 0 and len(quest_villans) > 0:
            looser = quest_heroes[0].combat(quest_villans[0])

            if looser == quest_heroes[0]:
                popped = quest_heroes.pop(0)
                beat_heroes.append(popped)

            if looser == quest_villans[0]:
                popped = quest_villans.pop(0)
                beat_villans.append(popped)

        if len(quest_heroes) > len(quest_villans):
            winner = "Heroes"

        for villans in quest_villans:
            villan += "<p>" + villans.name + ": " + str(round(villans.hp)) + "hp left</p>"

        for villans in beat_villans:
            villan += "<p>" + villans.name + ": " + str(round(villans.hp)) + "hp left</p>"

        for heroes in quest_heroes:
            hero += "<p>" + heroes.name + ": " + str(round(heroes.hp)) + "hp left</p>"

        for heroes in beat_heroes:
            hero += "<p>" + heroes.name + ": " + str(round(heroes.hp)) + "hp left</p>"


        new_result = Result(
            quest_name=quest_name,
            heroes=hero,
            villans=villan,
            winner=winner
        )

        Controller.session.add(new_result)
        Controller.session.commit()

    def make_bet(self):
        """Bet on winning team"""
        if request.args.get("betamount") and request.args.get("winteam"):

            bet = int(request.args.get("betamount"))
            quest_name = self.results[-1].quest_name
            balance = self.bets[-1].balance

            if self.results[-1].winner.lower() == request.args.get("winteam"):
                balance += bet
                outcome = "Bet won"
            else:
                balance -= bet
                outcome = "Bet lost"


            new_bet = Bets(
                quest_name=quest_name,
                balance=balance,
                bet=bet,
                outcome=outcome)

            Controller.session.add(new_bet)
            Controller.session.commit()

    def get_last_balance(self):
        """ Last balance """
        return self.bets[-1].balance

    def table_bets(self):
        """ table bets """
        html = ""
        for bet in reversed(self.bets):
            html += """<tr>
            <td>{q}</td>
            <td>{bal}</td>
            <td>{bet}</td>
            <td>{o}</td>2
            </tr>""".format(\
            q=bet.quest_name, bal=bet.balance, bet=bet.bet, o=bet.outcome)

        return html

    def table_results(self):
        """ table bets """
        html = ""
        for result in reversed(self.results):
            html += """<tr>
            <td>{q}</td>
            <td>{vil}</td>
            <td>{her}</td>
            <td>{win}</td>2
            </tr>""".format(\
            q=result.quest_name, vil=result.villans, her=result.heroes, win=result.winner)

        return html

    def add_funds(self):
        """ add funds """
        Controller.session.query(Bets).delete()

        new_bet = Bets(
            quest_name="Reset balance",
            balance=5000,
            bet=0,
            outcome="Success")

        Controller.session.add(new_bet)
        Controller.session.commit()

    def reset_history(self):
        """ add funds """
        Controller.session.query(Result).delete()

        Controller.session.commit()
