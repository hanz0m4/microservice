# Курсовой проект - приложение для управления задачами

В рамках курсовой работы необходимо разработать микросервисное бэкенд приложение на тему "приложение для управления задачами". Данная работа содержит два микросервиса: первый - сервис авторизации, аутенфикации и регистрацию; второй - микросервис управления задачами
Первый микросервис был развёрнут с помощью docker'а на 8000 порту, а второй - на 8001 порту.

#### Примечание 

В связи с проблемами в работе Docker, необходимо будет настроить его. Про настройку Dockera можно почитать <a href="https://huecker.io/" target="_blank">тут</a> .

#### Требования:
-	Приложение включает минимум 2 бэкенд сервиса
-	Каждый сервис должен запускаться в виде отдельного инстанса
-	Переменные окружения каждого сервиса вынесены в .env файле (в репозитории должен быть файл .env.example)
-	Коммуникация между сервиса может осуществляться через: Rest API, grpc, брокер сообщений 
-	База данных описана в docker-compose файле
-	БД в docker-compose для инициализации использует переменные из .env файла
-	В проекте есть файл requirements.txt со списком всех библиотек проекта
-	Каждый сервис содержит Readme файл с указанием задач сервиса, логики работы и инструкцию по запуску


### Решение

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



Подключение базы данных PostgreSQL к auth service

<p align="center">
  <img src="https://github.com/hanz0m4/microservice/assets/166024789/82d24309-e2de-40a8-ad6c-28c208b6998d">
</p>
