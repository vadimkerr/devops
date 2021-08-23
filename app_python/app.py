from datetime import datetime

import pytz as pytz
from flask import Flask

app = Flask(__name__)


@app.route("/")
def current_time():
    tz = pytz.timezone("Europe/Moscow")
    return str(datetime.now().astimezone(tz))
