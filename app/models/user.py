from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(512), nullable=False)
    last_name = Column(String(512), nullable=False)
    deleted = Column(Boolean, default=False)
