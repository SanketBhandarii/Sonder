from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from db.base import Base

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)

    session_id = Column(Integer, ForeignKey("chat_sessions.id"))

    sender_role = Column(String)
    # student | counsellor | ai

    message = Column(String)

    created_at = Column(DateTime, server_default=func.now())
