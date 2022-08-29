from flask import Flask, request, jsonify, abort
from database.models import setup_db, Actor, Movie, setup_migrations
from flask_cors import CORS
import sys
import datetime
from werkzeug.exceptions import HTTPException, NotFound, PreconditionFailed
from auth.auth import requires_auth, AuthError


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', "Content-Tpe, Authorization, true")
        response.headers.add('Access-Control-Allow-Methods', "GET, PUT, POST, PATCH, DELETE, OPTIONS")
        return response


    # sample routes:
    @app.route('/')
    def index():
        return jsonify({
            "success": True,
            "message": "Hi, there! This is just a sample route. It means your app is working! Yippeeee!!"
        })


    # routes for movies:
    @app.route('/movies', methods=["GET"])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            movies = Movie.query.all()

            if len(movies) == 0:
                abort(404)

            formatted_movies = [movie.get_formatted_json() for movie in movies]
            return jsonify({
                "success": True,
                "movies": formatted_movies
            })
        except:
            abort(404)
            
    @app.route('/movies/<int:movie_id>', methods=["GET"])
    @requires_auth('get:movie_details')
    def get_movie_details(payload, movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none().get_formatted_json()
            if movie is None:
                abort(404)

            return jsonify({
                "success": True,
                "movie": movie
            })
        except:
            abort(404)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        try:
            data = request.get_json()
            if 'title' not in data or 'release_date' not in data or 'genre'not in data:
                abort(400)
            
            movie = Movie(
                title = data['title'],
                release_date = data['release_date'], 
                genre =  data['genre']
            )
            movie.insert()

            return jsonify({
                "success": True,
                "movie_id": movie.id
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def modify_movie(payload, movie_id):
        try:
            data = request.get_json()

            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            if movie is None:
                abort(404)

            title = data.get('title', None)
            release_date = data.get('release_date', None)
            genre = data.get('genre', None)

            if title != None:
                movie.title = title
            if release_date != None:
                movie.release_date = release_date
            if genre != None:
                movie.genre = genre


            movie.update()

            return jsonify({
                "success": True,
                "movie": movie.get_formatted_json()
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            if movie is None:
                abort(404)
            
            movie.delete()

            return jsonify({
                "success": True,
                "deleted": movie.id
            })
        except:
            abort(404)


    # routes for actors:
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors = Actor.query.all()

            if len(actors) == 0:
                abort(404)
            
            formatted_actors = [actor.get_formatted_json() for actor in actors]
            return jsonify({
                "success": True,
                "actors": formatted_actors
            })
        except:
            abort(404)

    @app.route('/actors/<int:actor_id>', methods=["GET"])
    @requires_auth('get:actor_details')
    def get_actor_details(payload, actor_id):
        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none().get_formatted_json()
            if actor is None:
                abort(404)

            return jsonify({
                "success": True,
                "actor": actor
            })
        except:
            abort(404)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        try:
            data = request.get_json()
            if 'name' not in data or 'age' not in data or 'gender' not in data:
                abort(400)

            actor = Actor(
                name=data['name'],
                age=data['age'], 
                gender=data['gender']
            )
            actor.insert()

            return jsonify({
                "success": True,
                "actor_id": actor.id
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def modify_actor(payload, actor_id):
        try:
            data = request.get_json()

            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
            if actor is None:
                abort(404)

            name = data.get('name', None)
            age = data.get('age', None)
            gender = data.get('gender', None)

            if name != None:
                actor.name = name
            if age != None:
                actor.age = age
            if gender != None:
                actor.gender = gender
            
            actor.update()

            return jsonify({
                "success": True,
                "actor": actor.get_formatted_json()
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):
        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                "success": True,
                "deleted": actor.id
            })
        except:
            abort(404)


    # error handlers:
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400
    
    @app.errorhandler(401)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Not Authorized"
        })

    @app.errorhandler(403)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden"
        }), 403
    
    @app.errorhandler(404)
    def error_resource_not_found(error):
        return jsonify({
            "success": False,
            "message": "Resource not found",
            "error": 404
        }), 404

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(412)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 412,
            "message": "Precondition for resource failed",
            "question": False
        }), 412

    @app.errorhandler(422)
    def not_processable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Request cant be processed"
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "message": "Internal server error",
            "error": 500
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(error):
        print(error)
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
