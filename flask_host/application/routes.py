from flask import request, render_template, session
from application import app, db
from application.models import Sequences
import requests
import os

#db.create_all()

#ip = "35.240.6.143"
ip = os.getenv("IP")


buttons = ["Get Random Number", "Get Random Letter", "Generate Random Sequence", "Send Random Generated Sequence to Prize Pool"]


@app.route("/")
def home():
    return render_template("home.html", title="Random Generator", buttons=buttons)



@app.route("/button0", methods=["GET"])
def button0():
    res = requests.post( "http://"+str(ip)+":5001/getRandomNumber" )
    if res.ok:
        return res.json()

    return "request failed"


@app.route("/button1", methods=["GET"])
def button1():
    res = requests.post( "http://"+str(ip)+":5002/getRandomLetter" )
    if res.ok:
        return res.json()

    return "request failed"


@app.route("/button2", methods=["GET"])
def button2():
    res = requests.post( "http://"+str(ip)+":5003/getRandomSequence" )
    if res.ok:
        session["sequence"] = res.json()["sequence"]

        return render_template("home.html", title="Random Generator", buttons=buttons, sequence=session.get("sequence","not set") )

    return "request failed"

@app.route("/button3", methods=["GET"])
def button3():
    res = requests.post( "http://"+str(ip)+":5004/getPrize", json={"sequence":session.get("sequence","not set")} )
    if res.ok:
        return "You have won: " + res.json()["prize"]

    return "request failed"
