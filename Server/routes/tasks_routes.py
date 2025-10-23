from fastapi import APIRouter
from controllers.tasks import *
from schema.tasks_shemas import taskSchema, UpdateTaskSchema
from DataBase.connect import engine , session , ConnectDB

taskRouter = APIRouter()



## Route to get all  the tasks
@taskRouter.get('/')
def get_task(db: Session = Depends(ConnectDB)):
    return getAllTasks(db=db)

## Route to create  the tasks
@taskRouter.post('/')
def create_task( task : taskSchema,db: Session = Depends(ConnectDB)):
    return createTask(task, db)


## Route to get update single task
@taskRouter.put('/{id}')
def update_task(task: UpdateTaskSchema ,id:int,db: Session = Depends(ConnectDB) ):
    return updateTaskId(task,id,db)

## Route to get single task
@taskRouter.get('/{id}')
def get_single_task(id : int,db: Session = Depends(ConnectDB) ):
    return getTaskById(id,db)

## Route to delete the single task
@taskRouter.delete('/{id}')
def delete_task(id : int , db: Session = Depends(ConnectDB) ):
    return deleteTaskById(id,db)


## Route to update the status of the task
@taskRouter.get('/toggle/{id}')
def delete_task(id : int , db: Session = Depends(ConnectDB) ):
    return toggleIsDoneFlag(id,db)
