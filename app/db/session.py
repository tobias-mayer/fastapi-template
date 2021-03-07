from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import app_settings

engine = create_engine(app_settings.SQLALCHEMY_DB_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
