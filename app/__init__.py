from flask import Flask
from configs import config
from flask_bootstrap import Bootstrap
import os
from peewee import *
from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy
# from . import models
# import os

# mysql = MySQLDatabase(
#     os.environ.get('MYSQL_DATABASE'),
#     user=os.environ.get('MYSQL_USER'),
#     password=os.environ.get('MYSOL_PASSWORD'),
#     host=os.environ.get('MYSQL_HOST'),
#     port=3306
# )

db = MySQLDatabase( 
  os.getenv('MYSQL_DATABASE'),
  user=os.getenv('MYSQL_USER'),
  password=os.getenv('MYSQL_PASSWORD'),
  host=os.getenv('MYSQL_HOST'),
  port=3306
)

# db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()

def create_app(config_profile: str):
    #creates app instance
    app = Flask(__name__)
    app.config.from_object(config[config_profile])

    #init plug ins
    bootstrap.init_app(app)
    moment.init_app(app)
    # db.init_app(app)

    #loads the view(s)
    with app.app_context():
        from . import models

        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

        from .api_v1 import api_v1 as api_v1_blueprint
        app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

        from .main_v2 import main_v2 as main_v2_blueprint
        app.register_blueprint(main_v2_blueprint, url_prefix='/v2')

    # print(app.config)
    # print(mysql)
    #returns app instance
    return app
