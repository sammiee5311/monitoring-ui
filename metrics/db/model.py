class Metric:
    def __init__(
        self,
        machine_name: str,
        server_name: str,
        server_id: str,
        cpu_usage: int,
        memory_usage: int,
        network_io_receive: int,
        network_io_transmit: int,
        disk_io_read: int,
        disk_io_write: int,
    ) -> None:
        self.machine_name = machine_name
        self.server_name = server_name
        self.server_id = server_id
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.network_io_receive = network_io_receive
        self.network_io_transmit = network_io_transmit
        self.disk_io_read = disk_io_read
        self.disk_io_write = disk_io_write
