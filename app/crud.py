from sqlalchemy.orm import Session
from app import models
from app import schemas
from fastapi import HTTPException


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_group(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()



def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return {"message": "Студент успешно удален"}
    else:
        return {"error": "Студент не найден"}


def delete_group(db: Session, group_id: int):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if group:
        db.delete(group)
        db.commit()
        return {"message": "Группа успешно удалена"}
    else:
        return {"error": "Группа не найдена"}



def add_student_to_group(db: Session, student_id: int, group_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    group = db.query(models.Group).filter(models.Group.id == group_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    if not group:
        raise HTTPException(status_code=404, detail="Группа не найдена")

    student.group_id = group_id
    db.commit()
    return {"message": "Студент успешно добавлен в группу"}


def remove_student_from_group(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")

    student.group_id = None
    db.commit()
    return {"message": "Студент успешно удален из группы"}

