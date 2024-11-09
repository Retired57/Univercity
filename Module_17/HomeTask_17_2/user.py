from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.backend.db import Base
from app.models import *


# from HomeTask_17_2.app.backend.db import Base             # это для моей структуры
# from HomeTask_17_2.app.models import *                    # это для моей структуры


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"keep_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True)

    tasks = relationship("Task", back_populates="user")


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
