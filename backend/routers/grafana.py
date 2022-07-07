from fastapi import APIRouter

router = APIRouter(
    prefix="/grafana",
    tags=["grafana"],
)

servers = {
    "server": {
        "url": "http://localhost:3030/d-solo/OnfS5Lqnz/init?orgId=1&from=1656486968140&to=1656508568140&panelId=2",
    }
}


@router.get("/")
async def grafana_panels(server: str):
    if server not in servers:
        return {"error": f"{server} does not contain in grafana servers."}
    return {"grafanaPanels": [servers[server]]}
