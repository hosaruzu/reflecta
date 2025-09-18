from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class JournalEntry(Base):
    __tablename__ = 'journal_entries'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow())
    moodValence = Column(Integer)
    moodArousal = Column(Integer)
    notes = Column(String, nullable=True)
    tags = Column(String, nullable=True)

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    color = Column(String, default="blue")
    icon = Column(String, default="circle")
    isArchived = Column(Boolean, default=False)

class HabitLog(Base):
    __tablename__ = 'habit_logs'

    id = Column(Integer, primary_key=True, index=True)
    habitId = Column(Integer, ForeignKey('habits.id'))
    date = Column(DateTime, default=datetime.utcnow())
    value = Column(Boolean, default=True)