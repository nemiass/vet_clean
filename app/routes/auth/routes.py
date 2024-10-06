from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
import services
from app.core.security import verify_password
from app.core.auth import generate_access_token, generate_refresh_token


route = APIRouter()

@route.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = services.get_user_by_id(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="usuario o contraseña incorrectos")
    token = generate_refresh_token()
