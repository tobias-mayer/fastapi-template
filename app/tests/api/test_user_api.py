from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.db import operations
from app.schemas.user import UserCreate


def test_create_user_new_email(
    db: Session, client: TestClient
) -> None:
    email = 'create_user_new_mail@test.de'
    password = 'asdf123'
    payload = {"email": email, "password": password}

    response = client.post(
        '/users/', json=payload,
    )

    assert 200 <= response.status_code < 300
    created_user = response.json()
    user = operations.user_operations.get_by_email(db, email=email)
    assert user
    assert user.email == created_user['email']


def test_create_user_already_exists(
    db: Session, client: TestClient
) -> None:
    email = 'already_exists@gmail.com'
    password = 'asdf123'
    user_in = UserCreate(email=email, password=password)
    operations.user_operations.create(db, obj_in=user_in)
    payload = {"email": email, "password": password}

    response = client.post(
        '/users/', json=payload,
    )

    created_user = response.json()
    assert response.status_code == 400
    
