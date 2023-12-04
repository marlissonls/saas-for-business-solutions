from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from app.config import engine

class Base(DeclarativeBase):
    pass

class UserSchema(Base):

    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String(30))
    email = Column(String)
    password = Column(String)
    profile_image = Column(String)


Base.metadata.create_all(engine)
