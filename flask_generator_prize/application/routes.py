from flask import request
from application import app
import requests
import random
import string




@app.route("/getPrize", methods=["POST"])
def getPrize():
    sequence = request.json["sequence"]
    if len(sequence) == 20:
        try:
            if int(sequence[0]) == int(sequence[0]):
                try:
                    if int(sequence[2]) == int(sequence[2]):
                        try:
                            if int(sequence[7]) == int(sequence[7]):
                                return {"prize":"999,999"}
                        except ValueError:
                            return {"prize":"99,999"}
                except ValueError: 
                    return {"prize":"9,999"}
        except ValueError:
            pass

    return {"prize":"X"}
