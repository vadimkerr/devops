import pytz as pytz
from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def current_time():
    tz = pytz.timezone("Europe/Moscow")
    return str(datetime.now().astimezone(tz))
