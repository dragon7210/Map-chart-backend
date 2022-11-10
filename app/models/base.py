from sqlalchemy import Column, String, Integer, FLOAT, Numeric
from db.database import Base


class Base1(Base):
    __tablename__ = "base"
    __table_args__ = {'schema': 'per_user'}

    name = Column(String(512), primary_key=True, nullable=False)
    kkk = Column(Integer,  nullable=False)
    lll = Column(FLOAT, nullable=False)
