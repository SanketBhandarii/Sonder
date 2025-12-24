from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from db.base import Base

class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("users.id"))
    counsellor_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    chat_type = Column(String)  
    # "ai" | "counsellor"

    status = Column(String, default="pending")  
    # pending | active | closed

    created_at = Column(DateTime, server_default=func.now())
