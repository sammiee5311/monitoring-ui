import os

from dotenv import load_dotenv

load_dotenv(".env")

USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("DB_PASSWORD")
HOST = os.environ.get("DB_HOST")
PORT = os.environ.get("DB_PORT")
DATABASE_NAME = os.environ.get("DB_NAME")


def get_database_uri() -> str:
    return f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
