from sqlalchemy import Column, Integer, String
from db.database import Base


class Data(Base):
    __tablename__ = "data"
    name = Column(String(512), nullable=False)
    age = Column(String(512), primary_key=True, nullable=False)
    tall = Column(String(512), nullable=False)
