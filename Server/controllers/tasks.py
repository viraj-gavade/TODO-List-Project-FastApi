from DataBase.connect import engine , session , ConnectDB
from models.tasks_model import TaskModel
import models
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.responses import JSONResponse
from schema.tasks_shemas import taskSchema, UpdateTaskSchema
from utils.exception import * 
from utils.response import CustomResponse
from Middleware.auth_middleware import verify_jwt
from fastapi import HTTPException,status

## Fucntion to create a Task 
def createTask( task : taskSchema , db: Session = Depends(ConnectDB), current_user = Depends(verify_jwt) ):
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
        date=task.date,
        createdBy = current_user['id']
    )
        
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        
        return CustomResponse.success(
            message="Task created successfully!",
            data=jsonable_encoder(new_task)
        )   
    
    
    
## Fucntion to get all the tasks from the database
def getAllTasks(db:Session = Depends(ConnectDB), current_user = Depends(verify_jwt)):
    
    '''
    This function fetches all the tasks from the database.
    '''
    user_id = current_user["id"]
    print('UserId : ' , user_id)

    tasks = db.query(TaskModel).filter(TaskModel.createdBy == user_id).all()
    print('Task : ' , tasks)
    if tasks :
         return CustomResponse.success(
           message='All Tasks Fetched Successfully!',
           data= jsonable_encoder(tasks)
       )
    else:
        return TaskNotFound(name = f'No Tasks')


def getTaskById(id: int, db: Session = Depends(ConnectDB), current_user = Depends(verify_jwt)):
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if task:
        if task.createdBy != current_user["id"]:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to access this task"
        )
        return CustomResponse.success(
           message='Task Fetched Successfully!',
           data= jsonable_encoder(task)
       )
    else:
        return TaskNotFound(name=f'id : {id}')



def deleteTaskById(id:int,db: Session = Depends(ConnectDB), current_user = Depends(verify_jwt)):
    
    '''
    This function Fetches a single task by the given id 
    '''
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    
    if task:
        if task.createdBy != current_user["id"]:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to access this task"
        )

        db.delete(task)
        db.commit()
        return CustomResponse.success(
           message='Task Deleted  Successfully!',
           data= jsonable_encoder(task)
       )
    else:
         return TaskNotFound(name=f'id : {id}')


def updateTaskId(updated_task : UpdateTaskSchema , id:int ,db: Session = Depends(ConnectDB), current_user = Depends(verify_jwt)):
    '''
    This function updates the task with the help of given id 
    '''
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if task:
        if task.createdBy != current_user["id"]:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to access this task"
        )
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
    


def toggleIsDoneFlag(id: int, db: Session = Depends(ConnectDB), current_user = Depends(verify_jwt)):
    '''
    This function  toggles the status of the task from done to
    undone and vice versa
    '''
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    
    if task:
        if task.createdBy != current_user["id"]:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to access this task"
        )
        task.isDone = not task.isDone  
        db.commit()                    
        db.refresh(task)               # 

        return CustomResponse.success(
           message='Task Status changed Successfully!',
           data= jsonable_encoder(task)
       )
    else:
         return TaskNotFound(name=f'id : {id}')
        