from fastapi import FastAPI


from app.database import get_db
import app.routers as routers

VERSION = 'ALPHA'

app = FastAPI(version=VERSION)

app.include_router(routers.router)

