from sqlalchemy import Column, Integer, ForeignKey, String
from db.base import Base

class CounsellorRating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("users.id"))
    counsellor_id = Column(Integer, ForeignKey("users.id"))

    rating = Column(Integer)  # 1 to 5
    review = Column(String, nullable=True)
