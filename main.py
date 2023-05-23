
from dotenv import dotenv_values
from flask import Flask, jsonify

from ai import make_ai_decision

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({ "name": "AI Decision Maker!",
                     "description": "Use cutting edge technology to answer yes/no questions.",
                     "instructions": "Think carefully about a decision you need to make, then make a GET request to /decide."})

@app.route("/decide", methods=["GET"])
def decide():
    return jsonify({ "decision": make_ai_decision() })

if __name__ == "__main__":

    config = dotenv_values()
    print(config)
    app.run(debug=int(config["DEBUG"]),
            port=config["PORT"],
            host=config["HOST"])
