from sqlalchemy.orm import Session

from utils import get_metrics_from_docker, add_metric_to_database
from db.sql_alchemy import SqlAlchemyDB
from container_status import ContainerStatus


def test_add_metric_to_database_and_get_utils(
    sqlite_session_factory: Session, container_status: ContainerStatus
) -> None:
    db = SqlAlchemyDB(sqlite_session_factory)

    add_metric_to_database(db, *get_metrics_from_docker(container_status))

    with db:
        metrics = db.metric.get(server_id="test")

        assert metrics[-1].server_id == "test"
