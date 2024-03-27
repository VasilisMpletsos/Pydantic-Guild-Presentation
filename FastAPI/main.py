from typing import Union
from fastapi import FastAPI
from routes import models, general
import uvicorn

app = FastAPI()

app.include_router(general.router)
# app.include_router(models.router)

# Have to run the server using uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="info")
