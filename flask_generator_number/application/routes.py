from flask import request
from application import app
import requests
import random

@app.route("/getRandomNumber", methods=["POST"])
def get_test():
    return {"number":random.randint(0, 9)}



