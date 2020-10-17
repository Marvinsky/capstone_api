import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api import create_app
from database.models import setup_db, Show, Movie, Actor
import datetime

class ApiTestCases(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'agencydbtest'
        self.database_path = 'postgres://{}@{}/{}'.format('student', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': 'The client',
            'release_date': datetime.date(2019, 3, 19)
        }

        self.new_movie_fail = {
            'title': 1,
            'release_date': 56
        }

        self.new_actor = {
            'name': 'leonard',
            'age': 40,
            'gender': 'M'
        }

        self.new_actor_fail = {
            'name': 1,
            'age': '40',
            'gender': 110
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):
        pass

    #----------------------GET ACTORS & MOVIES---------------------
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])
        
    def test_get_movies_fail(self):
        res = self.client().get('/movies2')
        self.assertEqual(res.status_code, 404)

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['totoal_actors'])

    def test_get_actors_fail(self):
        res = self.client().get('/actors2')
        self.assertEqual(res.status_code, 404)


    #----------------------POST ACTORS & MOVIES---------------------
    def test_create_movie_success(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_movies'])
        self.assertTrue(data['movies'])


    def test_create_movie_fail(self):
        res = self.client().post('/movies', json=self.new_movie_fail)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)

    
    def test_create_actor_success(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])

    def test_create_actor_fail(self):
        res = self.client().post('/actors', json=self.new_actor_fail)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    #----------------------UPDATE ACTORS & MOVIES---------------------
    def test_update_actor_success(self):
        id_actor = 1
        res = self.client().patch('/actors/' + str(id_actor), json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_update_actor_fail(self):
        id_actor = 20000
        res = self.client().patch('/actors/' + str(id_actor), json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_update_movie_success(self):
        id_movie = 1
        res = self.client().patch('/movies/' + str(id_movie), json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_update_movie_fail(self):
        id_movie = 2000
        res = self.client().patch('/movies/' + str(id_movie), json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    #----------------------DELETE ACTORS & MOVIES---------------------
    def test_delete_actor_success(self):
        id_to_delete = 1
        res = self.client().delete('/actors/' + str(id_to_delete))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor_fail(self):
        id_to_delete = 1000
        res = self.client().delete('/actors/' + str(id_to_delete))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_delete_movie_success(self):
        id_to_delete = 1
        res = self.client().delete('/movies/' + str(id_to_delete))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie_fail(self):
        id_to_delete = 1000
        res = self.client().delete('/movies/' + str(id_to_delete))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)



if __name__ == '__main__':
    unittest.main()

