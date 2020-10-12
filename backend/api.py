import os
from flask import (
    Flask,
    request,
    jsonify,
    abort
)
import json
from flask_cors import CORS
import sys

from database.models import db, setup_db, Show, Actor, Movie
from auth.auth import AuthError, requires_auth

MODELS_PER_PAGE = 10


#db_drop_and_create_all()

app = Flask(__name__)
setup_db(app)
CORS(app)


def paginate_model(request, selection):
    if request:
        page = request.args.get('page', 1, type=int)
    else:
        page = 1
    start = (page-1)*MODELS_PER_PAGE
    end = start + MODELS_PER_PAGE
    models = [m.format() for m in selection]
    current_models = models[start:end]
    return current_models

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    current_movies = paginate_model(request, movies)
    if len(current_movies) == 0:
        abort(404)

    return jsonify({
        'success': True,
        'movies': current_movies,
        'total_movies': len(movies)
    }), 200


@app.route('/actors', methods=['GET'])
def get_actors():
    actors = Actor.query.all()
    current_actors = paginate_model(request, actors)
    if len(current_actors) == 0:
        abort(404)

    return jsonify({
        'success': True,
        'actors': current_actors,
        'totoal_actors': len(actors)
    }), 200

@app.route('/movies', methods=['POST'])
def create_movie():
    body = request.get_json()
    title = body.get('title', '')
    release_date = body.get('release_date', '')
    try:
        movie = Movie(title=title, release_date=release_date)
        movie.insert()

        selection = Movie.query.order_by(Movie.id).all()
        current_movies = paginate_model(request, selection)

        return jsonify({
            'success': True,
            'created': movie.id,
            'total_movies': len(selection),
            'movies': current_movies
        }), 200
    except Exception as e:
        abort(422)


@app.route('/actors', methods=['POST'])
def create_actor():
    body = request.get_json()
    name = body.get('name', '')
    age = body.get('age', 0)
    gender = body.get('gender', 'M')
    try:
        actor = Actor(name=name, age=age, gender=gender)
        actor.insert()

        selection = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_model(request, selection)
        return jsonify({
            'success': True,
            'created': actor.id,
            'actors': current_actors,
            'total_actors': len(selection)
        }), 200
    except Exception as e:
        abort(422)


@app.route('/movies/<int:movie_id>', methods=['PATCH'])
def update_movie(movie_id):
    body = request.get_json()
    title = body.get('title', None)
    if title is None:
        abort(404)

    try:
        movie = Movie.query.filter_by(id=movie_id).one_or_none()
        if movie is None:
            abort(404)
        movie.title = title
        movie.update()

        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200

    except Exception as e:
        abort(422)


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
def update_actor(actor_id):
    body = request.get_json()
    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', None)
    try:
        actor = Actor.query.filter_by(id=actor_id).one_or_none()
        if actor is None:
            abort(404)

        actor.name = actor.name if name is None else name
        actor.age = actor.age if age is None else age
        actor.gender = actor.gender if gender is None else gender

        actor.update()

        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200
    except Exception as e:
        abort(422)

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    try:
        movie = Movie.query.filter_by(id=movie_id).one_or_none()
        
        if movie is None:
            abort(404)
        else:
            movie.delete()
            return jsonify({
                'success': True,
                'delete': movie_id
            }), 200
    except Exception as e:
        abort(422)

@app.route('/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    try:
        actor = Actor.query.filter_by(id=actor_id).one_or_none()
        if actor is None:
            abort(404)
        else:
            actor.delete()
            return jsonify({
                'success': True,
                'delete': actor_id
            })
    except Exception as e:
        abort(422)

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

@app.errorhandler(404)
def not_found(error):
    return jsonify({
                    'success': False,
                    'error': 404,
                    'message': 'resource not found'
                    }), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
                    'success': False,
                    'error': 500,
                    'message': 'internal server error'
                    }), 500

@app.errorhandler(400)
def bad_error(error):
    return jsonify({
                    'success': False,
                    'error': 400,
                    'message': 'bad request'
                    }), 400

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
                    'success': False,
                    'error': 405,
                    'message': 'method not allowed'
                    }), 405

