import os
from flask import Flask, render_template, request
from configs import config
from flask_bootstrap import Bootstrap
from peewee import *
from playhouse.shortcuts import model_to_dict
from crypt import methods
 


from dotenv import load_dotenv 
load_dotenv()
app = Flask(__name__)
#bootstrap.init_app(app)

#print("DATOS ++++++++",os.getenv("URL"))

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

bootstrap = Bootstrap()

