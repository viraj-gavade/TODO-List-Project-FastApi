from fastapi import FastAPI
from routes.tasks_routes import taskRouter
from fastapi.middleware.cors import CORSMiddleware
from  routes.auth_routes import authRouter
import models
from DataBase.connect import engine

models.tasks_model.Base.metadata.create_all(engine)
app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers
app.include_router(taskRouter, prefix='/tasks', tags=['tasks'])
app.include_router(authRouter ,  prefix='/auth' , tags=['auth'])
