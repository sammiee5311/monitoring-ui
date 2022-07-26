import pytest
from sqlalchemy.orm import Session

from db.model import Metric
from db.repository import SqlAlchemyRepository
from container_status import ContainerStatus


@pytest.mark.parametrize("machine_names", [(["metric1"]), (["metric1", "metric2"])])
def test_add_metric_and_get_same_one(
    sqlite_session_factory: Session, container_status: ContainerStatus, machine_names: list[str]
) -> None:
    session = sqlite_session_factory()
    repo = SqlAlchemyRepository(session)

    server_name, server_id = container_status.name, container_status.id
    cpu_usage = container_status.get_cpu_usage()
    memory_usage = container_status.get_memory_uasge()
    network_io_receive, network_io_transmit = container_status.get_network_io_receive_and_transmit()
    disk_io_read, disk_io_write = container_status.get_disk_io_read_and_write()

    added_machine_names = []

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

        repo.add(metric)

    added_metrics = repo.get(server_id)

    for added_metric in added_metrics:
        added_machine_names.append(added_metric.machine_name)

    assert added_machine_names == machine_names
