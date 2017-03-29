#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template, request
from controller import Controller


app = Flask(__name__)
# Make it easier to debug
app.debug = True
app.config.update(
    PROPAGATE_EXCEPTIONS=True
)

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/sandbox", methods=["GET", "POST"])
def sandbox():
    """ sandbox route """
    if request.method == "POST":
        if request.form["type"] == "hero":
            Controller().add_hero()
        if request.form["type"] == "villan":
            Controller().add_villan()

    return render_template("sandbox.html", controller=Controller())


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """ edit route """
    if request.method == "GET":
        if request.args.get("remove") == "hero":
            Controller().remove_hero()
        if request.args.get("edit") == "hero":
            Controller().edit_hero()
        if request.args.get("quest") == "true":
            name = request.args.get("name")
            Controller().add_quest(name)

    return render_template("edit.html", controller=Controller())

@app.route("/quests", methods=["GET", "POST"])
def quests():
    """ quests route """
    if request.method == "GET":
        if request.args.get("quest") == "true":
            name = request.args.get("name")
            Controller().add_quest(name)



    return render_template("quests.html", controller=Controller())


@app.route("/results", methods=["GET", "POST"])
def results():
    """ results route """
    if request.args.get("quest") == "false":

        heroList = request.args.getlist("hero")
        questVariables = Controller().set_fight(heroList)

        Controller().exec_fight(questVariables)

        Controller().make_bet()

    if request.method == "POST":
        Controller().reset_history()

    return render_template("results.html", controller=Controller())


@app.route("/chars", methods=["GET", "POST"])
def chars():
    """ chars route """
    if request.method == "GET":
        if request.args.get("init") == "true":
            Controller().init_db()


        if request.args.get("remove") == "hero":
            Controller().remove_hero()
        elif request.args.get("remove") == "villan":
            Controller().remove_villan()
        if request.args.get("edit") == "hero":
            Controller().edit_hero()
        elif request.args.get("edit") == "villan":
            Controller().edit_villan()

    if request.method == "POST":
        if request.form["type"] == "hero":
            Controller().add_hero()
        if request.form["type"] == "villan":
            Controller().add_villan()


    return render_template("chars.html", controller=Controller())

@app.route("/bets", methods=["GET", "POST"])
def bets():
    """ bets route """
    if request.method == "POST":
        Controller().add_funds()

    return render_template("bets.html", controller=Controller())

@app.route("/addchar", methods=["GET", "POST"])
def addchar():
    """ addchar route """

    return render_template("addchar.html", controller=Controller())



if __name__ == "__main__":
    app.run()
