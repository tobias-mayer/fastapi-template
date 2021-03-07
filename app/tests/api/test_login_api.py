from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.db import operations
from app.schemas.user import UserCreate


def test_login_successful(
    db: Session, client: TestClient
) -> None:
    email = 'login_successful@gmail.com'
    password = 'asdf123'
    user_in = UserCreate(email=email, password=password)
    operations.user_operations.create(db, obj_in=user_in)

    payload = {"username": email, "password": password}
    response = client.post('/login/', data=payload)
    token = response.json()
    assert response.status_code == 200
    assert 'access_token' in token
    assert token['access_token']


def test_login_user_not_existent(
    db: Session, client: TestClient
) -> None:
    email = 'i_dont_exist@gmail.com'
    password = 'asdf123'

    payload = {"username": email, "password": password}
    response = client.post('/login/', data=payload)
    assert response.status_code == 400
