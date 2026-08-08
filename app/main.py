from fastapi import FastAPI

import app.routers as routers

VERSION = 'ALPHA'

app = FastAPI(version=VERSION)

app.include_router(routers.router)

