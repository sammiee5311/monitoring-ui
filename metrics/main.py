"""
This is scheduler.
"""

__version__ = "0.1"


from docker.errors import NotFound
from apscheduler.schedulers.background import BlockingScheduler
from db.config import SqlAlchemyDB

from utils import get_containers_status, get_metrics_from_docker, add_metric_to_database


SCHEDULER_TIME = 60
SCHEDULER_ID = "metrics"
SCHEDULER_TRIGGER = "interval"
SCHEDULER_TIMEZONE = "Asia/Seoul"

db = SqlAlchemyDB()


def main() -> None:
    try:
        containers_metrics = get_containers_status()
        for container_metric in containers_metrics:
            add_metric_to_database(db, *get_metrics_from_docker(container_metric))

    except (KeyError, NotFound) as err:
        print(f"Server cannot save metrics: {err}")


if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone=SCHEDULER_TIMEZONE)
    scheduler.add_job(main, SCHEDULER_TRIGGER, seconds=SCHEDULER_TIME, id=SCHEDULER_ID)
    scheduler.start()
