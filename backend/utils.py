from db.config import SqlAlchemyDB

db = SqlAlchemyDB()


def get_grafana_servers() -> dict[str, dict[str, str]]:
    servers = {}

    with db:
        metrics = db.metric.get()

        for metric in metrics:
            servers[metric.server_id[:12]] = {
                "url": "http://localhost:3030/d-solo/OnfS5Lqnz/init?orgId=1&from=1656486968140&to=1656508568140&panelId=2",
            }

    return servers
