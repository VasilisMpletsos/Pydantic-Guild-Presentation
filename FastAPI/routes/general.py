from models import UserInput
from fastapi import APIRouter

router = APIRouter(prefix="/intro", tags=["Introduction"])


@router.post("/user_query")
async def user_query(input: UserInput):
    return f"Hello {input.name}, you are {input.age} years old and your favourite drink is {input.favourite_drink}"
