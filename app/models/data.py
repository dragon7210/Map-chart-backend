from sqlalchemy import Column, String, Integer, FLOAT, Numeric
from db.database import Base


class Data(Base):
    __tablename__ = "data"
    name = Column(String(512), primary_key=True, nullable=False)
    age = Column(Integer,  nullable=False)
    tall = Column(FLOAT, nullable=False)
    bigo = Column(Numeric, nullable=False)
