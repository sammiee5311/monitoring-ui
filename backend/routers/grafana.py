from fastapi import APIRouter, Depends, Response, status
from utils import get_grafana_servers
from typing import Callable

from db.sql_alchemy import SqlAlchemyDB

router = APIRouter(
    prefix="/grafana",
    tags=["grafana"],
)


def get_db() -> SqlAlchemyDB:
    db = SqlAlchemyDB()
    return db


@router.get("/")
async def grafana_panels(server: str, response: Response, db: Callable = Depends(get_db)):
    servers = get_grafana_servers(db)
    if server not in servers:
        response.status_code = status.HTTP_204_NO_CONTENT
        return {"error": f"{server} does not contain in grafana servers."}
    return {"grafanaPanels": [servers[server]]}
