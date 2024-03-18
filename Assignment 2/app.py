from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

client = MongoClient(host='test_mongodb',
                    port=27017, 
                    username='root', 
                    password='pass',
                    authSource="admin")
db = client["moviesdb"]
collection = db['movies']

movie_model = api.model('Movie', {
    'title': fields.String(required=True, description='Movie title'),
    'genre': fields.String(required=True, description='Movie genre'),
    'director': fields.String(required=True, description='Movie director'),
    'rating': fields.Float(required=True, description='Movie rating')
})


@api.route('/movies')
class Movies(Resource):
    @api.response(200, 'Success')
    def get(self):
        movies = list(collection.find())
        for movie in movies:
            movie['_id'] = str(movie['_id'])
        return movies

    @api.expect(movie_model)
    @api.response(201, 'Movie created successfully')
    def post(self):
        new_movie = request.json
        collection.insert_one(new_movie)
        return {'message': 'Movie created successfully'}, 201


@api.route('/movies/<movie_id>')
class Movie(Resource):
    @api.response(200, 'Success')
    @api.response(404, 'Movie not found')
    def get(self, movie_id):
        movie = collection.find_one({'_id': ObjectId(movie_id)})
        if movie:
            movie['_id'] = str(movie['_id'])
            return movie
        else:
            return {'message': 'Movie not found'}, 404

    @api.expect(movie_model)
    @api.response(200, 'Movie updated successfully')
    @api.response(404, 'Movie not found')
    def put(self, movie_id):
        movie_data = request.json
        updated_movie = collection.update_one({'_id': ObjectId(movie_id)}, {'$set': movie_data})
        if updated_movie.modified_count > 0:
            return {'message': 'Movie updated successfully'}, 200
        else:
            return {'message': 'Movie not found'}, 404

    @api.response(200, 'Movie deleted successfully')
    @api.response(404, 'Movie not found')
    def delete(self, movie_id):
        deleted_movie = collection.delete_one({'_id': ObjectId(movie_id)})
        if deleted_movie.deleted_count > 0:
            return {'message': 'Movie deleted successfully'}, 200
        else:
            return {'message': 'Movie not found'}, 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
