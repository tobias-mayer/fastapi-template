from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from app.core.config import app_settings
from app.api import login, users
from app.db.init_db import init_db
from app.db.session import SessionLocal

db = SessionLocal()
init_db(db)

app = FastAPI(
    title=app_settings.PROJECT_NAME
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter()
api_router.include_router(login.router, tags=['login'])
api_router.include_router(users.router, prefix='/users', tags=['users'])

app.include_router(api_router)
