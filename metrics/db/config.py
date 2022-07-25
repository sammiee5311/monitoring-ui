import os

from dotenv import load_dotenv

load_dotenv("./config/.env")

USER = os.environ["DB_USER"]
PASSWORD = os.environ["DB_PASSWORD"]
HOST = os.environ["DB_HOST"]
PORT = os.environ["DB_PORT"]
DATABASE_NAME = os.environ["DB_NAME"]


def get_database_uri() -> str:
    return f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
