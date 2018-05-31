import werobot

robot = werobot.WeRoBot(token="weidoudou")

@robot.text
def hello():
    return "hello"

robot.config["HOST"] = "127.0.0.1"
robot.config["PORT"] = 8082
robot.run()

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "hello"

# app.run(host="127.0.0.1", port=8082)