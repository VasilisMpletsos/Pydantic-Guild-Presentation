import os

from fastapi import APIRouter, HTTPException, Depends
from utils.type import ImageRequest, MultiSearchQueryResponse
from openai import AzureOpenAI, AsyncAzureOpenAI

extract_router = APIRouter(
    prefix='/extract_products',
    tags=['extract products'],
    dependencies=None
)

client = AsyncAzureOpenAI(
    api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
    api_version=os.environ.get("OPENAI_API_VERSION"),
    azure_endpoint=os.environ.get("OPENAI_API_BASE"),
    timeout=10.0,
    max_retries=10
)


@extract_router.post("/api/extract_products", response_model=MultiSearchQueryResponse)
async def extract_products(image_request: ImageRequest):
    completion = await client.chat.completions.create(
        model="gpt-4-vision-preview",
        max_tokens=image_request.max_tokens,
        temperature=image_request.temperature,
        stop=["```"],
        messages=[
            {
                "role": "system",
                "content": f"""
                You are an expert system designed to extract products from images for 
                an ecommerce application. Please provide the product name and a 
                descriptive query to search for the product. Accurately identify every 
                product in an image and provide a descriptive query to search for the 
                product. You just return a correctly formatted JSON object with the 
                product name and query for each product in the image and follows the 
                schema below:

                JSON Schema:
                {MultiSearchQueryResponse.model_json_schema()}""",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """Extract the products from the image, 
                        and describe them in a query in JSON format""",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": image_request.url},
                    },
                ],
            },
            {
                "role": "assistant",
                "content": "```json",
            },
        ],
    )
    return MultiSearchQueryResponse.model_validate_json(completion.choices[0].message.content)
