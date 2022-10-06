from flask import Flask, Blueprint
from flask_cors import CORS
from  flask_restful import Api
from resources import videogames

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
api_bp = Blueprint('api',__name__)
CORS(api_bp)
api = Api(api_bp)
app.register_blueprint(api_bp)


def init_module(app,api):
    videogames.init_module(api)



init_module(app,api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4100)