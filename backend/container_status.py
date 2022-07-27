from dataclasses import dataclass


@dataclass
class BlkioStats:  # io_service_bytes_recursive, io_serviced_recursive
    major: int
    minor: int
    op: str
    value: int


@dataclass
class CpuUsage:
    total_usage: int
    percpu_usage: list[int]
    usage_in_kernelmode: int
    usage_in_usermode: int


@dataclass
class CpuStats:
    cpu_usage: CpuUsage
    system_cpu_usage: int
    online_cpus: int
    throttling_data: dict


@dataclass
class MemoryDetailStats:
    active_anon: int
    active_file: int
    cache: int
    dirty: int
    hierarchical_memory_limit: int
    hierarchical_memsw_limit: int
    inactive_anon: int
    inactive_file: int
    mapped_file: int
    pgfault: int
    pgmajfault: int
    pgpgin: int
    pgpgout: int
    rss: int
    rss_huge: int
    total_active_anon: int
    total_active_file: int
    total_cache: int
    total_dirty: int
    total_inactive_anon: int
    total_inactive_file: int
    total_mapped_file: int
    total_pgfault: int
    total_pgmajfault: int
    total_pgpgin: int
    total_pgpgout: int
    total_rss: int
    total_rss_huge: int
    total_unevictable: int
    total_writeback: int
    unevictable: int
    writeback: int


@dataclass
class MemoryStats:
    usage: int
    max_usage: int
    stats: MemoryDetailStats
    limit: int


@dataclass
class NetworkStats:
    rx_bytes: int
    rx_packets: int
    rx_errors: int
    rx_dropped: int
    tx_bytes: int
    tx_packets: int
    tx_errors: int
    tx_dropped: int


@dataclass
class ContainerStatus:
    read: str
    preread: str
    pids_stats: dict
    blkio_stats: dict[str, list[BlkioStats]]
    num_procs: int
    storage_stats: dict
    cpu_stats: CpuStats
    precpu_stats: CpuStats
    memory_stats: MemoryStats
    name: str
    id: str
    networks: dict[str, NetworkStats]

    def get_cpu_usage(self) -> int:
        return self.cpu_stats.cpu_usage.total_usage - self.precpu_stats.cpu_usage.total_usage

    def get_memory_uasge(self) -> int:
        return self.memory_stats.usage

    def get_network_io_receive_and_transmit(self) -> tuple[int, int]:
        io_receive, io_transmit = 0, 0

        for network, stats in self.networks.items():
            if network.startswith("eth"):
                io_receive += stats.rx_bytes
                io_transmit += stats.tx_bytes

        return io_receive, io_transmit

    def get_disk_io_read_and_write(self) -> tuple[int, int]:
        io_read, io_write = 0, 0

        for stats in self.blkio_stats.get("io_service_bytes_recursive", []):
            if stats.op == "Read":
                io_read += stats.value
            elif stats.op == "Write":
                io_write += stats.value
            elif stats.op == "Async":
                pass
            elif stats.op == "Sync":
                pass

        return io_read, io_write
