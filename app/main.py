from fastapi import FastAPI
from app.api.routes.system import router as system_router
from app.models.user import User
from app.database.db import engine, Base


app = FastAPI()

app.include_router(system_router)

Base.metadata.create_all(bind=engine)