from data import ContainerStatus
from datetime import time


TEST_CONTAINER_STATUS = {
    "read": time(),
    "preread": time(),
    "pids_stats": {"current": 1},
    "blkio_stats": {
        "io_service_bytes_recursive": [],
        "io_serviced_recursive": [],
    },
    "num_procs": 0,
    "storage_stats": {},
    "cpu_stats": {
        "cpu_usage": {
            "total_usage": 10,
            "percpu_usage": [1, 2, 3, 4, 5, 6, 7, 8],
            "usage_in_kernelmode": 10,
            "usage_in_usermode": 10,
        },
        "system_cpu_usage": 10,
        "online_cpus": 8,
        "throttling_data": {"periods": 0, "throttled_periods": 0, "throttled_time": 0},
    },
    "precpu_stats": {
        "cpu_usage": {
            "total_usage": 10,
            "percpu_usage": [1, 2, 3, 4, 5, 6, 7, 8],
            "usage_in_kernelmode": 10,
            "usage_in_usermode": 10,
        },
        "system_cpu_usage": 10,
        "online_cpus": 8,
        "throttling_data": {"periods": 0, "throttled_periods": 0, "throttled_time": 0},
    },
    "memory_stats": {
        "usage": 1,
        "max_usage": 1,
        "stats": {
            "active_anon": 0,
            "active_file": 0,
            "cache": 0,
            "dirty": 0,
            "hierarchical_memory_limit": 1,
            "hierarchical_memsw_limit": 1,
            "inactive_anon": 1,
            "inactive_file": 0,
            "mapped_file": 0,
            "pgfault": 1,
            "pgmajfault": 0,
            "pgpgin": 1,
            "pgpgout": 1,
            "rss": 1,
            "rss_huge": 0,
            "total_active_anon": 0,
            "total_active_file": 0,
            "total_cache": 0,
            "total_dirty": 0,
            "total_inactive_anon": 1,
            "total_inactive_file": 0,
            "total_mapped_file": 0,
            "total_pgfault": 1,
            "total_pgmajfault": 0,
            "total_pgpgin": 1,
            "total_pgpgout": 1,
            "total_rss": 1,
            "total_rss_huge": 0,
            "total_unevictable": 0,
            "total_writeback": 0,
            "unevictable": 0,
            "writeback": 0,
        },
        "limit": 1,
    },
    "name": "test",
    "id": "test",
    "networks": {
        "eth0": {
            "rx_bytes": 1,
            "rx_packets": 1,
            "rx_errors": 0,
            "rx_dropped": 0,
            "tx_bytes": 0,
            "tx_packets": 0,
            "tx_errors": 0,
            "tx_dropped": 0,
        }
    },
}


def test_container_status_data() -> None:
    container_status = ContainerStatus(**TEST_CONTAINER_STATUS)

    assert container_status.id == "test"
