from typing import Optional

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserUpdate(UserBase):
    pass

class UserInDbBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class User(UserInDbBase):
    pass

class UserInDb(UserInDbBase):
    hashed_password: str