from DataBase.connect import engine , session , ConnectDB
from models.tasks_model import TaskModel
import models
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.responses import JSONResponse
from schema.tasks_shemas import taskSchema, UpdateTaskSchema
models.tasks_model.Base.metadata.create_all(engine)



def createTask( task : taskSchema , db: Session = Depends(ConnectDB) ):
    

    if (db.query(TaskModel).filter(TaskModel.id == task.id).first()): 
         return JSONResponse(
            content={'message':" Task with this id already exists"},
            status_code=200
        )
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
        
        return JSONResponse(
                content={'message':" task created successfully!",'Tasks':jsonable_encoder(new_task)},
                status_code=200
            )
    
    

def getAllTasks(db:Session = Depends(ConnectDB)):
    tasks = db.query(TaskModel).all()
    if len(tasks) != 0 :
        return JSONResponse(
            content={'message':"All tasks retured successfully!",'Tasks': jsonable_encoder(tasks)},
            status_code=200
        )
    return JSONResponse(
            content={'message':"No Taks Found!"},
            status_code=204
    )


def getTaskById(id: int, db: Session = Depends(ConnectDB)):
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    
    if task:
        return {
            "message": "Task Found Successfully!",
            "task": jsonable_encoder(task) 
        }
    else:
        return JSONResponse(
            content={"message": "No Task Found!"},
            status_code=404  #
        )



def deleteTaskById(id:int,db: Session = Depends(ConnectDB)):
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    
    if task:
        db.delete(task)
        db.commit()
        return {
            "message": "Task deleted Successfully!",
        }
    else:
        return JSONResponse(
            content={"message": "No Task Found!"},
            status_code=404  
        )


def updateTaskId(updated_task : UpdateTaskSchema , id:int ,db: Session = Depends(ConnectDB)):

    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if task:
        update_data = updated_task.model_dump(exclude_unset=True)
        for key , value in update_data.items():
            setattr(task, key , value)
        db.commit()
        db.refresh(task)

        


        return {
            "message": "Task updated Successfully!",
            'Task':jsonable_encoder(task)
        }
    else:
        return JSONResponse(
            content={"message": "No Task Found!"},
            status_code=404  #
        )
    


def toggleIsDoneFlag(id: int, db: Session = Depends(ConnectDB)):
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    
    if task:
        task.isDone = not task.isDone  
        db.commit()                    
        db.refresh(task)               # 

        return {
            "message": "Task status updated successfully!",
            "task": jsonable_encoder(task) 
        }
    else:
        return JSONResponse(
            content={"message": "No Task Found!"},
            status_code=404
        )
        