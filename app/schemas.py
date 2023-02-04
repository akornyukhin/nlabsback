from pydantic import BaseModel

class UserBase(BaseModel):
    firstName: str
    lastName: str
    age: int
    city: str
    portrait: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True