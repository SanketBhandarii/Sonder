from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from models.user import User
from models.chat_session import ChatSession
from models.chat_message import ChatMessage
from models.schedule_request import ScheduleRequest
from models.rating import CounsellorRating
