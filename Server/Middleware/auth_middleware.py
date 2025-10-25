# dependencies/auth.py
from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError
from auth.auth import decodeToken


def verify_jwt(request: Request):
    token = request.cookies.get("accessToken")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    try:
        payload = decodeToken(token)
        return payload  
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
