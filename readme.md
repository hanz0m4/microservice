# Курсовой проект - приложение для управления задачами

В рамках курсовой работы необходимо разработать микросервисное бэкенд приложение на тему "приложение для управления задачами". Данная работа содержит два микросервиса: первый - сервис авторизации, аутенфикации и регистрацию; второй - микросервис управления задачами
Первый микросервис был развёрнут с помощью docker'а на 8000 порту, а второй - на 8001 порту.

#### Требования:
-	Приложение включает минимум 2 бэкенд сервиса
-	Каждый сервис должен запускаться в виде отдельного инстанса
-	Переменные окружения каждого сервиса вынесены в .env файле (в репозитории должен быть файл .env.example)
-	Коммуникация между сервиса может осуществляться через: Rest API, grpc, брокер сообщений 
-	База данных описана в docker-compose файле
-	БД в docker-compose для инициализации использует переменные из .env файла
-	В проекте есть файл requirements.txt со списком всех библиотек проекта
-	Каждый сервис содержит Readme файл с указанием задач сервиса, логики работы и инструкцию по запуску


## Сервис для регистрации, аутенфикации и авторизации пользователя

В сервисе auth производится процесс аутенфикации, регистрации и авторизации. Данные сохраняются в БД - PostgreSQL (auth_db). 
Микросервис был развёрнут на 8000 порту. Сервис содержит файлы:

-	src:
  
    - database.py - содержит настройки подключения к базе данных auth_db
    ```
    import os

    load_dotenv()

    AUTH_DATABASE_URL = os.getenv("AUTH_DATABASE_URL")

    engine = create_engine(AUTH_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()
    ```

    - dependencies.py - содержит данные о верификации, регистрации и т. д.

    ```
    from fastapi import APIRouter, Depends, HTTPException, status
    from sqlalchemy.orm import Session
    import models, schemas
    from database import SessionLocal
    from passlib.context import CryptContext
    from datetime import datetime, timedelta
    import jwt
    import os

    SECRET_KEY = os.getenv("JWT_SECRET")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    router = APIRouter()
    
    
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return pwd_context.hash(password)
    
    
    def create_access_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    @router.post("/register/", response_model=schemas.User)
    def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
        db_user = db.query(models.User).filter(models.User.username == user.username).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        hashed_password = get_password_hash(user.password)
        db_user = models.User(username=user.username, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    
    @router.post("/token/", response_model=schemas.Token)
    def login_for_access_token(form_data: schemas.UserCreate, db: Session = Depends(get_db)):
        user = db.query(models.User).filter(models.User.username == form_data.username).first()
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    
    ```
      
      - main.py - содержит основную точку входа в приложение
    
      ```
    from fastapi import FastAPI
    import models, dependencies
    from database import engine
    
    
    app = FastAPI()
    
    
    models.Base.metadata.create_all(bind=engine)
    app.include_router(dependencies.router)
    ```
    
      - models.py -  содержит описание моделей базы данных auth_db.
      
      ```
    from fastapi import FastAPI
    import models, dependencies
    from database import engine
    
    
    app = FastAPI()
    
    
    models.Base.metadata.create_all(bind=engine)
    app.include_router(dependencies.router)
    ```
      
      - schemas.py - содержит схемы для валидации данных
    
    ```
    from pydantic import BaseModel
    
    
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
    
    ```
  
  -	env.example - переменные окружения
    
  ```
  JWT_SECRET=
  AUTH_DATABASE_URL=
  POSTGRES_USER=
  POSTGRES_PASSWORD=
  POSTGRES_DB=
  ```
  
  -	docker-compose.yml - база данных и запуск сервиса auth
  
  ```
  version: '3'
  
  services:
    auth:
      build: .
      environment:
        AUTH_DATABASE_URL: ${AUTH_DATABASE_URL}
        JWT_SECRET: ${JWT_SECRET}
      depends_on:
        - auth-db
      ports:
        - "8000:8000"
  
    auth-db:
      image: postgres:13
      environment:
        POSTGRES_USER: ${POSTGRES_USER}
        POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
        POSTGRES_DB: ${POSTGRES_DB}
      volumes:
        - auth_postgres_data:/var/lib/postgresql/data
  
  volumes:
    auth_postgres_data:
  
  ```
  
  -	requirements.txt - список всех библиотек в сервисе

```
  
annotated-types==0.6.0
anyio==4.3.0
click==8.1.7
exceptiongroup==1.2.0
fastapi==0.110.0
h11==0.14.0
idna==3.6
Mako==1.3.2
MarkupSafe==2.1.5
pydantic
asyncpg
pydantic_core==2.16.3
python-dotenv==1.0.1
sniffio==1.3.1
SQLAlchemy==2.0.28
sqlmodel==0.0.16
starlette==0.36.3
typing_extensions==4.10.0
uvicorn==0.27.1
python-dotenv==1.0.1
pyjwt==2.8.0
passlib==1.7.4
psycopg2-binary==2.9.9

```

  -	Dockerfile - конфигурационный файл для сборки Docker-образа и запуска контейнера
  
  ```
  
  FROM python:3.10-alpine
  
  COPY ./src /app
  WORKDIR /app
  
  COPY requirements.txt .
  
  RUN pip install --no-cache-dir -r requirements.txt
  
  COPY . .
  
  CMD ["uvicorn", "main:app", "--port", "8000"]
  
  ```

## Сервис todo для планирования задач

В сервисе todo происходит управление задачами: добавление, чтение, обновление и удаление задач. Данные сохраняются в БД - PostgreSQL (auth_db). 
Микросервис был развёрнут на 8001 порту. Сервис содержит файлы:

-	src:
     - database.py - содержит настройки подключения к базе данных auth_db

      ```
      from sqlalchemy import create_engine
      from sqlalchemy.ext.declarative import declarative_base
      from dotenv import load_dotenv
      from sqlalchemy.orm import sessionmaker
      import os
      
      load_dotenv()
      
      TODO_DATABASE_URL = os.getenv("TODO_DATABASE_URL")
      
      engine = create_engine(TODO_DATABASE_URL)
      SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
      
      Base = declarative_base()
      ```
      
     - dependencies.py - содержит данные о верификации, регистрации и т. д.
 
      ```
      from fastapi import APIRouter, Depends, HTTPException, status
      from sqlalchemy.orm import Session
      import models, schemas
      from database import SessionLocal
      from passlib.context import CryptContext
      from datetime import datetime, timedelta
      import jwt
      import os
      from typing import List
      from fastapi.security import OAuth2PasswordBearer
      
      
      SECRET_KEY = os.getenv("JWT_SECRET")
      ALGORITHM = "HS256"
      ACCESS_TOKEN_EXPIRE_MINUTES = 30
      AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL")
      
      pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
      oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
      
      router = APIRouter()
      
      
      def get_db():
          db = SessionLocal()
          try:
              yield db
          finally:
              db.close()
      def verify_password(plain_password, hashed_password):
          return pwd_context.verify(plain_password, hashed_password)
      
      def get_password_hash(password):
          return pwd_context.hash(password)
      
      def create_access_token(data: dict, expires_delta: timedelta = None):
          to_encode = data.copy()
          if expires_delta:
              expire = datetime.utcnow() + expires_delta
          else:
              expire = datetime.utcnow() + timedelta(minutes=15)
          to_encode.update({"exp": expire})
          encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
          return encoded_jwt
      
      def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
          credentials_exception = HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Could not validate credentials",
              headers={"WWW-Authenticate": "Bearer"},
          )
          try:
              payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
              username: str = payload.get("sub")
              if username is None:
                  raise credentials_exception
          except jwt.PyJWTError:
              raise credentials_exception
          user = db.query(models.User).filter(models.User.username == username).first()
          if user is None:
              raise credentials_exception
          return user
      
      @router.post("/todos/", response_model=schemas.TodoInDB)
      def create_todo(
          todo: schemas.TodoCreate,
          db: Session = Depends(get_db),
          current_user: models.User = Depends(get_current_user),
      ):
          db_todo = models.Todo(**todo.dict(), owner_id=current_user.id)
          db.add(db_todo)
          db.commit()
          db.refresh(db_todo)
          return db_todo
      
      @router.get("/todos/", response_model=List[schemas.TodoInDB])
      def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
          todos = db.query(models.Todo).filter(models.Todo.owner_id == current_user.id).offset(skip).limit(limit).all()
          return todos
      
      @router.put("/todos/{todo_id}", response_model=schemas.TodoInDB)
      def update_todo(
          todo_id: int,
          todo: schemas.TodoUpdate,
          db: Session = Depends(get_db),
          current_user: models.User = Depends(get_current_user),
      ):
          db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == current_user.id).first()
          if db_todo is None:
              raise HTTPException(status_code=404, detail="Todo not found")
          for key, value in todo.dict().items():
              setattr(db_todo, key, value)
          db.commit()
          db.refresh(db_todo)
          return db_todo
      
      @router.delete("/todos/{todo_id}", response_model=schemas.TodoInDB)
      def delete_todo(
          todo_id: int,
          db: Session = Depends(get_db),
          current_user: models.User = Depends(get_current_user),
      ):
          db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == current_user.id).first()
          if db_todo is None:
              raise HTTPException(status_code=404, detail="Todo not found")
          db.delete(db_todo)
          db.commit()
          return db_todo

      ```
 
  
     - main.py - содержит основную точку входа в приложение

      ```
      from fastapi import FastAPI
      import models, dependencies
      from database import engine
        
        
      app = FastAPI()
        
        
      models.Base.metadata.create_all(bind=engine)
      app.include_router(dependencies.router, prefix="/api")

       ```
 
     - models.py -  содержит описание моделей базы данных auth_db.
 
      ```
      
      from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
      from sqlalchemy.orm import relationship
      from database import Base
      
      
      class Todo(Base):
          __tablename__ = "todos"

      id = Column(Integer, primary_key=True, index=True)
      title = Column(String, index=True)
      description = Column(String, index=True)
      completed = Column(Boolean, default=False)
      owner_id = Column(Integer, ForeignKey("users.id"))
  
      owner = relationship("User", back_populates="todos")

      class User(Base):
          __tablename__ = "users"

      id = Column(Integer, primary_key=True, index=True)
      username = Column(String, unique=True, index=True)
      hashed_password = Column(String)

      todos = relationship("Todo", back_populates="owner")

      ```
 
     - schemas.py - содержит схемы для валидации данных

      ```
      
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

 	    ```
 

      
-	env.example - переменные окружения

```
JWT_SECRET=
AUTH_SERVICE_URL=
TODO_DATABASE_URL=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

```

-	docker-compose.yml - база данных и запуск сервиса auth

```

version: '3'

services:
  todo:
    build: .
    environment:
      TODO_DATABASE_URL: ${TODO_DATABASE_URL}
      JWT_SECRET: ${JWT_SECRET}
    depends_on:
      - todo-db
      - auth
    ports:
      - "8001:8001"

  todo-db:
    image: postgres:13
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - todo_postgres_data:/var/lib/postgresql/data

volumes:
  todo_postgres_data:

```

-	requirements.txt - список всех библиотек в сервисе

Список библиотек для todo сервиса такой же, как и в auth
  
-	Dockerfile - конфигурационный файл для сборки Docker-образа и запуска контейнера

 ```
      
 FROM python:3.10-alpine

COPY ./src /app
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--port", "8001"]

```

#### Примечание 

В связи с проблемами в работе Docker, необходимо будет настроить его. Про настройку Dockera можно почитать <a href="https://huecker.io/" target="_blank">тут</a> .


## Работа микросервиса

В ходе реализации курсового проекта были получены следующие результаты:

Работа docker-compose auth service
<p align="center">
  <img src="https://github.com/hanz0m4/microservice/assets/166024789/2bb77283-cce5-4d4a-b885-5aac3c3d8b4a">
</p>


Работа docker-compose todo service
<p align="center">
  <img src="https://github.com/hanz0m4/microservice/assets/166024789/77977b17-96b6-4669-a2c6-de2da130a3ad">
</p>


Запуск на 8000 порту - auth service
<p align="center">
  <img src="https://github.com/hanz0m4/microservice/assets/166024789/e1e20346-6948-4f48-9be8-218da6878a60)">
</p>

Запуск на 8001 порту - todo service
<p align="center">
  <img src="https://github.com/hanz0m4/microservice/assets/166024789/d051ecc1-9cff-4cd8-9da8-94eec4829ade">
</p>

Подключение базы данных PostgreSQL к auth service

<p align="center">
  <img src="https://github.com/hanz0m4/microservice/assets/166024789/6de70033-b555-4195-862c-5bcda62d978c">
</p>



Подключение базы данных PostgreSQL к todo service

<p align="center">
  <img src="https://github.com/hanz0m4/microservice/assets/166024789/82d24309-e2de-40a8-ad6c-28c208b6998d">
</p>


