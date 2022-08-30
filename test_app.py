import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from database.models import setup_db, Movie, Actor
from app import create_app

TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL')
ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')
PRODUCER_TOKEN = os.getenv('PRODUCER_TOKEN')


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_DATABASE_URI)
        self.casting_assistant = ASSISTANT_TOKEN
        self.casting_director = DIRECTOR_TOKEN
        self.executive_producer = PRODUCER_TOKEN
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.new_movie = {
            "title": "Sample",
            "release_date": "01-01-2016",
            "genre": "XYZ"
        }
        
        self.update_movie = {
            "name": "SAMPLE EDITED"
        }

        self.new_actor = {
            "name": "sample",
            "age": 32,
            "gender": "Male"
        }

        self.update_actor = {
            "name": "SAMPLE CHANGE"
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Testing the sample endpoint
    def test_app_testing(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], 'Hi, there! This is just a sample route. It means your app is working! Yippeeee!!')


    '''
    TESTING ENDPOINTS RELATED TO MOVIES
    '''

    # Testing get /movies for each role and then without token
    def test_get_movies_as_assistant(self):
        res = self.client().get('/movies', headers={'Authorization': f'Bearer {ASSISTANT_TOKEN}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    
    def test_get_movies_as_director(self):
        res = self.client().get('/movies', headers={'Authorization': f'Bearer {DIRECTOR_TOKEN}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movies_as_producer(self):
        res = self.client().get('/movies', headers={'Authorization': f'Bearer {PRODUCER_TOKEN}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movies_without_token(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 403)


    # Testing get /movies/<movie_id> for each role and then without token
    def test_get_movie_by_id_as_assistant(self):
        res = self.client().get('/movies/1', headers={"Authorization": "Bearer " + ASSISTANT_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_get_movie_by_id_as_director(self):
        res = self.client().get('/movies/1', headers={"Authorization": "Bearer " + DIRECTOR_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_get_movie_by_id_as_producer(self):
        res = self.client().get('/movies/1', headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_get_movie_by_id_without_token(self):
        res = self.client().get('/movies/1')
        self.assertEqual(res.status_code, 403)


    # Testing post /movies for each role and then without token
    def test_post_movie_as_assistant(self):
        res = self.client().post('/movies', headers={
            "Authorization": "Bearer " + ASSISTANT_TOKEN}, json=self.new_movie)
        
        self.assertEqual(res.status_code, 403)

    def test_post_movie_as_director(self):
        res = self.client().post('/movies', headers={
            "Authorization": "Bearer " + DIRECTOR_TOKEN}, json=self.new_movie)
        
        self.assertEqual(res.status_code, 403)

    def test_post_movie_as_producer(self):
        res = self.client().post('/movies', headers={
            "Authorization": "Bearer " + PRODUCER_TOKEN}, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movie_id'])

    def test_post_movie_without_token(self):
        res = self.client().post('/movies', json=self.new_movie)
        self.assertEqual(res.status_code, 403)


    # Testing patch /movies for each role and then without token
    def test_patch_movie_as_assistant(self):
        res = self.client().patch('/movies/9', headers={
            "Authorization": "Bearer " + ASSISTANT_TOKEN}, json=self.update_movie)
        
        self.assertEqual(res.status_code, 403)

    def test_patch_movie_as_director(self):
        res = self.client().patch('/movies/9', headers={
            "Authorization": "Bearer " + DIRECTOR_TOKEN}, json=self.update_movie)
        
        self.assertEqual(res.status_code, 200)

    def test_patch_movie_as_producer(self):
        res = self.client().patch('/movies/9', headers={
            "Authorization": "Bearer " + PRODUCER_TOKEN}, json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movie'])
    
    def test_patch_movie_without_token(self):
        res = self.client().post('/movies', json=self.new_movie)
        self.assertEqual(res.status_code, 403)
    


    # Testing delete /movies for each role and then without token
    def test_delete_movie_as_assistant(self):
        res = self.client().delete('/movies/10', headers={"Authorization": "Bearer " + ASSISTANT_TOKEN})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    def test_delete_movie_as_director(self):
        res = self.client().delete('/movies/10', headers={"Authorization": "Bearer " + DIRECTOR_TOKEN})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    def test_delete_movie_as_producer(self):
        res = self.client().get('/movies/10', headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_delete_movie_without_token(self):
        res = self.client().post('/movies', json=self.new_movie)
        self.assertEqual(res.status_code, 403)


    '''
    TESTING ENDPOINTS RELATED TO ACTORS
    '''

    # Testing get /actors for each role and then without token
    def test_get_actors_as_assistant(self):
        res = self.client().get('/actors', headers={'Authorization': f'Bearer {ASSISTANT_TOKEN}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
    
    def test_get_actors_as_director(self):
        res = self.client().get('/actors', headers={'Authorization': f'Bearer {DIRECTOR_TOKEN}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actors_as_producer(self):
        res = self.client().get('/actors', headers={'Authorization': f'Bearer {PRODUCER_TOKEN}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actors_without_token(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 403)


    # Testing get /actors/<actor_id> for each role and then without token
    def test_get_actor_by_id_as_assistant(self):
        res = self.client().get('/actors/1', headers={"Authorization": "Bearer " + ASSISTANT_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_get_actor_by_id_as_director(self):
        res = self.client().get('/actors/1', headers={"Authorization": "Bearer " + DIRECTOR_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_get_actor_by_id_as_producer(self):
        res = self.client().get('/actors/1', headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_get_actor_by_id_without_token(self):
        res = self.client().get('/actors/1')
        self.assertEqual(res.status_code, 403)


    # Testing post /actors for each role and then without token
    def test_post_actor_as_assistant(self):
        res = self.client().post('/actors', headers={
            "Authorization": "Bearer " + ASSISTANT_TOKEN}, json=self.new_actor)
        
        self.assertEqual(res.status_code, 403)

    def test_post_actor_as_director(self):
        res = self.client().post('/actors', headers={
            "Authorization": "Bearer " + DIRECTOR_TOKEN}, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actor_id'])

    def test_post_actor_as_producer(self):
        res = self.client().post('/actors', headers={
            "Authorization": "Bearer " + PRODUCER_TOKEN}, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actor_id'])

    def test_post_actor_without_token(self):
        res = self.client().post('/actors', json=self.new_actor)
        self.assertEqual(res.status_code, 403)


    # Testing patch /actors for each role and then without token
    def test_patch_actor_as_assistant(self):
        res = self.client().patch('/actors/14', headers={
            "Authorization": "Bearer " + ASSISTANT_TOKEN}, json=self.update_actor)
        
        self.assertEqual(res.status_code, 403)

    def test_patch_actor_as_director(self):
        res = self.client().patch('/actors/19', headers={
            "Authorization": "Bearer " + DIRECTOR_TOKEN}, json=self.update_actor)
        
        self.assertEqual(res.status_code, 200)

    def test_patch_actor_as_producer(self):
        res = self.client().patch('/actors/64', headers={
            "Authorization": "Bearer " + PRODUCER_TOKEN}, json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actor'])
    
    def test_patch_actor_without_token(self):
        res = self.client().post('/actors', json=self.new_actor)
        self.assertEqual(res.status_code, 403)


    # Testing delete /actors for each role and then without token
    def test_delete_actor_as_assistant(self):
        res = self.client().delete('/actors/16', headers={"Authorization": "Bearer " + ASSISTANT_TOKEN})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    def test_delete_actor_as_director(self):
        res = self.client().delete('/actors/23', headers={"Authorization": "Bearer " + DIRECTOR_TOKEN})

        self.assertEqual(res.status_code, 200)

    def test_delete_actor_as_producer(self):
        res = self.client().delete('/actors/24', headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    def test_delete_actor_without_token(self):
        res = self.client().post('/actors', json=self.new_movie)
        self.assertEqual(res.status_code, 403)


if __name__ == "__main__":
    unittest.main()