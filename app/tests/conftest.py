from typing import Dict, Generator
import os

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.api import deps
from app.models.base_model import BaseModel

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


BaseModel.metadata.create_all(bind=engine)


@pytest.fixture(scope='session')
def db() -> Generator:
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        os.remove('./test.db')


@pytest.fixture(scope='module')
def client() -> Generator:

    def _get_db_override() -> Generator:
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()
    app.dependency_overrides[deps.get_db] = _get_db_override

    with TestClient(app) as c:
        yield c