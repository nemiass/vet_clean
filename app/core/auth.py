import datetime

import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, HTTPException
from app.core.config import settings
from jwt.exceptions import InvalidTokenError


def generate_access_token(subject: dict, expires_delta: int = None):
    to_encode = subject.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire, "sub": str(subject), "iat": datetime.utcnow()})
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt


def generate_refresh_token(subject: dict, expires_delta: int = None):
    to_encode = subject.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire, "sub": str(subject), "iat": datetime.utcnow()})
    encoded_jwt = jwt.encode(
        to_encode, settings.refresh_secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt


def decodeJWT(token: str):
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        return payload
    except InvalidTokenError:
        return None


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            token = credentials.credentials
            if not self.verify_jwt(token):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return token

    def verify_jwt(self, token: str) -> bool:
        try:
            _ = decodeJWT(token)
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.JWTError:
            return False
