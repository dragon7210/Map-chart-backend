from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class New(Base):
    __tablename__ = "new"
    __table_args__ = {'schema': 'per_user'}

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    pak = Column(String, nullable=False)
