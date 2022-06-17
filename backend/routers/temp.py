from fastapi import APIRouter

router = APIRouter(
    prefix="/temp",
    tags=["temp"],
)


@router.get("/")
async def temp():
    return {"message": "temp"}
