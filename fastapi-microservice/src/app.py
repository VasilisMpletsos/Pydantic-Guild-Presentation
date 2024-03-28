from api import APIProvider

import multiprocessing
from utils.type import OptionDict
from configs import settings
import uvicorn

api = APIProvider(title=settings.api_spec.name, openapi_url=settings.api_spec.openapi_url,
                  docs_url=settings.api_spec.docs_url,
                  version=settings.api_spec.version,
                  debug=settings.debug
                  ).get_api()


def __build_options() -> OptionDict:
    _workers = settings.server.workers

    if type(_workers) is str:
        if str(_workers).lower() == 'auto':
            _workers = multiprocessing.cpu_count() * 2 + 1
        else:
            _workers = 4
    else:
        _workers = int(_workers)

    return {
        "host": settings.server.host,
        "workers": _workers,
        "bind": settings.server.bind,
        "graceful_timeout": settings.server.graceful_timeout,
        "timeout": settings.server.timeout,
        'loglevel': settings.logging.level
    }


if __name__ == "__main__":
    config = __build_options()
    uvicorn.run(app='app:api', host=config['host'], port=config['bind'],
                workers=config['workers'], log_level=config['loglevel'],
                timeout_keep_alive=config['timeout'], timeout_graceful_shutdown=config['graceful_timeout'])
