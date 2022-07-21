from __future__ import annotations

import os

from dotenv import load_dotenv
from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from db.repository import AbstractRepository, SqlAlchemyRepository

load_dotenv("./config/.env")

USER = os.environ["DB_USER"]
PASSWORD = os.environ["DB_PASSWORD"]
HOST = os.environ["DB_HOST"]
PORT = os.environ["DB_PORT"]
DATABASE_NAME = os.environ["DB_NAME"]
DATABASE_URI = f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/metrics"

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        DATABASE_URI,
        isolation_level="REPEATABLE READ",
    )
)


class AbstractDB(ABC):
    metric: AbstractRepository

    def __enter__(self) -> AbstractDB:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class SqlAlchemyDB(AbstractDB):
    def __init__(self, session_factory: sessionmaker = DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session: Session = self.session_factory()
        self.metric = SqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
