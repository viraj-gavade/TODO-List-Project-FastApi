
from schema.users_schemas import SingInSchema ,SinUpSchema
from DataBase.connect import ConnectDB
from fastapi import Depends ,status
from sqlalchemy.orm import Session
from models.tasks_model import UserModel
from auth.auth import * 
from utils.response import CustomResponse
from fastapi.responses import Response




def login_user(response : Response ,user : SingInSchema , db:Session = Depends(ConnectDB)):

    db_user  = db.query(UserModel).filter(UserModel.username == user.username).first()
    if db_user:
        isPassCorrect = verifyPassword(user.password , db_user.password)
        print('Is pass correct ' , isPassCorrect)
        if isPassCorrect != True:
            return CustomResponse.error(
                message='Invalid username and password provided',
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        payload : dict = {
        'id': db_user.id,
        'username':db_user.username,
        'email': db_user.email
    }
        accessToken = create_access_token(data=payload)
        response.set_cookie(
        key="accessToken",
        value=accessToken,
        httponly=True,
        samesite="lax"
    )


    response.status_code = status.HTTP_200_OK
    response.body = CustomResponse.success(
        message="Login Successful!",
        data=accessToken
    ).body  #   

    return response
        


def signup_user(user : SinUpSchema , db : Session = Depends(ConnectDB)):

    if (db.query(UserModel).filter(UserModel.username == user.username)).first():
        return CustomResponse.error(
            message='Username already taken !'
        )
    
    if (db.query(UserModel).filter(UserModel.email == user.email)).first():
        return CustomResponse.error(
            message='email already taken !'
        ) 

    db_user = UserModel(
        username = user.username,
        email = user.email,
        password =  hash_password(user.password),
    )
    public_user = {
        'username' : user.username,
        'email':user.email
    }
    db.add(db_user)
    db.commit()
    return CustomResponse.success(
        message='User created Successfully!',
        data=public_user
    )