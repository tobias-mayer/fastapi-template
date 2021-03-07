from typing import Any, Generic, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy.orm import Session

from app.models.base_model import BaseModel

ModelType = TypeVar('ModelType', bound=BaseModel)
CreateSchemaType = TypeVar('CreateSchemaType', bound=PydanticBaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=PydanticBaseModel)


class BaseOperations(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        json_data = jsonable_encoder(obj_in)
        db_obj = self.model(**json_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
