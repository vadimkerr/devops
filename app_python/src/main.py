from datetime import datetime

import pytz
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def current_time():
    tz = pytz.timezone("Europe/Moscow")
    return datetime.now().astimezone(tz)
