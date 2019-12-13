from flask import request, render_template
from application import app

@app.route("/", methods=["GET"])
def get_test():
    return {"name":"bob"}

@app.route("/post-test", methods=["POST", "GET"])
def post_test():
    print(request.json)
    return "OK"



