from flask import Flask
from werobot.contrib.flask import make_view

from app.robot import robot

app = Flask(__name__)
app.add_url_rule(
    rule = "/robot/",
    endpoint = "werobot",
    view_func = make_view(robot),
    methods = ["GET", "POST"]
)
