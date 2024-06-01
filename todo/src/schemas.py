from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    completed: bool


class TodoInDBBase(TodoBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class TodoInDB(TodoInDBBase):
    completed: bool


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str

