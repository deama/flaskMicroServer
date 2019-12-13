from flask import request
from application import app
import requests
import random
import string

@app.route("/getPrize", methods=["POST"])
def getPrize():
    return {"prize":"not implemented yet"}



