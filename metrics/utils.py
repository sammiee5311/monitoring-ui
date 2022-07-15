import docker
from typing import Iterator

from data import ContainerStatus


def get_containers_status() -> Iterator[ContainerStatus]:
    client = docker.DockerClient(base_url="unix:///var/run/docker.sock")
    for containers in client.containers.list():
        status = containers.stats(decode=None, stream=False)
        yield ContainerStatus(**status)


def save_metrics_in_database(container_metric: ContainerStatus) -> None:
    print(container_metric)
