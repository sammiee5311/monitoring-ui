from fastapi import APIRouter
from utils import get_grafana_servers
from db.sql_alchemy import SqlAlchemyDB

router = APIRouter(
    prefix="/grafana",
    tags=["grafana"],
)

db = SqlAlchemyDB()


@router.get("/")
async def grafana_panels(server: str):
    servers = get_grafana_servers(db)
    if server not in servers:
        return {"error": f"{server} does not contain in grafana servers."}
    return {"grafanaPanels": [servers[server]]}
