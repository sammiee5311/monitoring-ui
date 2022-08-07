import docker
import socket
from typing import Iterator
from dacite import from_dict

from container_status import ContainerStatus
from db.sql_alchemy import SqlAlchemyDB
from db.model import Metric
from log import logger


def get_containers_status() -> Iterator[ContainerStatus]:
    client = docker.DockerClient(base_url="unix:///var/run/docker.sock")
    for containers in client.containers.list():
        status = containers.stats(decode=None, stream=False)
        yield from_dict(data_class=ContainerStatus, data=status)


def get_metrics_from_docker(container_metric: ContainerStatus) -> tuple[str, str, str, int, int, int, int, int, int]:
    machine_name = socket.gethostname()
    server_name, server_id = container_metric.name, container_metric.id
    cpu_usage = container_metric.get_cpu_usage()
    memory_usage = container_metric.get_memory_uasge()
    network_io_receive, network_io_transmit = container_metric.get_network_io_receive_and_transmit()
    disk_io_read, disk_io_write = container_metric.get_disk_io_read_and_write()

    logger.info(f"Getting container metrics from {machine_name}-{server_name}")

    return (
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


def add_metric_to_database(
    db: SqlAlchemyDB,
    machine_name: str,
    server_name: str,
    server_id: str,
    cpu_usage: int,
    memory_usage: int,
    network_io_receive: int,
    network_io_transmit: int,
    disk_io_read: int,
    disk_io_write: int,
):

    with db:
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
