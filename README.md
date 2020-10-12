## CAPSTONE PROJECT

### DEPENDENCIES
---
```
pip3 install --upgrade pip
pio3 install flask-cors
pip3 install flask_migrate
pip3 install psycopg2-binary
pip3 install python-jose
postgresql 
```
pip3 install -r requirements.txt

## Create Database
1.- Create database: agencydb and agencydbtest

2.- psql agencydb

3.- psql agencydbtest

## Sepecifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Models
*   Movies with attributes title and release date
*   Actors with attributes name, age and gender

## Endpoints
*   GET /actors and /movies
*   DELETE /actors/<actor_id> and /movies/<movie_id>
*   POST /actors and /movies
*   PATCH /actors and /movies

## Roles
*   Casting Assistant
    *   Can view actors and movies

*   Casting Director
    *   All permissions a Casting has and...
    *   Add or delete an actor from the database
    *   Modify actors or movies

*   Executive Producer
    *   All permisions a Casting Director has and...
    *   Add or delete movie from the database

## Tests
*   One test for success behavior of each endpoint
*   One test for error behavior of each endpoint
*   At least two tests of RBAC for each role


## Scripts DB interacting with Python
```
>>> from api import app
>>> from database.models import db, Show, Actor, Movie
>>> db.create_all()
>>> a = Actor(name='rash', age=20, gender='M')
>>> db.session.add(a)
>>> db.session.commit()
>>> b = Movie(title='TBBT', release_date=datetime.now())
>>> db.session.add(b)
>>> db.session.commit()
>>> s = Show(start_time=datetime.now(), movie_id=1, actor_id=1)
>>> db.session.add(s)
>>> db.session.commit()
```




