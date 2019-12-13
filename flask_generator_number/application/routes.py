from flask import request
from application import app
import requests
import random

@app.route("/getRandomNumber", methods=["POST"])
def getNumber():
    return {"number":random.randint(0, 9)}



