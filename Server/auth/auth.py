import os
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta



SECRETE_KEY = '178e2620318ca8706b206ed747ab440de8857aa69cb30bcabdf7cf169bf4eb20'
ALGORITHM = 'HS256'


pwd_contetx = CryptContext(schemes=['bcrypt'],deprecated='auto')



def hash_password(plain_password : str )-> str:
    return pwd_contetx.hash(plain_password)




def verifyPassword(user_pass : str , hashed_password:str)-> bool:
    return pwd_contetx.verify(user_pass,hashed_password)


def decodeToken(  token : str ):
    try:
        payload = jwt.decode(token,SECRETE_KEY,algorithms=[ALGORITHM],)
        return payload
    except JWTError:
        return JWTError
    


def create_access_token(data : dict):
    paylod = data.copy()
    return jwt.encode(paylod,SECRETE_KEY,ALGORITHM)
