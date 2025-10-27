from fastapi import APIRouter
from controllers.tasks import *
from schema.tasks_shemas import taskSchema, UpdateTaskSchema
from DataBase.connect import engine , session , ConnectDB
from Middleware.auth_middleware import verify_jwt

taskRouter = APIRouter()



## Route to get all  the tasks
@taskRouter.get('/')
def get_task(db: Session = Depends(ConnectDB) , current_user = Depends(verify_jwt)):
    return getAllTasks(db,current_user)

## Route to create  the tasks
@taskRouter.post('/')
def create_task( task : taskSchema,db: Session = Depends(ConnectDB),current_user = Depends(verify_jwt)):
    return createTask(task, db,current_user)


## Route to get update single task
@taskRouter.put('/{id}')
def update_task(task: UpdateTaskSchema ,id:int,db: Session = Depends(ConnectDB) ,current_user = Depends(verify_jwt)):
    return updateTaskId(task,id,db,current_user)

## Route to get single task
@taskRouter.get('/{id}')
def get_single_task(id : int,db: Session = Depends(ConnectDB) ,current_user = Depends(verify_jwt)):
    return getTaskById(id,db,current_user)

## Route to delete the single task
@taskRouter.delete('/{id}')
def delete_task(id : int , db: Session = Depends(ConnectDB) ,current_user = Depends(verify_jwt)):
    return deleteTaskById(id,db,current_user)


## Route to update the status of the task
@taskRouter.get('/toggle/{id}')
def delete_task(id : int , db: Session = Depends(ConnectDB) ,current_user = Depends(verify_jwt) ):
    return toggleIsDoneFlag(id,db,current_user)
