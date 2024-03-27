from pydantic import BaseModel
from typing import List


class ModelInference(BaseModel):
    system_prompt: str
    user_prompt: str


class UserInput(BaseModel):
    name: str
    age: int
    favourite_drink: str = "Aperol Spritz"
