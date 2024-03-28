from typing import Optional
from fastapi import FastAPI
from routers import health, about, extract_products
from utils.logger import logger
from middleware import middlewares
from configs import settings


class APIProvider:
    def __init__(self,
                 title: Optional[str] = 'API',
                 openapi_url: Optional[str] = '/openapi.json',
                 version: Optional[str] = "0.0.1",
                 docs_url: Optional[str] = "/docs",
                 debug: bool = False
                 ) -> None:
        self.api = FastAPI(middleware=middlewares, title=title, openapi_url=openapi_url, docs_url=docs_url,
                           version=version, debug=debug)
        self.configure_routes()
        self.logger = logger.bind(classname=self.__class__.__name__)
        self.logger.debug('API configured')

    def configure_routes(self):
        self.api.include_router(health.router)
        self.api.include_router(about.router)
        self.api.include_router(extract_products.extract_router)

    def get_api(self) -> FastAPI:
        return self.api
