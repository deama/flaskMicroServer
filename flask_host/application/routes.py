from flask import request, render_template
from application import app
import requests





@app.route("/")
def home():
    buttons = ["Get Random Number", "Get Random Letter", "Generate Random Sequence", "Send Random Generated Sequence to Prize Pool"]
    return render_template("home.html", title="Random Generator", buttons=buttons)



@app.route("/button0", methods=["GET"])
def button0():
    res = requests.post( "http://127.0.0.1:5001/getRandomNumber" )
    if res.ok:
        return res.json()

    return "request failed"


@app.route("/button1", methods=["GET"])
def button1():
    res = requests.post( "http://127.0.0.1:5002/getRandomLetter" )
    if res.ok:
        return res.json()

    return "request failed"


@app.route("/button2", methods=["GET"])
def button2():
    res = requests.post( "http://127.0.0.1:5003/getRandomSequence" )
    if res.ok:
        return res.json()

    return "request failed"
