from fastapi import APIRouter
from controllers.tasks import *


taskRouter = APIRouter()



## Route to get all  the tasks
@taskRouter.get('/')
def get_task():
    return getAllTasks()

## Route to create  the tasks
@taskRouter.post('/')
def create_task():
    return createTask()


## Route to get update single task
@taskRouter.put('/{id}')
def update_task(id:int):
    return updateTaskId(id)

## Route to get single task
@taskRouter.get('/{id}')
def get_single_task(id : int):
    return getTaskById(id)

## Route to delete the single task
@taskRouter.delete('/{id}')
def get_task():
    return deleteTaskById(id)
