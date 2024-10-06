from pydantic import BaseModel


class SUserLogin(BaseModel):
    username: str
    password: str
