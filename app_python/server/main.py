from datetime import datetime
from pathlib import Path

import aiofiles
import pytz
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
file_path = Path("data/last-visited.txt")


@app.get("/")
async def current_time():
    tz = pytz.timezone("Europe/Moscow")
    now = str(datetime.now(tz=tz))

    file_path.parent.mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(file_path, mode="w") as file:
        await file.write(now)

    return now


@app.get("/visits")
async def visits():
    if not file_path.exists():
        return None

    return FileResponse(file_path)
