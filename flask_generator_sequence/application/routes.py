from flask import request
from application import app
import requests
import random
import string

ip = "127.0.0.1"

@app.route("/getRandomSequence", methods=["POST"])
def getSequence():
    sequence = ""
    for i in range(20):
        randomNumber = requests.post( "http://"+str(ip)+":5001/getRandomNumber" )
        randomLetter = requests.post( "http://"+str(ip)+":5002/getRandomLetter" )

        if random.randint(0,9) > 4 and randomNumber.ok and randomLetter.ok:
            sequence = sequence + str(randomNumber.json()["number"])
        else:
            sequence = sequence + str(randomLetter.json()["letter"])

    return {"sequence":sequence}



