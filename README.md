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
>>> from app import app
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

## Deployment

* git remote add heroku https://git.heroku.com/agencycast.git

* git push heroku HEAD:master

  remote:        https://agencycast.herokuapp.com/ deployed to Heroku


heroku run python manage.py db upgrade --app agencycast

#### ERROR:
python: can't open file 'manage.py': [Errno 2] No such file or directory

* I can run python manage.py runserver and locahost works
* git ls-files manage.py --outputs--> manage.py

However,
* heroku run bash
* ls manage.py
I get: ls: cannot access 'manage.py': No such file or directory

It seems that manage.py is in my local but not in my heroku.

### IF ERROR FIXED
* heroku addons:create heroku-postgresql:hobby-dev --app agencycast

Creating heroku-postgresql:hobby-dev on ⬢ agencycast... free
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-polished-75028 as HEROKU_POSTGRESQL_GOLD_URL
Use heroku addons:docs heroku-postgresql to view documentation


* heroku config --app agencycast
DATABASE_URL:               postgres://jyrksohpzsilpa:0e8d14d644dcb97740ad5af88c23e7611f0b626ff57d634218ff57cff142a001@ec2-52-202-146-43.compute-1.amazonaws.com:5432/df35itb1n1jqq8
EXCITED:                    true
HEROKU_POSTGRESQL_GOLD_URL: postgres://kixtjipjkocnow:c7e43e527e9c53284d16d5ded672180fffeb71c8b8c0db295f867c78a3702795@ec2-18-211-86-133.compute-1.amazonaws.com:5432/d46eiv1qs8kbl1

* git push heroku HEAD:master

* heroku run python manage.py db upgrade --app agencycast

## Third-Partty Authentication

setup.sh


## Create roles in Auth0 - 48 hours
https://mazpe.us.auth0.com/authorize?audience=show&response_type=token&client_id=3lf13WcJ0ciLvsRHvp4umZp3JrgXlwap&redirect_uri=https://127.0.0.1:8080/login-results

returns:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFBMzl5OWhpclh0QmdWSXlRendRNSJ9.eyJpc3MiOiJodHRwczovL21henBlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjY5ODc5YmI0OThlMjAwNmI5MmZhNzAiLCJhdWQiOiJzaG93IiwiaWF0IjoxNjAyOTE3NTk4LCJleHAiOjE2MDI5MjQ3OTgsImF6cCI6IjNsZjEzV2NKMGNpTHZzUkh2cDR1bVpwM0pyZ1hsd2FwIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.H80qhB7db1g8HVFmkzkwTVNPHy6Bk-enwwWEiyvtaPd40CBoNiIIGHk4do3DOAuhDNo-3yIDu45z5_GqsRrc6740x5PM47ijr5t0Fy_rX-lqy7CVN7rJU8WeLifb7xPXglJ-QGYngcS106Jo6oPwPng7m53PM15LQaUUG3iT8SoDtwgRCZr1dr9cWgJTUQbi8EKJdiMvVkPfNdAiEbFB0CCqajujadrNgvKpckkU-Lr9GQzKKitg5RfPmA0iqtGa27yzusoGjSvSm6hDuN7LUSLMJeqTOs-cOL4MVIGynOQujSZQm6gBVf8C9U5799xqgNu1mvj__2SVdipgrzsM_Q

-----------------------------------------------------------------------

https://mazpe.us.auth0.com/authorize?
  audience=show&
  response_type=token&
  client_id=3lf13WcJ0ciLvsRHvp4umZp3JrgXlwap&
  redirect_uri=https://127.0.0.1:8080/login-results

https://127.0.0.1:8080/login-results#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFBMzl5OWhpclh0QmdWSXlRendRNSJ9.eyJpc3MiOiJodHRwczovL21henBlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjU5YjU2MjE1YWIzYTAwNzcyZDA2OGEiLCJhdWQiOiJzaG93IiwiaWF0IjoxNjAyOTIwMDY4LCJleHAiOjE2MDI5MjcyNjgsImF6cCI6IjNsZjEzV2NKMGNpTHZzUkh2cDR1bVpwM0pyZ1hsd2FwIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.NfTypgAaqUCkDEe31TNpT61B60Oag5IVc65VdN8RbZstRon2Uc_AWm9eE6ImP9owytC4a-CNVvRTJMZt2nBXLx60qPTwG7ngUW6F0ft1tNWuk5BR1fOWxaDRz3GGg8RXoGjJwNJucXYckowsPUCeCH6rh68fiZexopcKwdAEFfKV6JB63VJw92OWKIvjd92ib5WUV6iW3BJen-NVlFChaCRTw2qATBytCR21J6pis7P3iRIOXJYmGGwR1iqJ-k_v4zwSsT8ONUs-Bk4wEJb8RhBpNfspwnuYYc_3jACX5XEXykStLH0-3BojDnpOCmq5XXnyjA9UKuN7yiUjuaCWBA&expires_in=7200&token_type=Bearer





