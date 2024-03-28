from fastapi import APIRouter
from configs import settings
from utils.type import HealthStatus


router = APIRouter(
    prefix=settings.endpoints.prefix,
    tags=["health"],
    dependencies=None
)


@router.get('/' + settings.endpoints.health, response_model=HealthStatus,
            description=None, summary="Get server health status")
async def health_check():
    return HealthStatus()
