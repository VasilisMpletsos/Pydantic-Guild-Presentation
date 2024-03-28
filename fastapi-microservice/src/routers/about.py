from fastapi import APIRouter
from configs import settings
from utils.type import ServerInfo


router = APIRouter(
    prefix=settings.endpoints.prefix,
    tags=["about"],
    dependencies=None
)


@router.get('/' + settings.endpoints.info, response_model=ServerInfo,
            description=None, summary="Get server information")
async def info():
    return ServerInfo(worker_class=settings.server.worker_class,
                      workers=settings.server.workers,
                      bind=settings.server.bind,
                      timeout=settings.server.timeout)
