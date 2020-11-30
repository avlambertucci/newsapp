from flask import Flask

from .extensions import mongo
from .main.routes import main


# Função principal que faz as configurações iniciais do MongoDB
def create_app():
  app = Flask(__name__)
  # Foi necessario criar uma secret_key para usar o flash()
  app.secret_key = 'many random bytes'
  app.config['MONGO_URI'] = 'mongodb+srv://admin:182182@cluster0.cxaae.mongodb.net/mydb?retryWrites=true&w=majority'
  mongo.init_app(app) 

  app.register_blueprint(main)

  return app