from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr

app = FastAPI()


class SatorianUser(BaseModel):
    age: int = Field(
        title="User Age", description="Age of the user", examples=[25, 30, 35, 40]
    )

    email: EmailStr = Field(
        title="Email",
        description="Give here the email of the user",
        examples=["nick.korakas@satoryanalytics.com"],
    )

    name: str = Field(
        title="Username of the user",
        description="The name of the user must be provided here",
        examples=["Nikos Korakas"],
    )

    password: SecretStr = Field(
        title="Password",
        description="Password of the user",
        examples=["123456", "password", "admin123"],
        json_schema_extra={"password_strength": "test"},
    )

    coding_languages: List[str] = Field(
        title="Coding Languages",
        description="List of coding languages",
        examples=[["Python", "React", "C", "C++", "PowerBI"]],
    )


@app.get("/")
def read_root():
    return {"Hello Welcome to the FastAPI"}


@app.post("/add_satorian_user")
def add_satorian_user(user: SatorianUser):
    return {"created_user": user.dict()}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
