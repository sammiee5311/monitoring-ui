from sqlalchemy.orm import Session

from utils import get_grafana_servers
from db.model import Metric
from db.sql_alchemy import SqlAlchemyDB
from container_status import ContainerStatus


def test_getting_grafana_servers(sqlite_session_factory: Session, container_status: ContainerStatus) -> None:
    machine_names = ["machine1", "machine2"]
    server_name, server_id = container_status.name, container_status.id
    cpu_usage = container_status.get_cpu_usage()
    memory_usage = container_status.get_memory_uasge()
    network_io_receive, network_io_transmit = container_status.get_network_io_receive_and_transmit()
    disk_io_read, disk_io_write = container_status.get_disk_io_read_and_write()

    db = SqlAlchemyDB(sqlite_session_factory)

    with db:
        for machine_name in machine_names:
            metric = Metric(
                machine_name,
                server_name,
                server_id,
                cpu_usage,
                memory_usage,
                network_io_receive,
                network_io_transmit,
                disk_io_read,
                disk_io_write,
            )
            db.session.add(metric)
            db.commit()

    servers = get_grafana_servers(db)

    assert len(servers) == 1
