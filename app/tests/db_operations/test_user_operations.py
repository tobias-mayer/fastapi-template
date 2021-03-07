from sqlalchemy.orm import Session

from app.db import operations
from app.schemas.user import UserCreate


def test_create_user(db: Session) -> None:
    email = 'test@gmail.com'
    password = 'test1234'
    user_in = UserCreate(email=email, password=password)
    user = operations.user_operations.create(db, obj_in=user_in)
    assert user.email == email
    assert hasattr(user, 'hashed_password')


def test_authenticate_user(db: Session) -> None:
    email = 'test1@gmail.com'
    password = 'test1234'
    user_in = UserCreate(email=email, password=password)
    user = operations.user_operations.create(db, obj_in=user_in)
    authenticated_user = operations.user_operations.authenticate(db, email=email, password=password)
    assert authenticated_user
    assert user.email == authenticated_user.email


def test_get_by_email(db: Session) -> None:
    email = 'get_by_email@gmail.com'
    password = 'test1234'
    user_in = UserCreate(email=email, password=password)
    user = operations.user_operations.create(db, obj_in=user_in)
    search_result = operations.user_operations.get_by_email(db, email=email)
    assert user.id == search_result.id
    assert user.email == search_result.email
    assert user.is_active == search_result.is_active


def test_is_active(db: Session) -> None:
    email = 'is_active@gmail.com'
    password = 'test1234'
    user_in = UserCreate(email=email, password=password)
    user = operations.user_operations.create(db, obj_in=user_in)
    assert operations.user_operations.is_active(user)
