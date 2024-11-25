from fastapi import APIRouter

from ..models import User

router = APIRouter()


@router.get("/all/")
async def read_users() -> list[User]:
    return []
