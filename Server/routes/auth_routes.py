from fastapi import APIRouter
from controllers.auth_controllers import * 
from schema.users_schemas import SingInSchema ,SinUpSchema
from DataBase.connect import ConnectDB
from fastapi.responses import Response

authRouter = APIRouter()


@authRouter.post('/login')
async def login(response : Response ,user : SingInSchema , db:Session = Depends(ConnectDB)):
    return login_user(response,user,db)


@authRouter.post('/signup')
async def signup(user : SinUpSchema , db : Session = Depends(ConnectDB)):
    return signup_user(user,db)

