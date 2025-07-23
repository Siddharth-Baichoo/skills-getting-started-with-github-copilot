from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    schedule = Column(String)
    max_participants = Column(Integer)
    participants = relationship("Participant", back_populates="activity")

class Participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"))
    activity = relationship("Activity", back_populates="participants")