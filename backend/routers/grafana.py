from fastapi import APIRouter
from utils import get_grafana_servers

router = APIRouter(
    prefix="/grafana",
    tags=["grafana"],
)


@router.get("/")
async def grafana_panels(server: str):
    servers = get_grafana_servers()
    if server not in servers:
        return {"error": f"{server} does not contain in grafana servers."}
    return {"grafanaPanels": [servers[server]]}
