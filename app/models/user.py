from sqlalchemy import Boolean, Column, Integer, String

from app.models.base_model import BaseModel

class User(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)