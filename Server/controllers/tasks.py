from DataBase.connect import engine , session , ConnectDB
from models.tasks_model import TaskModel
import models
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.responses import JSONResponse
from schema.tasks_shemas import taskSchema, UpdateTaskSchema
models.tasks_model.Base.metadata.create_all(engine)
from utils.exception import * 
from utils.response import CustomResponse

## Fucntion to create a Task 
def createTask( task : taskSchema , db: Session = Depends(ConnectDB) ):
    '''
    This function creates a task in tha database.
    '''
    if (db.query(TaskModel).filter(TaskModel.id == task.id).first()): 
          return TaskAlreadyExists(name=f'Id : {task.id}')
    else:
        new_task =  new_task = TaskModel(
        name=task.name,
        description=task.description,
        isDone=task.isDone,
        date=task.date
    )
        
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        
        return CustomResponse.success(
            message="Task created successfully!",
            data=jsonable_encoder(new_task)
        )   
    
    
    
## Fucntion to get all the tasks from the database
def getAllTasks(db:Session = Depends(ConnectDB)):
    
    '''
    This function fetches all the tasks from the database.
    '''
    tasks = db.query(TaskModel).all()
    if tasks :
         return CustomResponse.success(
           message='All Tasks Fetched Successfully!',
           data= jsonable_encoder(tasks)
       )
    else:
        return TaskNotFound(name = f'No Tasks')


def getTaskById(id: int, db: Session = Depends(ConnectDB)):
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if task:
        return CustomResponse.success(
           message='Task Fetched Successfully!',
           data= jsonable_encoder(task)
       )
    else:
        return TaskNotFound(name=f'id : {id}')



def deleteTaskById(id:int,db: Session = Depends(ConnectDB)):
    
    '''
    This function Fetches a single task by the given id 
    '''
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    
    if task:
        db.delete(task)
        db.commit()
        return CustomResponse.success(
           message='Task Deleted  Successfully!',
           data= jsonable_encoder(task)
       )
    else:
         return TaskNotFound(name=f'id : {id}')


def updateTaskId(updated_task : UpdateTaskSchema , id:int ,db: Session = Depends(ConnectDB)):
    '''
    This function updates the task with the help of given id 
    '''
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if task:
        update_data = updated_task.model_dump(exclude_unset=True)
        for key , value in update_data.items():
            setattr(task, key , value)
        db.commit()
        db.refresh(task)
        return CustomResponse.success(
           message='Task updated Successfully!',
           data= jsonable_encoder(task)
       )
    else:
        return TaskNotFound(name=f'id : {id}')
    


def toggleIsDoneFlag(id: int, db: Session = Depends(ConnectDB)):
    '''
    This function  toggles the status of the task from done to
    undone and vice versa
    '''
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    
    if task:
        task.isDone = not task.isDone  
        db.commit()                    
        db.refresh(task)               # 

        return CustomResponse.success(
           message='Task Status changed Successfully!',
           data= jsonable_encoder(task)
       )
    else:
         return TaskNotFound(name=f'id : {id}')
        