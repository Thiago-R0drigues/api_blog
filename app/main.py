from fastapi import FastAPI


from database import get_db
import schemas
import models
import routers

VERSION = 'ALPHA'

app = FastAPI(version=VERSION)

app.include_router(routers.router)

