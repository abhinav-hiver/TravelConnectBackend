# Backend Template
Template build on top of fastapi , mysql.
```
This project uses poetry as the dependency manager, alembic as migration manager and sqlAlchemy for Db interactions. 

```
# Steps to run

```
1. docker-compose up #This will start up mysql8 which will be mapped to 3356 port of host machine.
2. pip install poetry 
3. poetry shell      # This will start virual env. All the libraries are present inside this folder and hence all 
commands needs to be run from inside.
4. poetry install
5. alembic upgrade head  #This will create the tables.
6. python -m server.py

RUN below command inside vitual env to format the code:
black .

```
# one command to run db migrations and start server:
```
sh start.sh    

```
# Additional info :
```
Fastapi runs on port 80

```