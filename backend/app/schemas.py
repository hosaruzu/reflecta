from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class JournalEntryBase(BaseModel):
    moodValence: int
    moodArousal: int
    note: Optional[str] = None
    tabs: Optional[List[str]] = []

class JournalEntryCreate(JournalEntryBase):
    pass

class JournalEntry(JournalEntryBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

class HabitBase(BaseModel):
    name: str
    color: str = "blue"
    icon: str = "circle"

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: int
    isArchived: bool

    class Config:
        orm_mode = True

class HabitLogBase(BaseModel):
    habitId: int
    value: bool = True

class HabitLogCreate(HabitLogBase):
    pass

class HabitLog(HabitLogBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True