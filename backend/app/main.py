from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.routers as routers

VERSION = 'ALPHA'

app = FastAPI(version=VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(routers.router)

