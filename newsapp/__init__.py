from flask import Flask

from .extensions import mongo
from .main.routes import main


def create_app():
  app = Flask(__name__)
  app.secret_key = 'many random bytes'
  app.config['MONGO_URI'] = 'mongodb+srv://admin:182182@cluster0.cxaae.mongodb.net/mydb?retryWrites=true&w=majority'
  mongo.init_app(app) 

  app.register_blueprint(main)

  return app