from container_status import ContainerStatus


def test_container_server_name(container_status: ContainerStatus) -> None:
    server_name, server_id = container_status.name, container_status.id

    assert server_name == "test"
    assert server_id == "test"


def test_get_container_metrics(container_status: ContainerStatus) -> None:
    cpu_usage = container_status.get_cpu_usage()
    memory_usage = container_status.get_memory_uasge()
    network_io_receive, network_io_transmit = container_status.get_network_io_receive_and_transmit()
    disk_io_read, disk_io_write = container_status.get_disk_io_read_and_write()

    assert cpu_usage == 0
    assert memory_usage == 1
    assert network_io_receive == 1 and network_io_transmit == 1
    assert disk_io_read == 1 and disk_io_write == 2
