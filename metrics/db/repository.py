from abc import ABC, abstractmethod
from db.model import Metric
from sqlalchemy.orm import Session


class AbstractRepository(ABC):
    def add(self, metric: Metric) -> None:
        self._add(metric)

    def get(self, server_id: str) -> list[Metric]:
        metric = self._get(server_id)

        return metric

    @abstractmethod
    def _add(self, metric: Metric) -> None:
        raise NotImplementedError

    @abstractmethod
    def _get(self, server_id: str) -> list[Metric]:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def _add(self, metric: Metric) -> None:
        self.session.add(metric)

    def _get(self, server_id: str) -> list[Metric]:
        return self.session.query(Metric).filter(Metric.server_id.startswith(server_id))
