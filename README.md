# PetFamily Project for cmpt470


Members  (Group 21):

Shan Qing, sqing

Yanze Zheng, yanzez

Lei Du, duleid

# master branch
# RUN (docker):

docker-compose build
docker-compose up

Start URL: http://127.0.0.1:8080/


Admin URL：http://127.0.0.1:8080/admin

Admin username: admin

Admin password: admin123...



# RUN (without docker): 

#### you need to change the database SQLite from PostgreSQL, then run command:

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py migrate --run-syncdb

python3 manage.py runserver

Start URL: http://127.0.0.1:8000/

# Learning Reference:

https://www.youtube.com/watch?v=1XiJvIuvqhs&list=PLKILtxhEt4-RT-GkrDkJDLuRPQfSK-6Yi&index=51

https://stackoverflow.com/questions/34548768/django-no-such-table-exception

https://stackoverflow.com/questions/33086444/django-1-8-migrate-is-not-creating-tables

https://www.youtube.com/watch?v=RCE3VUpzGw0&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=10

https://www.djangoproject.com/

