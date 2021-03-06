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