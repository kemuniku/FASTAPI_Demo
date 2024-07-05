from sqlalchemy import Column, Integer, String, DateTime, Index,Float
from datetime import datetime
from settings import Base


class SubmissionModel(Base):
    __tablename__ = 'submissions'
    id = Column(Integer, primary_key=True)
    epoch_second = Column(Integer)
    problem_id = Column(String)
    contest_id = Column(String)
    user_id = Column(String)
    language = Column(String)
    point = Column(String)
    length = Column(Integer)
    result = Column(String)
    execution_time = Column(Integer)
    __table_args__ = (Index('user_id', 'problem_id', 'epoch_second'),) 