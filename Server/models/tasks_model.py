from sqlalchemy import Column, Integer, String, Date, Boolean, func
from DataBase.connect import Base

class TaskModel(Base):
    __tablename__ = "tasks" 

    id = Column(Integer, primary_key=True, index=True, autoincrement=True,unique=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    isDone = Column(Boolean, default=False)
    date = Column(Date, default=func.current_date())

    class Config:
        orm_mode = True


    