from fastapi import APIRouter

router = APIRouter(
    prefix="/grafana",
    tags=["grafana"],
)


@router.get("/")
async def grafana_panels():
    return {
        "grafanaPanels": [
            {
                "id": "server1",
                "url": "http://localhost:3030/d-solo/OnfS5Lqnz/init?orgId=1&from=1656486968140&to=1656508568140&panelId=2",
            }
        ]
    }
