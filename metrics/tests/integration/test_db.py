import pytest
from sqlalchemy.orm import Session

from db.sql_alchemy import SqlAlchemyDB
from db.model import Metric
from container_status import ContainerStatus

from typing import Callable


def test_add_metric_to_database_and_get_utils(
    sqlite_session_factory: Callable[[], Session], container_status: ContainerStatus
) -> None:
    db = SqlAlchemyDB(sqlite_session_factory)

    server_name, server_id = container_status.name, container_status.id
    cpu_usage = container_status.get_cpu_usage()
    memory_usage = container_status.get_memory_uasge()
    network_io_receive, network_io_transmit = container_status.get_network_io_receive_and_transmit()
    disk_io_read, disk_io_write = container_status.get_disk_io_read_and_write()

    metric = Metric(
        "machine",
        server_name,
        server_id,
        cpu_usage,
        memory_usage,
        network_io_receive,
        network_io_transmit,
        disk_io_read,
        disk_io_write,
    )

    with pytest.raises(Exception):
        with db:
            db.session.add(metric)
            raise Exception

    new_session = sqlite_session_factory()
    rows = list(new_session.execute("SELECT * FROM metrics"))

    assert rows == []
