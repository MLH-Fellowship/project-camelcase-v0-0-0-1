import os
from flask import Flask, render_template, request
from configs import config
from flask_bootstrap import Bootstrap
from peewee import *
from playhouse.shortcuts import model_to_dict
from crypt import methods
 


from dotenv import load_dotenv

#print("DATOS ++++++++",os.getenv("URL"))

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)
bootstrap = Bootstrap()
def create_app(config_profile: str):
    #creates app instance
    app = Flask(__name__)
    #app.config.from_object(config[config_profile])
    print(mydb)
    #incldue library support
    bootstrap.init_app(app)

    #loads the view(s)
    with app.app_context():
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)
        from . import models
    

    #returns app instance
    return app

