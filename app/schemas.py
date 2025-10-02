from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    email   : str
    password: str

class TokenSchema(BaseModel):
    name  : str
    token : str