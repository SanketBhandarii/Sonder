from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from db.base import Base

class ScheduleRequest(Base):
    __tablename__ = "schedule_requests"

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("users.id"))
    counsellor_id = Column(Integer, ForeignKey("users.id"))

    scheduled_time = Column(DateTime)

    status = Column(String, default="pending")
    # pending | accepted | rejected

    created_at = Column(DateTime, server_default=func.now())
