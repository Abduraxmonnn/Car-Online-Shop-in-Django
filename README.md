## Welcome
### to CAR ONLINE SHOP for BEGINNERS in DJANGO 
by Abdurakhmon


### About the Project
Coming soon. Description about project in progress

### About the BackEnd
Coming soon. Description about BackEnd in progress

***

## Tech

* [Django](https://www.djangoproject.com/) - is a high-level `Python Web framework`
* [Django REST framework](https://www.django-rest-framework.org/) - `Django REST Framework` is a powerful and flexible toolkit for building Web `APIs`
* [PostgreSQL](https://www.postgresql.org/) - open source object-relational database system

And many other libraries.

Dillinger requires [Python](https://www.python.org) v3.4+.

```shell
$ git clone https://gitlab.com/Abduraxmonnn/chehol_api.git
$ cd chat_api
```

***

## Setting project

* `Linux`
```shell
$ virtualenv -p /usr/bin/python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* `Windows`
```shell
$ python -m venv ./venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* `MacBook`
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

***

## Development
### Configure `PostgreSQL`
Create clear database named `car_db`.

Create `car_db_user` db user with password `car_1234` and grand privileges to him.

If you want to create a database with a different name, user and password, you can change the initial configuration to your own configuration.
```shell
$ sudo -u postgres psql
postgres=# ...
CREATE DATABASE car_db;
CREATE USER car_db_user WITH PASSWORD 'car_1234';
ALTER ROLE car_db_user SET client_encoding TO 'utf8';
ALTER ROLE car_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE car_db_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE car_db TO car_db_user;
\q
```
and add the PostgreSQL configuration in core/settings.py

in general the default database is sqlite3 if you do not change anything in core/settings.py DATABASE

Migrate to database and run project.
```shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
`Output`
```shell
System check identified no issues (0 silenced).
Month date, year - hh:mm:ss
Django version 4.2.1, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Open http://127.0.0.1:8000 in your browser for see result.
