from pydantic import BaseModel
from typing import List


class StudentBase(BaseModel):
    name: str


class StudentCreate(StudentBase):
    group_id: int


class Student(StudentBase):
    id: int
    group_id: int

    class Config:
        orm_mode = True


class GroupBase(BaseModel):
    name: str


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    students: List[Student] = []

    class Config:
        orm_mode = True
