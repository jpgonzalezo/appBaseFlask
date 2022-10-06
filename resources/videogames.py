import json
from flask import Flask, Blueprint, jsonify, request, send_file, current_app
from flask_restful import Api, Resource, url_for, reqparse
def init_module(api):
    api.add_resource(VideoGames,'/videogames')

class VideoGames(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('auth-token', type = str, required = False, location = 'headers')
        super(VideoGames,self).__init__()
    
    def get(self):
        return {"message":"Hello world2!"}
    
    def post(self):
        #args = self.reqparse.parse_args()
        data = request.data.decode()
        data = json.loads(data)
        print("lo que viene de la solicitud es: ",data)
        return {"message":"Hello user!"}
