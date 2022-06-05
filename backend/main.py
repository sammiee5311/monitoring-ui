"""
This is fast-api.
"""

__version__ = "0.1"

import os
import uvicorn
import sentry_sdk

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

load_dotenv("./config/.env")

sentry_sdk.init(dsn=os.environ["SENTRY_DNS"], environment=os.environ["SENTRY_ENV"])

HOST = os.environ["SERVER_HOST"]
PORT = int(os.environ["SERVER_PORT"])
ORIGINS = ["localhost:8000"]

app = FastAPI()

app.add_middleware(SentryAsgiMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "It is a backend server."}


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
