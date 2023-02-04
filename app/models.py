from sqlalchemy import Column, Integer, String

from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    age = Column(Integer)
    city = Column(String)
    portrait = Column(String)