from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get('/')
async def get_home():
    return 'This is the home page'