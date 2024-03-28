import logging
from loguru import logger
import sys
from configs import settings


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # find caller from where originated the logged message
        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


cfg = settings.logging
logger.remove()  # remove initial loguru logger to add one with custom configs

# Add gunicorn and uvicorn logs to loguru loggers,
# adapted from https://pawamoy.github.io/posts/unify-logging-for-a-gunicorn-uvicorn-app/
intercept_handler = InterceptHandler()  # Create a handler to redirect specific logs to loguru logger
if 'loggers_to_loguru' in cfg:
    if cfg['loggers_to_loguru'] is not None:
        for logger_name in cfg['loggers_to_loguru']:
            logging.getLogger(logger_name).handlers = [intercept_handler]  # redirect logs from python logger to loguru
logger.configure(extra={"classname": "None"})
logger.add(sys.stderr, format=cfg['format'], filter=None, level=cfg['level'], backtrace=True, diagnose=True)
