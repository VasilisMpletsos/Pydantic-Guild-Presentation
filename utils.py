# Import requests from get and post methods
import requests

# Import pydantic base model to be expected as input
from pydantic import BaseModel


def request_user_intro(user: BaseModel):
    """
    This function sends a POST request to the API and expects as inputs the following json format:
    {
        'name': 'something',
        'age': something,
        'favourite_drink': 'something'
    }
    """

    # Send a POST request to the API
    response = requests.post(
        "http://127.0.0.1:8001/intro/user_query", json=user.model_dump()
    )

    # Print the response
    print(response.json())
