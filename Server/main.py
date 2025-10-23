from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from routes.tasks_routes import taskRouter


app = FastAPI()


app.include_router(taskRouter,prefix='/tasks',tags=['tasks'])

