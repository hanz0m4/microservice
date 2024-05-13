from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, database, models, schemas

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для создания студента
@router.post("/students/")
async def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

# Эндпоинт для создания группы
@router.post("/groups/")
async def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)


# Эндпоинт для получения информации о студенте по его id
@router.get("/students/{student_id}")
async def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db=db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return student


# Эндпоинт для получения информации о группе по ее id
@router.get("/groups/{group_id}")
async def read_group(group_id: int, db: Session = Depends(get_db)):
    group = crud.get_group(db=db, group_id=group_id)
    if group is None:
        raise HTTPException(status_code=404, detail="Группа не найдена")
    return group


# Эндпоинт для удаления студента
@router.delete("/students/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db=db, student_id=student_id)


# Эндпоинт для удаления группы
@router.delete("/groups/{group_id}")
async def delete_group(group_id: int, db: Session = Depends(get_db)):
    return crud.delete_group(db=db, group_id=group_id)



# Эндпоинт для получения списка студентов
@router.get("/students/", response_model=List[schemas.Student])
async def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students


# Эндпоинт для получения списка групп
@router.get("/groups/", response_model=List[schemas.Group])
async def get_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    groups = db.query(models.Group).offset(skip).limit(limit).all()
    return groups


# Эндпоинт для добавления стдента в группу
@router.put("/students/{student_id}/add-to-group/{group_id}/")
async def add_student_to_group(student_id: int, group_id: int, db: Session = Depends(get_db)):
    return crud.add_student_to_group(db=db, student_id=student_id, group_id=group_id)


# Эндпоинт для удаления студента из группы
@router.put("/students/{student_id}/remove-from-group/")
async def remove_student_from_group(student_id: int, db: Session = Depends(get_db)):
    return crud.remove_student_from_group(db=db, student_id=student_id)


# Эндпоинт для получения всех студентов в группе
@router.get("/groups/{group_id}/students/", response_model=List[schemas.Student])
async def get_students_in_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Группа не найдена")
    return group.students


# Эндпоинт для перевода студента из группы A в группу B
@router.put("/students/{student_id}/move-to-group/{new_group_id}/")
async def move_student_to_group(student_id: int, new_group_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")

    new_group = db.query(models.Group).filter(models.Group.id == new_group_id).first()
    if not new_group:
        raise HTTPException(status_code=404, detail="Новая группа не найдена")

    student.group_id = new_group_id
    db.commit()
    return {"message": "Студент успешно переведен в новую группу"}