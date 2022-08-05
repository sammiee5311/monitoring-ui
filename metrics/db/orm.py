from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import mapper

from db.model import Metric

metadata = MetaData()

metrics = Table(
    "metrics",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("create_date", DateTime(timezone=True), default=func.now()),
    Column("machine_name", String(50)),
    Column("server_name", String(50)),
    Column("server_id", String(100)),
    Column("cpu_usage", Integer),
    Column("memory_usage", Integer),
    Column("network_io_receive", Integer),
    Column("network_io_transmit", Integer),
    Column("disk_io_read", Integer),
    Column("disk_io_write", Integer),
)


mapper(Metric, metrics)
