from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from configs import settings

cors = Middleware(CORSMiddleware,
                  allow_origins=settings.cors.origins,
                  allow_credentials=settings.cors.allow_credentials,
                  allow_methods=settings.cors.allow_methods,
                  allow_headers=settings.cors.allow_headers,
                  max_age=settings.cors.max_age)
