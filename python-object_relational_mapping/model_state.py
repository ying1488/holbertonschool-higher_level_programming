from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    __tablename__ = 'State'

    id = Column(Integer, primary_key=True)
    name = Column(String)
