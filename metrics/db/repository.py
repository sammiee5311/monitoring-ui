from abc import ABC, abstractmethod
from db.model import Metric
from sqlalchemy.orm import Session


class AbstractRepository(ABC):
    def add(self, metric: Metric) -> None:
        self._add(metric)

    @abstractmethod
    def _add(self, metric: Metric) -> None:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def _add(self, metric: Metric) -> None:
        self.session.add(metric)
