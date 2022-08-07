"""
This is scheduler.
"""

__version__ = "0.1"

import os
from docker.errors import NotFound
from apscheduler.schedulers.background import BlockingScheduler
from db.sql_alchemy import SqlAlchemyDB
from dotenv import load_dotenv

from log import logger
from utils import get_containers_status, get_metrics_from_docker, add_metric_to_database


load_dotenv("./config/.env")

SCHEDULER_TIME = os.environ["SCHEDULER_TIME"]
SCHEDULER_ID = os.environ["SCHEDULER_ID"]
SCHEDULER_TRIGGER = os.environ["SCHEDULER_TRIGGER"]
SCHEDULER_TIMEZONE = os.environ["SCHEDULER_TIMEZONE"]

db = SqlAlchemyDB()


def main() -> None:
    try:
        containers_metrics = get_containers_status()
        for container_metric in containers_metrics:
            add_metric_to_database(db, *get_metrics_from_docker(container_metric))

    except (KeyError, NotFound) as err:
        logger.warning(f"Server cannot save metrics: {err}")


if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone=SCHEDULER_TIMEZONE)
    scheduler.add_job(main, SCHEDULER_TRIGGER, seconds=SCHEDULER_TIME, id=SCHEDULER_ID)
    scheduler.start()
