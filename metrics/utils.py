import docker
import socket
from typing import Iterator
from dacite import from_dict

from container_status import ContainerStatus


def get_containers_status() -> Iterator[ContainerStatus]:
    client = docker.DockerClient(base_url="unix:///var/run/docker.sock")
    for containers in client.containers.list():
        status = containers.stats(decode=None, stream=False)
        yield from_dict(data_class=ContainerStatus, data=status)


def save_metrics_in_database(container_metric: ContainerStatus) -> None:
    machine_name = socket.gethostname()
    server_name, server_id = container_metric.name, container_metric.id
    cpu_usage = container_metric.get_cpu_usage()
    memory_usage = container_metric.get_memory_uasge()
    network_io_receive, network_io_transmit = container_metric.get_network_io_receive_and_transmit()
    disk_io_read, disk_io_write = container_metric.get_disk_io_read_and_write()
