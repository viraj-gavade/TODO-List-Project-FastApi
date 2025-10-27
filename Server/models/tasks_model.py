from sqlalchemy import Column, Integer, String, Date, Boolean, func , ForeignKey 
from sqlalchemy.orm import relationship
from DataBase.connect import Base

class TaskModel(Base):
    __tablename__ = "tasks" 

    id = Column(Integer, primary_key=True, index=True, autoincrement=True,unique=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    isDone = Column(Boolean, default=False)
    date = Column(Date, default=func.current_date())
    createdBy = Column(Integer,ForeignKey('Users.id'),nullable=True)

    owner = relationship('UserModel',back_populates='tasks')


    class Config:
        orm_mode = True



class UserModel(Base):
    __tablename__ = 'Users'
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    username =  Column(String,unique=True)
    password = Column(String)
    email = Column(String,unique=True)
    tasks = relationship('TaskModel',back_populates='owner')
    class Config:
        orm_mode = True

    