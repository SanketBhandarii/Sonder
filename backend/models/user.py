from sqlalchemy import Column, Integer, String, Boolean, Float
from db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    role = Column(String, index=True)  # student | counsellor | admin

    phone = Column(String, nullable=True)
    experience = Column(Integer, nullable=True)
    certification = Column(String, nullable=True)
    rating = Column(Float, default=0.0)
    is_available = Column(Boolean, default=True)
