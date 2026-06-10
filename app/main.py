from fastapi import FastAPI
from app.api.routes.system import router as system_router
from app.models.user import User
from app.database.db import engine, Base
from app.api.routes.user import router as user_router

app = FastAPI()

app.include_router(system_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)

