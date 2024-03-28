from typing import Dict, Union, Any, List
from pydantic import BaseModel, Field, ConfigDict

OptionDict = Dict[str, Union[str, int]]


class HealthStatus(BaseModel):
    status: str = "UP"


class ServerInfo(BaseModel):
    worker_class: str
    workers: int
    bind: int
    timeout: int


class SearchQuery(BaseModel):
    product_name: str
    query: str = Field(..., description="""A descriptive query to search for the product, include 
                            adjectives, and the product type. will be used to serve relevant 
                            products to the user.""")


class MultiSearchQueryResponse(BaseModel):
    products: List[SearchQuery]

    model_config = ConfigDict(
      json_schema_extra={
            "examples": [
                {
                    "products": [
                        {
                            "product_name": "Nike Air Max",
                            "query": "black running shoes",
                        },
                        {
                            "product_name": "Apple iPhone 13",
                            "query": "smartphone with best camera",
                        },
                    ]
                }
            ]
        }
    )


class ImageRequest(BaseModel):
    url: str
    temperature: float = 0.0
    max_tokens: int = 1800

    model_config = ConfigDict(
      json_schema_extra={
            "examples": [
                {
                    "url": "https://mensfashionpostingcom.files.wordpress.com/2020/03/fbe79-img_5052.jpg?w=768",
                    "temperature": 0.0,
                    "max_tokens": 1800,
                }
            ]
        }
    )
