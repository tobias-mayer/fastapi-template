from sqlalchemy.orm import Session

from app.models.base_model import BaseModel
from app.db.session import engine

def init_db(db: Session) -> None:
    BaseModel.metadata.create_all(bind=engine)

