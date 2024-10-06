from pydantic import BaseModel

class SUser(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    type_document: str
    nro_document: str
    email: str
    age: int
    phone_number: str
    address: str
    gender: str
    url_photo: str
    