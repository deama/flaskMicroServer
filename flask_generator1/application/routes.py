from flask import request
from application import app
import requests

@app.route("/", methods=["GET"])
def get_test():
    requests.post( "http://127.0.0.1:5000/post-test", json={"name":"Bob"} )
    return "SENT"



